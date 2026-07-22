"""RT-DETR training wrapper (Ultralytics).

Standalone usage:
    uv run python -m src.s3_train.rt_detr [--data-dir PATH] [--epochs 100]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.config import RTDETRConfig
from src.s3_train.base import register_trainer

logger = structlog.get_logger(__name__)


class RTDETRTrainer:
    """Train RT-DETR via the Ultralytics Python API."""

    name = "rt_detr"

    def __init__(self, config: RTDETRConfig | None = None) -> None:
        self.config = config or RTDETRConfig()

    def train(self, config: RTDETRConfig | None = None) -> Path:
        """Train RT-DETR and return path to best weights.

        Args:
            config: Optional override config.

        Returns:
            Path to ``best.pt`` weights.
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else Path("data")
        output_dir = Path(config.output_dir) if config.output_dir else Path("output/rt_detr")
        # TODO: implement using ultralytics RTDETR
        logger.info(
            "rt_detr_train_stub",
            data_dir=str(data_dir),
            output=str(output_dir),
            epochs=config.epochs,
        )
        return output_dir / "best.pt"

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export RT-DETR model.

        Args:
            checkpoint: Path to ``.pt`` weights.
            output_dir: Where to save the exported file.
            format: Export format.

        Returns:
            Path to exported model.
        """
        # TODO: implement using ultralytics RTDETR.export()
        logger.info("rt_detr_export_stub", checkpoint=str(checkpoint), format=format)
        return output_dir / f"model.{format}"


register_trainer("rt_detr", RTDETRTrainer)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=RTDETRConfig,
        run_fn=lambda cfg: RTDETRTrainer(cfg).train(cfg),
        description="Train RT-DETR",
        required_fields=["data_dir"],
    )
