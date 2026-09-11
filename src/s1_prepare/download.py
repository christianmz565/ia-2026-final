"""Download the wood-surface-defects dataset from Kaggle.

Standalone usage:
    uv run python -m src.s1_prepare.download [--kaggle-dataset SLUG] [--force-redownload]
"""

from __future__ import annotations

import shutil
from pathlib import Path

import kagglehub
import structlog

from src.caching import config_fingerprint, run_cached_step
from src.config import DownloadConfig
from src.constants import RAW_DATASET

logger = structlog.get_logger(__name__)


def download_dataset(config: DownloadConfig | None = None) -> Path:
    """Download dataset from Kaggle and place it in the raw partials directory.

    Args:
        config: Download configuration. Uses defaults when ``None``.

    Returns:
        Path to the downloaded dataset directory.
    """
    config = config or DownloadConfig()
    target = Path(RAW_DATASET)

    def _download() -> Path:
        if target.exists():
            logger.info("force_redownload", path=str(target))
            shutil.rmtree(target)

        target.parent.mkdir(parents=True, exist_ok=True)

        logger.info("downloading_dataset", kaggle_slug=config.kaggle_dataset)
        downloaded_dir = kagglehub.dataset_download(config.kaggle_dataset)
        shutil.copytree(downloaded_dir, target)
        logger.info("download_complete", path=str(target))
        return target

    return run_cached_step(
        step_name="download",
        target_path=target,
        fn=_download,
        force=config.force_redownload,
        fingerprint=config_fingerprint(config),
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=DownloadConfig,
        run_fn=lambda cfg: download_dataset(cfg),
        description="Download wood-surface-defects dataset",
    )
