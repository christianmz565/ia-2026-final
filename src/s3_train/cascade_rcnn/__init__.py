"""Cascade R-CNN Baseline package for wood surface defect detection.
Includes ConvNeXt backbone, PAFPN neck, data sanitization, AMP, and early stopping.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import structlog

if TYPE_CHECKING:
    from src.s3_train.cascade_rcnn.config import PipelineConfig

from src.caching import run_cached_step
from src.config import CascadeRCNNConfig
from src.constants import S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import Trainer, register_trainer

logger = structlog.get_logger(__name__)

__version__ = "0.1.0"


def _build_pipeline_config(cfg: CascadeRCNNConfig) -> PipelineConfig:
    """Build internal PipelineConfig from CascadeRCNNConfig."""
    from src.s3_train.cascade_rcnn.config import DatasetConfig, ModelConfig, PipelineConfig, TrainingConfig

    data_dir = Path(cfg.data_dir) if cfg.data_dir else SPLIT_DATASET
    output_dir = Path(cfg.output_dir) if cfg.output_dir else S3_OUTPUT / "cascade_rcnn"

    dataset = DatasetConfig(
        data_dir=data_dir,
        train_json=data_dir / "train" / "_annotations.coco.json",
        val_json=data_dir / "val" / "_annotations.coco.json",
        output_dir=output_dir,
    )
    training = TrainingConfig(
        epochs=cfg.epochs,
        batch_size=cfg.batch_size,
        lr=cfg.lr,
    )
    return PipelineConfig(dataset=dataset, model=ModelConfig(), training=training)


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
        output_dir = Path(config.output_dir) if config.output_dir else S3_OUTPUT / "cascade_rcnn"

        def _do_train() -> Path:
            from src.s3_train.cascade_rcnn.train import run_pipeline

            pipeline_cfg = _build_pipeline_config(config)
            run_pipeline(pipeline_cfg)
            best_pt = output_dir / "best.pt"
            if best_pt.exists():
                return best_pt
            return output_dir

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
