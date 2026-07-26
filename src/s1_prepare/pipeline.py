"""s1_prepare pipeline — runs download -> preprocess -> explore -> split -> convert_coco.

Standalone usage:
    uv run python -m src.s1_prepare.pipeline [--log-level INFO]
"""

from __future__ import annotations

import structlog

from src.caching import run_cached_step
from src.config import S1Config
from src.constants import PROCESSED_DATASET, RAW_DATASET, S1_OUTPUT, SPLIT_DATASET
from src.s1_prepare.convert_coco import convert_coco_dataset
from src.s1_prepare.download import download_dataset
from src.s1_prepare.explore import explore_dataset
from src.s1_prepare.preprocess import preprocess_dataset
from src.s1_prepare.split import split_dataset

logger = structlog.get_logger(__name__)

STEPS = ["download", "preprocess", "explore", "split", "convert_coco"]


def run_pipeline(config: S1Config | None = None) -> None:
    """Execute the full s1_prepare pipeline.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S1Config()
    logger.info("s1_pipeline_start")

    run_cached_step(
        step_name="s1_download",
        target_path=RAW_DATASET,
        fn=lambda: download_dataset(config.download),
        force=config.download.force_redownload,
    )

    run_cached_step(
        step_name="s1_preprocess",
        target_path=PROCESSED_DATASET,
        fn=lambda: preprocess_dataset(config.preprocess),
    )

    run_cached_step(
        step_name="s1_explore",
        target_path=S1_OUTPUT / "explore_stats.json",
        fn=lambda: explore_dataset(),
    )

    run_cached_step(
        step_name="s1_split",
        target_path=SPLIT_DATASET,
        fn=lambda: split_dataset(config.split),
    )

    run_cached_step(
        step_name="s1_convert_coco",
        target_path=SPLIT_DATASET / "train" / "_annotations.coco.json",
        fn=lambda: convert_coco_dataset(),
    )

    logger.info("s1_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S1Config,
        run_fn=run_pipeline,
        description="s1_prepare pipeline",
        skip_fields=[],
    )

