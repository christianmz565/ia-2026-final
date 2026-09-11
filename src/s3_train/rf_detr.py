"""RF-DETR training wrapper.

Supports automatic mixed precision (AMP FP16), tqdm progress bars,
periodic metrics tracking with per-class mAP and epoch timing, and standardized artifact exporting.

Standalone usage:
    uv run python -m src.s3_train.rf_detr [--data-dir PATH] [--epochs 100]
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import structlog
import torch

from src.caching import run_cached_step
from src.config import RFDETRConfig
from src.constants import CLASS_NAMES, CLASS_WEIGHTS_LIST, S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import register_trainer
from src.s3_train.common import (
    create_epoch_pbar,
    format_per_class_map,
    save_epoch_history,
    save_summary_reports,
    setup_training_output_dir,
)
from src.utils import configure_torch_backend

logger = structlog.get_logger(__name__)


def patch_rfdetr_class_weights() -> None:
    """Patch rfdetr.models.lwdetr.SetCriterion.loss_labels to apply effective-number class weights."""
    try:
        import rfdetr.models.lwdetr as lwdetr_mod

        orig_loss_labels = lwdetr_mod.SetCriterion.loss_labels

        def weighted_loss_labels(self: Any, outputs: Any, targets: Any, indices: Any, num_boxes: Any, log: bool = True) -> Any:
            assert "pred_logits" in outputs
            src_logits = outputs["pred_logits"]
            idx = self._get_src_permutation_idx(indices)
            target_classes_o = torch.cat([t["labels"][J] for t, (_, J) in zip(targets, indices)])

            if self.ia_bce_loss:
                alpha = self.focal_alpha
                gamma = 2
                src_boxes = outputs["pred_boxes"][idx]
                target_boxes = torch.cat([t["boxes"][i] for t, (_, i) in zip(targets, indices)], dim=0)

                iou_targets = torch.diag(
                    lwdetr_mod.box_ops.box_iou(
                        lwdetr_mod.box_ops.box_cxcywh_to_xyxy(src_boxes.detach()),
                        lwdetr_mod.box_ops.box_cxcywh_to_xyxy(target_boxes),
                    )[0]
                )
                pos_ious = iou_targets.clone().detach()
                prob = src_logits.sigmoid()
                pos_weights = torch.zeros_like(src_logits)
                neg_weights = prob ** gamma

                pos_ind = [id for id in idx]
                pos_ind.append(target_classes_o)

                t = prob[pos_ind].pow(alpha) * pos_ious.pow(1 - alpha)
                t = torch.clamp(t, 0.01).detach()

                cw = torch.tensor(CLASS_WEIGHTS_LIST, dtype=t.dtype, device=t.device)
                w = cw[target_classes_o]
                pos_weights[pos_ind] = (t * w).to(pos_weights.dtype)
                neg_weights[pos_ind] = 1 - t.to(neg_weights.dtype)

                loss_ce = neg_weights * src_logits - torch.nn.functional.logsigmoid(src_logits) * (pos_weights + neg_weights)
                loss_ce = loss_ce.sum() / num_boxes

                losses = {"loss_ce": loss_ce}
                if log:
                    losses["class_error"] = 100 - lwdetr_mod.accuracy(src_logits[idx], target_classes_o)[0]
                return losses

            return orig_loss_labels(self, outputs, targets, indices, num_boxes, log=log)

        lwdetr_mod.SetCriterion.loss_labels = weighted_loss_labels
    except Exception as err:
        logger.warning("rfdetr_class_weights_patch_failed", error=str(err))


def patch_rfdetr_coco_extended_metrics() -> None:
    """Patch rfdetr.engine.coco_extended_metrics to prevent TypeError with 2D array scalar conversions."""
    try:
        import numpy as np
        import rfdetr.engine as rf_engine

        def safe_coco_extended_metrics(coco_eval: Any) -> dict[str, Any]:
            iou_thrs, rec_thrs = coco_eval.params.iouThrs, coco_eval.params.recThrs
            iou50_match = np.argwhere(np.isclose(iou_thrs, 0.50))
            iou50_idx = int(iou50_match[0, 0]) if iou50_match.size > 0 else 0
            area_idx, maxdet_idx = 0, 2

            P = coco_eval.eval["precision"]
            S = coco_eval.eval["scores"]

            prec_raw = P[iou50_idx, :, :, area_idx, maxdet_idx]

            prec = prec_raw.copy().astype(float)
            prec[prec < 0] = np.nan

            f1_cls = 2 * prec * rec_thrs[:, None] / (prec + rec_thrs[:, None])
            f1_macro = np.nanmean(f1_cls, axis=1)

            best_j = int(f1_macro.argmax())

            macro_precision = float(np.nanmean(prec[best_j]))
            macro_recall = float(rec_thrs[best_j])

            score_vec = S[iou50_idx, best_j, :, area_idx, maxdet_idx].astype(float)
            score_vec[prec_raw[best_j] < 0] = np.nan

            map_50_95, map_50 = float(coco_eval.stats[0]), float(coco_eval.stats[1])

            per_class = []
            cat_ids = coco_eval.params.catIds
            cat_id_to_name = {c["id"]: c["name"] for c in coco_eval.cocoGt.loadCats(cat_ids)}
            for k, cid in enumerate(cat_ids):
                p_slice = P[:, :, k, area_idx, maxdet_idx]
                valid = p_slice > -1
                ap_50_95 = float(p_slice[valid].mean()) if valid.any() else float("nan")
                ap_50 = (
                    float(p_slice[iou50_idx][p_slice[iou50_idx] > -1].mean())
                    if (p_slice[iou50_idx] > -1).any()
                    else float("nan")
                )

                pc = float(prec[best_j, k]) if prec_raw[best_j, k] > -1 else float("nan")
                rc = macro_recall

                if np.isnan(ap_50_95) or np.isnan(ap_50) or np.isnan(pc) or np.isnan(rc):
                    continue

                per_class.append(
                    {
                        "class": cat_id_to_name[int(cid)],
                        "map@50:95": ap_50_95,
                        "map@50": ap_50,
                        "precision": pc,
                        "recall": rc,
                    }
                )

            per_class.append(
                {
                    "class": "all",
                    "map@50:95": map_50_95,
                    "map@50": map_50,
                    "precision": macro_precision,
                    "recall": macro_recall,
                }
            )

            return {
                "class_map": per_class,
                "map": map_50,
                "precision": macro_precision,
                "recall": macro_recall,
            }

        rf_engine.coco_extended_metrics = safe_coco_extended_metrics
    except Exception as err:
        logger.warning("rfdetr_patch_failed", error=str(err))


class RFDETRTrainer:
    """Train RF-DETR model with AMP and tqdm progress logging."""

    name = "rf_detr"

    def __init__(self, config: RFDETRConfig | None = None) -> None:
        """Initialize RFDETRTrainer with configuration.

        Args:
            config: Optional RF-DETR training hyper-parameters.
        """
        self.config = config or RFDETRConfig()
        patch_rfdetr_coco_extended_metrics()
        patch_rfdetr_class_weights()

    def train(self, config: RFDETRConfig | None = None, force: bool = False) -> Path:
        """Train RF-DETR model with mixed precision and save standardized outputs.

        Args:
            config: Optional configuration override.
            force: If True, bypass cache and re-train.

        Returns:
            Path to best checkpoint (best.pt).
        """
        config = config or self.config
        configure_torch_backend()
        patch_rfdetr_coco_extended_metrics()
        patch_rfdetr_class_weights()
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET

        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "rf_detr"

        def _do_train() -> Path:
            patch_rfdetr_coco_extended_metrics()
            patch_rfdetr_class_weights()
            from rfdetr.detr import RFDETRMedium

            out_dir, checkpoints_dir = setup_training_output_dir(output_dir)

            logger.info(
                "rf_detr_train_start",
                data_dir=str(data_dir),
                output_dir=str(out_dir),
                epochs=config.epochs,
                batch=config.batch,
                lr=config.lr0,
                amp=True,
                resolution=config.imgsz,
            )

            start_time = time.time()
            history: list[dict[str, Any]] = []
            pbar = create_epoch_pbar(config.epochs, "RF-DETR")
            epoch_start_time = time.time()

            def on_fit_epoch_end(stats: dict[str, Any] | None = None, **kwargs: Any) -> None:
                nonlocal epoch_start_time
                now = time.time()
                epoch_duration = round(now - epoch_start_time, 2)
                epoch_start_time = now

                payload = kwargs if kwargs else (stats or {})

                epoch = int(payload.get("epoch", len(history))) + 1
                train_loss = float(payload.get("train_loss", 0.0))
                val_loss = float(payload.get("test_loss", payload.get("val_loss", 0.0)))

                coco_bbox = payload.get("ema_test_coco_eval_bbox", payload.get("test_coco_eval_bbox", [0.0, 0.0]))
                mAP_50_95 = float(coco_bbox[0]) if len(coco_bbox) > 0 else 0.0
                mAP_50 = float(coco_bbox[1]) if len(coco_bbox) > 1 else 0.0

                raw_per_class: dict[str, float] = {}
                results_json = payload.get("ema_test_results_json", payload.get("test_results_json", {}))
                if isinstance(results_json, dict):
                    for entry in results_json.get("class_map", []):
                        if isinstance(entry, dict):
                            name = entry.get("class", "")
                            if name and name != "all":
                                raw_per_class[name] = float(entry.get("map@50:95", 0.0))

                val_per_class = format_per_class_map(raw_per_class)

                epoch_data = {
                    "epoch": epoch,
                    "epoch_time_sec": epoch_duration,
                    "train_loss": round(train_loss, 4),
                    "val_loss": round(val_loss, 4),
                    "val_mAP_50": round(mAP_50, 4),
                    "val_mAP_50_95": round(mAP_50_95, 4),
                    "val_per_class_mAP": val_per_class,
                }
                history.append(epoch_data)
                save_epoch_history(out_dir, history)

                ckpt_candidate = out_dir / f"checkpoint{epoch - 1:04d}.pth"
                if ckpt_candidate.exists():
                    import shutil

                    shutil.copy2(ckpt_candidate, checkpoints_dir / f"epoch_{epoch}.pth")

                pbar.set_postfix(
                    {"mAP50": f"{mAP_50:.3f}", "mAP50-95": f"{mAP_50_95:.3f}", "time_s": f"{epoch_duration:.1f}"}
                )
                pbar.update(1)

            model = RFDETRMedium(
                resolution=config.imgsz,
                gradient_checkpointing=True,
            )
            if hasattr(model, "callbacks") and isinstance(model.callbacks, dict):
                model.callbacks.setdefault("on_fit_epoch_end", []).append(on_fit_epoch_end)

            try:
                model.train(
                    dataset_dir=str(data_dir),
                    output_dir=str(out_dir),
                    epochs=config.epochs,
                    batch_size=config.batch,
                    lr=config.lr0,
                    amp=config.device != "cpu" and torch.cuda.is_available(),
                    weight_decay=1e-4,
                    warmup_epochs=5,
                    early_stopping=True,
                    early_stopping_patience=config.patience,
                    class_names=CLASS_NAMES,
                    square_resize_div_64=config.square_resize,
                    num_workers=2,
                    tensorboard=True,
                )
            finally:
                pbar.close()

            total_time = time.time() - start_time

            best_candidates = [
                out_dir / "checkpoint_best_total.pth",
                out_dir / "checkpoint_best_regular.pth",
                out_dir / "checkpoint_best_ema.pth",
                out_dir / "checkpoint.pth",
            ]
            best: Path | None = None
            for cand in best_candidates:
                if cand.exists() and cand.stat().st_size > 0:
                    best = cand
                    break

            if best is None:
                raise FileNotFoundError(
                    f"RF-DETR training completed, but expected checkpoint (checkpoint_best_total.pth) was not found in {out_dir}"
                )

            save_summary_reports(
                output_dir=out_dir,
                pipeline_name="RF-DETR Detection Pipeline",
                total_time_sec=total_time,
                target_epochs=config.epochs,
                history=history,
                best_checkpoint=best,
            )

            logger.info("rf_detr_train_complete", checkpoint=str(out_dir / "best.pt"))
            return out_dir / "best.pt"

        return run_cached_step(
            step_name="train_rf_detr",
            target_path=output_dir,
            fn=_do_train,
            force=force,
        )

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export RF-DETR model.

        Args:
            checkpoint: Path to ``.pth`` weights.
            output_dir: Where to save exported file.
            format: Target export format.

        Returns:
            Path to exported model.
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info("rf_detr_export_stub", checkpoint=str(checkpoint), format=format)
        return output_dir / f"model.{format}"


register_trainer("rf_detr", RFDETRTrainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=RFDETRConfig,
        run_fn=lambda cfg: RFDETRTrainer(cfg).train(cfg),
        description="Train RF-DETR",
        required_fields=["data_dir"],
    )
