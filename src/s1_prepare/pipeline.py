"""s1_prepare pipeline — runs download -> explore -> convert -> split.

Standalone usage:
    uv run python -m src.s1_prepare.pipeline [--log-level INFO]
"""

from __future__ import annotations

import structlog

from src.config import S1Config
from src.s1_prepare.convert import convert_yolo_to_coco
from src.s1_prepare.download import download_dataset
from src.s1_prepare.explore import explore_dataset
from src.s1_prepare.split import split_dataset

logger = structlog.get_logger(__name__)

STEPS = ["download", "explore", "convert", "split"]


def run_pipeline(config: S1Config | None = None) -> None:
    """Execute the full s1_prepare pipeline.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S1Config()
    logger.info("s1_pipeline_start")

    logger.info("s1_step", step="download")
    download_dataset(config.download)

    logger.info("s1_step", step="explore")
    explore_dataset()

    logger.info("s1_step", step="convert")
    convert_yolo_to_coco()

    logger.info("s1_step", step="split")
    split_dataset(config.split)

    logger.info("s1_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S1Config,
        run_fn=run_pipeline,
        description="s1_prepare pipeline",
        skip_fields=["download", "split"],
    )
