"""s3_train pipeline — trains all configured models on all augmented datasets.

Standalone usage:
    uv run python -m src.s3_train.pipeline [--models yolov8,faster_rcnn,rt_detr]
"""

from __future__ import annotations

import structlog

from src.config import S3Config
from src.s3_train import (
    faster_rcnn,  # noqa: F401 — triggers registration
    rt_detr,  # noqa: F401 — triggers registration
    yolov8,  # noqa: F401 — triggers registration
)
from src.s3_train.base import get_trainer, list_trainers

logger = structlog.get_logger(__name__)


def run_pipeline(config: S3Config | None = None) -> None:
    """Train each configured model on each augmented dataset split.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S3Config()
    models = config.models

    logger.info("s3_pipeline_start", models=models, available=list_trainers())

    for model_name in models:
        logger.info("s3_step", model=model_name)
        try:
            _trainer = get_trainer(model_name)
            # TODO: iterate over augmented datasets from s2, call _trainer.train()
            logger.info("s3_step_complete", model=model_name)
        except KeyError:
            logger.error("s3_unknown_model", model=model_name)

    logger.info("s3_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S3Config,
        run_fn=run_pipeline,
        description="s3_train pipeline",
        skip_fields=["yolov8", "faster_rcnn", "rt_detr"],
    )
