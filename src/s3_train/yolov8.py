"""YOLOv8 training wrapper (Ultralytics).

Standalone usage:
    uv run python -m src.s3_train.yolov8 [--data-dir PATH] [--epochs 100]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.config import YOLOv8Config
from src.s3_train.base import register_trainer

logger = structlog.get_logger(__name__)


class YOLOv8Trainer:
    """Train YOLOv8 via the Ultralytics Python API."""

    name = "yolov8"

    def __init__(self, config: YOLOv8Config | None = None) -> None:
        self.config = config or YOLOv8Config()

    def train(self, config: YOLOv8Config | None = None) -> Path:
        """Train YOLOv8 and return path to best weights.

        Args:
            config: Optional override config.

        Returns:
            Path to ``best.pt`` weights.
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else Path("data")
        output_dir = Path(config.output_dir) if config.output_dir else Path("output/yolov8")
        # TODO: implement using ultralytics.YOLO
        logger.info("yolov8_train_stub", data_dir=str(data_dir), output=str(output_dir), epochs=config.epochs)
        return output_dir / "best.pt"

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export YOLOv8 model.

        Args:
            checkpoint: Path to ``.pt`` weights.
            output_dir: Where to save the exported file.
            format: Export format.

        Returns:
            Path to exported model.
        """
        # TODO: implement using ultralytics.YOLO.export()
        logger.info("yolov8_export_stub", checkpoint=str(checkpoint), format=format)
        return output_dir / f"model.{format}"


register_trainer("yolov8", YOLOv8Trainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=YOLOv8Config,
        run_fn=lambda cfg: YOLOv8Trainer(cfg).train(cfg),
        description="Train YOLOv8",
        required_fields=["data_dir"],
    )
