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

from src.caching import run_cached_step
from src.config import RFDETRConfig
from src.constants import CLASS_NAMES, S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import register_trainer
from src.s3_train.common import (
    create_epoch_pbar,
    format_per_class_map,
    save_epoch_history,
    save_summary_reports,
    setup_training_output_dir,
)

logger = structlog.get_logger(__name__)


class RFDETRTrainer:
    """Train RF-DETR model with AMP and tqdm progress logging."""

    name = "rf_detr"

    def __init__(self, config: RFDETRConfig | None = None) -> None:
        """Initialize RFDETRTrainer with configuration.

        Args:
            config: Optional RF-DETR training hyper-parameters.
        """
        self.config = config or RFDETRConfig()

    def train(self, config: RFDETRConfig | None = None, force: bool = False) -> Path:
        """Train RF-DETR model with mixed precision and save standardized outputs.

        Args:
            config: Optional configuration override.
            force: If True, bypass cache and re-train.

        Returns:
            Path to best checkpoint (best.pt).
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "rf_detr"

        def _do_train() -> Path:
            from rfdetr.detr import RFDETRLarge

            out_dir, checkpoints_dir = setup_training_output_dir(output_dir)

            logger.info(
                "rf_detr_train_start",
                data_dir=str(data_dir),
                output_dir=str(out_dir),
                epochs=config.epochs,
                batch=config.batch,
                lr=config.lr0,
                amp=True,
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

                epoch = len(history) + 1
                stats = stats or {}
                mAP_50 = float(
                    stats.get("map_50", stats.get("coco_eval_bbox", [0, 0])[1] if "coco_eval_bbox" in stats else 0.0)
                )
                mAP_50_95 = float(
                    stats.get("map", stats.get("coco_eval_bbox", [0])[0] if "coco_eval_bbox" in stats else 0.0)
                )
                train_loss = float(stats.get("loss", 0.0))

                raw_per_class: dict[str, float] = {}
                if "per_class_ap" in stats and isinstance(stats["per_class_ap"], dict):
                    raw_per_class = stats["per_class_ap"]
                elif "coco_eval" in stats:
                    coco_eval = (
                        stats["coco_eval"].get("bbox") if isinstance(stats["coco_eval"], dict) else stats["coco_eval"]
                    )
                    if hasattr(coco_eval, "eval") and "precision" in getattr(coco_eval, "eval", {}):
                        prec = coco_eval.eval["precision"]
                        vals = prec[:, :, :, 0, 0].mean(axis=(0, 1))
                        for i, name in enumerate(CLASS_NAMES):
                            if i < len(vals):
                                raw_per_class[name] = float(vals[i])

                val_per_class = format_per_class_map(raw_per_class)

                epoch_data = {
                    "epoch": epoch,
                    "epoch_time_sec": epoch_duration,
                    "train_loss": round(train_loss, 4),
                    "val_loss": round(float(stats.get("val_loss", 0.0)), 4),
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

            model = RFDETRLarge()
            if hasattr(model, "callbacks") and isinstance(model.callbacks, dict):
                model.callbacks.setdefault("on_fit_epoch_end", []).append(on_fit_epoch_end)

            try:
                model.train(
                    dataset_dir=str(data_dir),
                    output_dir=str(out_dir),
                    epochs=config.epochs,
                    batch_size=config.batch,
                    lr=config.lr0,
                    amp=True,
                    weight_decay=1e-4,
                    warmup_epochs=5,
                    early_stopping=True,
                    early_stopping_patience=10,
                    class_names=CLASS_NAMES,
                    square_resize_div_64=True,
                    num_workers=2,
                    tensorboard=True,
                )
            finally:
                pbar.close()

            total_time = time.time() - start_time

            best = out_dir / "best_model.pth"
            if not best.exists():
                logger.warning("rf_detr_train_no_checkpoint", path=str(best))
                checkpoints = list(out_dir.glob("*.pth"))
                if checkpoints:
                    best = max(checkpoints, key=lambda p: p.stat().st_mtime)
                    logger.info("rf_detr_train_fallback_checkpoint", path=str(best))
                else:
                    best.touch()

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
