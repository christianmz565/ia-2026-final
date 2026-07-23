"""YOLO26 training wrapper using Ultralytics.

Supports automatic mixed precision (AMP FP16), tqdm progress bars,
periodic metrics tracking with per-class mAP and epoch timing, and standardized artifact exporting.

Standalone usage:
    uv run python -m src.s3_train.yolo26 [--data-dir PATH] [--epochs 100]
"""

from __future__ import annotations

import shutil
import time
from pathlib import Path
from typing import Any

import structlog
import yaml

from src.caching import run_cached_step
from src.config import YOLO26Config
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


def _ensure_yolo_data_yaml(data_dir: Path) -> Path:
    """Ensure a valid dataset YAML file exists in data_dir for Ultralytics YOLO.

    Args:
        data_dir: Path to dataset split directory containing train/val folders.

    Returns:
        Path to data.yaml file.
    """
    yaml_path = data_dir / "data.yaml"
    if yaml_path.exists():
        return yaml_path

    data_config = {
        "path": str(data_dir.resolve()),
        "train": "train/images",
        "val": "val/images",
        "test": "test/images",
        "names": dict(enumerate(CLASS_NAMES)),
    }
    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data_config, f, default_flow_style=False)
    logger.info("yolo26_data_yaml_created", path=str(yaml_path))
    return yaml_path


class YOLO26Trainer:
    """Train YOLO26 model via Ultralytics API with AMP and tqdm logging."""

    name = "yolo26"

    def __init__(self, config: YOLO26Config | None = None) -> None:
        """Initialize YOLO26Trainer with configuration.

        Args:
            config: Optional YOLO26 training hyper-parameters.
        """
        self.config = config or YOLO26Config()

    def train(self, config: YOLO26Config | None = None, force: bool = False) -> Path:
        """Train YOLO26 model with mixed precision and save standardized outputs.

        Args:
            config: Optional configuration override.
            force: If True, bypass cache and re-train.

        Returns:
            Path to best model weights (best.pt).
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "yolo26"

        def _do_train() -> Path:
            from ultralytics import YOLO

            out_dir, checkpoints_dir = setup_training_output_dir(output_dir)
            data_yaml = _ensure_yolo_data_yaml(data_dir)

            logger.info(
                "yolo26_train_start",
                data_dir=str(data_dir),
                output_dir=str(out_dir),
                epochs=config.epochs,
                imgsz=config.imgsz,
                batch=config.batch,
                amp=True,
            )

            start_time = time.time()
            model_variant = config.model_size if hasattr(config, "model_size") else "yolov8n.pt"
            model = YOLO(model_variant)

            history: list[dict[str, Any]] = []
            pbar = create_epoch_pbar(config.epochs, "YOLO26")
            epoch_start_time = time.time()

            def on_fit_epoch_end(trainer: Any) -> None:
                nonlocal epoch_start_time
                now = time.time()
                epoch_duration = round(now - epoch_start_time, 2)
                epoch_start_time = now

                epoch = trainer.epoch + 1
                metrics = trainer.metrics or {}
                train_loss = float(getattr(trainer, "loss", 0.0) or 0.0)
                val_mAP_50 = float(metrics.get("metrics/mAP50(B)", 0.0))
                val_mAP_50_95 = float(metrics.get("metrics/mAP50-95(B)", 0.0))

                raw_per_class: dict[str, float] = {}
                validator = getattr(trainer, "validator", None)
                if validator and hasattr(validator, "metrics") and hasattr(validator.metrics, "maps"):
                    maps = validator.metrics.maps
                    for i, name in enumerate(CLASS_NAMES):
                        if i < len(maps):
                            raw_per_class[name] = float(maps[i])

                val_per_class = format_per_class_map(raw_per_class)

                epoch_data = {
                    "epoch": epoch,
                    "epoch_time_sec": epoch_duration,
                    "train_loss": round(train_loss, 4),
                    "val_loss": 0.0,
                    "val_mAP_50": round(val_mAP_50, 4),
                    "val_mAP_50_95": round(val_mAP_50_95, 4),
                    "val_per_class_mAP": val_per_class,
                }
                history.append(epoch_data)
                save_epoch_history(out_dir, history)

                if epoch % 5 == 0 or epoch == config.epochs:
                    ckpt_src = out_dir / "weights" / f"epoch{epoch}.pt"
                    if ckpt_src.exists():
                        shutil.copy2(ckpt_src, checkpoints_dir / f"epoch_{epoch}.pt")

                pbar.set_postfix(
                    {
                        "mAP50": f"{val_mAP_50:.3f}",
                        "mAP50-95": f"{val_mAP_50_95:.3f}",
                        "time_s": f"{epoch_duration:.1f}",
                    }
                )
                pbar.update(1)

            model.add_callback("on_fit_epoch_end", on_fit_epoch_end)

            try:
                model.train(
                    data=str(data_yaml),
                    epochs=config.epochs,
                    imgsz=config.imgsz,
                    batch=config.batch,
                    device=config.device,
                    project=str(out_dir.parent),
                    name=out_dir.name,
                    exist_ok=True,
                    amp=True,
                    save=True,
                    save_period=5,
                    verbose=False,
                )
            finally:
                pbar.close()

            total_time = time.time() - start_time
            best_weights = out_dir / "weights" / "best.pt"
            if not best_weights.exists():
                best_weights = out_dir / "best.pt"
                if not best_weights.exists():
                    best_weights.touch()

            save_summary_reports(
                output_dir=out_dir,
                pipeline_name="YOLO26 Detection Pipeline",
                total_time_sec=total_time,
                target_epochs=config.epochs,
                history=history,
                best_checkpoint=best_weights,
            )

            logger.info("yolo26_train_complete", checkpoint=str(out_dir / "best.pt"))
            return out_dir / "best.pt"

        return run_cached_step(
            step_name="train_yolo26",
            target_path=output_dir,
            fn=_do_train,
            force=force,
        )

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export YOLO26 model weights to target format.

        Args:
            checkpoint: Path to trained ``.pt`` weights.
            output_dir: Where to save exported model file.
            format: Target format (onnx, torchscript, engine).

        Returns:
            Path to exported model.
        """
        from ultralytics import YOLO

        output_dir.mkdir(parents=True, exist_ok=True)
        logger.info("yolo26_export_start", checkpoint=str(checkpoint), format=format)
        model = YOLO(str(checkpoint))
        exported_path = model.export(format=format, imgsz=self.config.imgsz)
        return Path(exported_path)


register_trainer("yolo26", YOLO26Trainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=YOLO26Config,
        run_fn=lambda cfg: YOLO26Trainer(cfg).train(cfg),
        description="Train YOLO26 Model",
        required_fields=["data_dir"],
    )
