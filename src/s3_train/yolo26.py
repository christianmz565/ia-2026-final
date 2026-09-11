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
import torch
import yaml

from src.caching import config_fingerprint, run_cached_step
from src.config import YOLO26Config
from src.constants import (
    CLASS_NAMES,
    CLASS_WEIGHTS_LIST,
    S3_OUTPUT,
    SPLIT_DATASET,
    TEST_SPLIT,
    TRAIN_SPLIT,
    VALID_SPLIT,
)
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
        "train": f"{TRAIN_SPLIT}/images",
        "val": f"{VALID_SPLIT}/images",
        "test": f"{TEST_SPLIT}/images",
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
        configure_torch_backend()
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "yolo26"

        def _do_train() -> Path:
            from ultralytics import YOLO

            out_dir, checkpoints_dir = setup_training_output_dir(output_dir)
            data_yaml = _ensure_yolo_data_yaml(data_dir)

            model_variant = config.model_size
            if not model_variant:
                raise ValueError("YOLO26Config.model_size must not be empty")

            logger.info(
                "yolo26_train_start",
                data_dir=str(data_dir),
                output_dir=str(out_dir),
                model_size=model_variant,
                epochs=config.epochs,
                imgsz=[config.target_height, config.target_width],
                batch=config.batch,
                lr0=config.lr0,
                device=config.device,
                freeze_layer_count=config.freeze_layer_count,
                amp=True,
            )

            start_time = time.time()
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
                if not isinstance(trainer.metrics, dict):
                    raise ValueError(f"YOLO trainer metrics missing at epoch {epoch}")
                metrics = trainer.metrics
                try:
                    val_mAP_50 = float(metrics["metrics/mAP50(B)"])
                    val_mAP_50_95 = float(metrics["metrics/mAP50-95(B)"])
                except KeyError as err:
                    raise ValueError(f"YOLO trainer metrics missing {err} at epoch {epoch}") from err
                train_loss = float(trainer.loss)

                validator = getattr(trainer, "validator", None)
                validator_metrics = getattr(validator, "metrics", None)
                maps = getattr(validator_metrics, "maps", None)
                if maps is None or len(maps) < len(CLASS_NAMES):
                    raise ValueError(
                        f"YOLO validator maps missing or short at epoch {epoch}: "
                        f"got {None if maps is None else len(maps)}, need {len(CLASS_NAMES)}"
                    )
                raw_per_class: dict[str, float] = {}
                for i, name in enumerate(CLASS_NAMES):
                    raw_per_class[name] = float(maps[i])
                val_per_class = format_per_class_map(raw_per_class)

                epoch_data = {
                    "epoch": epoch,
                    "epoch_time_sec": epoch_duration,
                    "train_loss": round(train_loss, 4),
                    "val_loss": None,
                    "val_mAP_50": round(val_mAP_50, 4),
                    "val_mAP_50_95": round(val_mAP_50_95, 4),
                    "val_per_class_mAP": val_per_class,
                }
                history.append(epoch_data)
                save_epoch_history(out_dir, history)

                if epoch % 5 == 0 or epoch == config.epochs:
                    ckpt_src = out_dir / "weights" / f"epoch{epoch}.pt"
                    if not ckpt_src.exists():
                        raise FileNotFoundError(f"Expected YOLO epoch checkpoint not found: {ckpt_src}")
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

            def on_pretrain_routine_end(trainer: Any) -> None:
                weights_tensor = torch.tensor(CLASS_WEIGHTS_LIST, dtype=torch.float32)
                trainer.model.class_weights = weights_tensor
                if hasattr(trainer, "criterion") and hasattr(trainer.criterion, "class_weights"):
                    trainer.criterion.class_weights = weights_tensor.to(trainer.device).view(1, 1, -1)

            model.add_callback("on_pretrain_routine_end", on_pretrain_routine_end)

            try:
                train_kwargs: dict[str, Any] = {
                    "data": str(data_yaml),
                    "epochs": config.epochs,
                    "imgsz": [config.target_height, config.target_width],
                    "rect": config.rect,
                    "batch": config.batch,
                    "lr0": config.lr0,
                    "device": config.device,
                    "project": str(out_dir.parent),
                    "name": out_dir.name,
                    "exist_ok": True,
                    "amp": config.device != "cpu" and torch.cuda.is_available(),
                    "patience": config.patience,
                    "workers": 2,
                    "save": True,
                    "save_period": 5,
                    "verbose": False,
                }
                if config.freeze_layer_count is not None:
                    train_kwargs["freeze"] = config.freeze_layer_count
                model.train(**train_kwargs)

            finally:
                pbar.close()

            total_time = time.time() - start_time
            best_candidates = [
                out_dir / "weights" / "best.pt",
                out_dir / "weights" / "last.pt",
                out_dir / "best.pt",
            ]
            best_weights: Path | None = None
            for cand in best_candidates:
                if cand.exists() and cand.stat().st_size > 0:
                    best_weights = cand
                    break

            if best_weights is None:
                raise FileNotFoundError(
                    f"YOLO26 training completed, but expected weights file (weights/best.pt) was not found in {out_dir}"
                )

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
            fingerprint=config_fingerprint(config),
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
        exported_path = model.export(format=format, imgsz=[self.config.target_height, self.config.target_width])
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
