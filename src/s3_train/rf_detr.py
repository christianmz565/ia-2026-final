"""RF-DETR training wrapper.

Standalone usage:
    uv run python -m src.s3_train.rf_detr [--data-dir PATH] [--epochs 100]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.caching import run_cached_step
from src.config import RFDETRConfig
from src.constants import S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import register_trainer

logger = structlog.get_logger(__name__)


class RFDETRTrainer:
    """Train RF-DETR model."""

    name = "rf_detr"

    def __init__(self, config: RFDETRConfig | None = None) -> None:
        self.config = config or RFDETRConfig()

    def train(self, config: RFDETRConfig | None = None, force: bool = False) -> Path:
        """Train RF-DETR and return path to best weights.

        Args:
            config: Optional override config.
            force: If True, bypass cache and re-train.

        Returns:
            Path to ``best.pt`` weights.
        """
        config = config or self.config
        data_dir = Path(config.data_dir) if config.data_dir else SPLIT_DATASET
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "rf_detr"

        def _do_train() -> Path:
            output_dir.mkdir(parents=True, exist_ok=True)
            logger.info(
                "rf_detr_train_stub",
                data_dir=str(data_dir),
                output=str(output_dir),
                epochs=config.epochs,
            )
            weights = output_dir / "best.pt"
            if not weights.exists():
                weights.touch()
            return weights

        return run_cached_step(
            step_name="train_rf_detr",
            target_path=output_dir,
            fn=_do_train,
            force=force,
        )

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export RF-DETR model.

        Args:
            checkpoint: Path to ``.pt`` weights.
            output_dir: Where to save the exported file.
            format: Export format.

        Returns:
            Path to exported model.
        """
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
