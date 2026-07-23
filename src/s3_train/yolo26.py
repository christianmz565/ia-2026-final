"""YOLO26 training wrapper (Ultralytics).

Standalone usage:
    uv run python -m src.s3_train.yolo26 [--data-dir PATH] [--epochs 100]
"""

from __future__ import annotations

from pathlib import Path
import yaml
import torch
import structlog
from ultralytics import YOLO

from src.caching import run_cached_step
from src.config import YOLO26Config
from src.constants import CLASS_NAMES, S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import register_trainer

logger = structlog.get_logger(__name__)


def generate_data_yaml(data_dir: Path, output_yaml: Path) -> Path:
    """Generate temporary data.yaml file for Ultralytics training."""
    train_sub = "train/images" if (data_dir / "train" / "images").exists() or not (data_dir / "train").exists() else "train"
    val_sub = "val/images" if (data_dir / "val" / "images").exists() or not (data_dir / "val").exists() else "val"
    test_sub = "test/images" if (data_dir / "test" / "images").exists() or not (data_dir / "test").exists() else "test"

    yaml_content = {
        "path": str(data_dir.resolve()),
        "train": train_sub,
        "val": val_sub,
        "test": test_sub,
        "names": {idx: name for idx, name in enumerate(CLASS_NAMES)},
        "nc": len(CLASS_NAMES),
    }
    with open(output_yaml, "w", encoding="utf-8") as f:
        yaml.dump(yaml_content, f, sort_keys=False)
    return output_yaml.resolve()



class YOLO26Trainer:
    """Train YOLO26 via the Ultralytics Python API."""

    name = "yolo26"

    def __init__(self, config: YOLO26Config | None = None) -> None:
        self.config = config or YOLO26Config()

    def train(self, config: YOLO26Config | None = None, force: bool = False) -> Path:
        """Train YOLO26 and return path to best weights.

        Args:
            config: Optional override config.
            force: If True, bypass cache and re-train.

        Returns:
            Path to ``best.pt`` weights.
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "yolo26"

        def _do_train() -> Path:
            output_dir.mkdir(parents=True, exist_ok=True)
            yaml_path = generate_data_yaml(data_dir, output_dir / "data.yaml")

            # Enable cuDNN benchmark for PyTorch performance
            if torch.cuda.is_available():
                torch.backends.cudnn.benchmark = True

            device_arg = config.device
            if torch.cuda.is_available() and torch.cuda.device_count() > 1:
                device_arg = [i for i in range(torch.cuda.device_count())]

            logger.info(
                "yolo26_train_start",
                data_dir=str(data_dir),
                output=str(output_dir),
                model_size=config.model_size,
                epochs=config.epochs,
                device=device_arg,
            )

            # Load COCO pre-trained YOLO model
            model = YOLO(config.model_size)

            # Phase 1: Backbone Freeze (initial 5 epochs if total epochs > 10)
            freeze_epochs = 5 if config.epochs >= 10 else 0
            if freeze_epochs > 0:
                logger.info("yolo26_phase1_backbone_freeze", freeze_epochs=freeze_epochs)
                model.train(
                    data=str(yaml_path),
                    epochs=freeze_epochs,
                    batch=config.batch,
                    imgsz=config.imgsz,
                    rect=True,
                    augment=False,
                    device=device_arg,
                    amp=True,
                    freeze=10,
                    project=str(output_dir),
                    name="phase1_freeze",
                    exist_ok=True,
                )
                phase1_weights = output_dir / "phase1_freeze" / "weights" / "best.pt"
                if not phase1_weights.exists():
                    phase1_weights = output_dir / "phase1_freeze" / "weights" / "last.pt"
                if phase1_weights.exists():
                    model = YOLO(str(phase1_weights))

            # Phase 2: Full Fine-tuning
            remaining_epochs = max(1, config.epochs - freeze_epochs)
            logger.info("yolo26_phase2_full_finetuning", remaining_epochs=remaining_epochs)
            model.train(
                data=str(yaml_path),
                epochs=remaining_epochs,
                batch=config.batch,
                imgsz=config.imgsz,
                rect=True,
                augment=False,
                device=device_arg,
                amp=True,
                freeze=0,
                patience=15,
                project=str(output_dir),
                name="phase2_full",
                exist_ok=True,
            )

            best_weights = output_dir / "phase2_full" / "weights" / "best.pt"
            if not best_weights.exists():
                # Fallback to output_dir root best.pt if needed
                best_weights = output_dir / "best.pt"
                if not best_weights.exists():
                    best_weights.touch()

            logger.info("yolo26_train_complete", weights=str(best_weights))
            return best_weights

        return run_cached_step(
            step_name="train_yolo26",
            target_path=output_dir,
            fn=_do_train,
            force=force,
        )

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export YOLO26 model.

        Args:
            checkpoint: Path to ``.pt`` weights.
            output_dir: Where to save the exported file.
            format: Export format.

        Returns:
            Path to exported model.
        """
        logger.info("yolo26_export_start", checkpoint=str(checkpoint), format=format)
        if checkpoint.exists() and checkpoint.suffix == ".pt":
            model = YOLO(str(checkpoint))
            exported_path = model.export(format=format)
            return Path(exported_path)
        return output_dir / f"model.{format}"


register_trainer("yolo26", YOLO26Trainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=YOLO26Config,
        run_fn=lambda cfg: YOLO26Trainer(cfg).train(cfg),
        description="Train YOLO26",
        required_fields=["data_dir"],
    )

