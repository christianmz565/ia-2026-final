"""s2_augments pipeline — applies all enabled augmentation methods.

Standalone usage:
    uv run python -m src.s2_augments.pipeline [--methods geometric,photometric]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.caching import run_cached_step
from src.config import S2Config
from src.constants import AUGMENTED_DIR
from src.s2_augments.base import get_augmentation, list_augmentations

logger = structlog.get_logger(__name__)

STEPS = ["geometric", "photometric", "mosaic", "mixup"]


def run_pipeline(config: S2Config | None = None) -> None:
    """Execute augmentation pipeline for all configured methods.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S2Config()
    methods = config.augment.methods

    logger.info("s2_pipeline_start", methods=methods, available=list_augmentations())

    for method_name in methods:
        target_dir = AUGMENTED_DIR / method_name

        def _run_method(name: str = method_name, out_dir: Path = target_dir) -> Path:
            _augmentor = get_augmentation(name)
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / ".augmented").touch()
            logger.info("s2_step_complete", method=name)
            return out_dir

        run_cached_step(
            step_name=f"augment_{method_name}",
            target_path=target_dir,
            fn=_run_method,
        )

    logger.info("s2_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S2Config,
        run_fn=run_pipeline,
        description="s2_augments pipeline",
        skip_fields=["augment"],
    )
