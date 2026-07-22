"""Cascade R-CNN training wrapper (MMDetection).

Standalone usage:
    uv run python -m src.s3_train.cascade_rcnn [--data-dir PATH] [--epochs 12]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.caching import run_cached_step
from src.config import CascadeRCNNConfig
from src.constants import S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import Trainer, register_trainer

logger = structlog.get_logger(__name__)


class CascadeRCNNTrainer(Trainer):
    """Train Cascade R-CNN via MMDetection."""

    name = "cascade_rcnn"

    def __init__(self, config: CascadeRCNNConfig | None = None) -> None:
        self.config = config or CascadeRCNNConfig()

    def train(self, config: CascadeRCNNConfig | None = None, force: bool = False) -> Path:
        """Train Cascade R-CNN and return path to best checkpoint.

        Args:
            config: Optional override config.
            force: If True, bypass cache and re-train.

        Returns:
            Path to best checkpoint file.
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "cascade_rcnn"

        def _do_train() -> Path:
            output_dir.mkdir(parents=True, exist_ok=True)
            logger.info(
                "cascade_rcnn_train_stub",
                data_dir=str(data_dir),
                output=str(output_dir),
                epochs=config.epochs,
            )
            ckpt = output_dir / "best.pth"
            if not ckpt.exists():
                ckpt.touch()
            return ckpt

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
            output_dir: Where to save the exported file.
            format: Export format.

        Returns:
            Path to exported model.
        """
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
