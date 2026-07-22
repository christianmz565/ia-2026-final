"""s2_augments pipeline — applies all enabled augmentation methods.

Standalone usage:
    uv run python -m src.s2_augments.pipeline [--methods geometric,photometric]
"""

from __future__ import annotations

import structlog

from src.config import S2Config
from src.s2_augments import (
    geometric,  # noqa: F401 — triggers registration
    mixup,  # noqa: F401 — triggers registration
    mosaic,  # noqa: F401 — triggers registration
    photometric,  # noqa: F401 — triggers registration
)
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
        logger.info("s2_step", method=method_name)
        try:
            _augmentor = get_augmentation(method_name)
            # TODO: iterate over split dataset images, apply _augmentor.apply(), write results
            logger.info("s2_step_complete", method=method_name)
        except KeyError:
            logger.error("s2_unknown_method", method=method_name)

    logger.info("s2_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S2Config,
        run_fn=run_pipeline,
        description="s2_augments pipeline",
        skip_fields=["augment"],
    )
