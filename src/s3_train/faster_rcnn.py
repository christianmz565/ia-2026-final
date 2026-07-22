"""Faster R-CNN training wrapper (MMDetection).

Standalone usage:
    uv run python -m src.s3_train.faster_rcnn [--data-dir PATH] [--epochs 12]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.config import FasterRCNNConfig
from src.s3_train.base import register_trainer

logger = structlog.get_logger(__name__)


class FasterRCNNTrainer:
    """Train Faster R-CNN via MMDetection."""

    name = "faster_rcnn"

    def __init__(self, config: FasterRCNNConfig | None = None) -> None:
        self.config = config or FasterRCNNConfig()

    def train(self, config: FasterRCNNConfig | None = None) -> Path:
        """Train Faster R-CNN and return path to best checkpoint.

        Args:
            config: Optional override config.

        Returns:
            Path to best checkpoint file.
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else Path("data")
        output_dir = Path(config.output_dir) if config.output_dir else Path("output/faster_rcnn")
        # TODO: implement using mmdet/apis
        logger.info(
            "faster_rcnn_train_stub",
            data_dir=str(data_dir),
            output=str(output_dir),
            epochs=config.epochs,
        )
        return output_dir / "best.pth"

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export Faster R-CNN model.

        Args:
            checkpoint: Path to ``.pth`` weights.
            output_dir: Where to save the exported file.
            format: Export format.

        Returns:
            Path to exported model.
        """
        # TODO: implement using mmdet/apis or torch.export
        logger.info("faster_rcnn_export_stub", checkpoint=str(checkpoint), format=format)
        return output_dir / f"model.{format}"


register_trainer("faster_rcnn", FasterRCNNTrainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=FasterRCNNConfig,
        run_fn=lambda cfg: FasterRCNNTrainer(cfg).train(cfg),
        description="Train Faster R-CNN",
        required_fields=["data_dir"],
    )
