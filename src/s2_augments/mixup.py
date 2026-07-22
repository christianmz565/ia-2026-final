"""MixUp augmentation: blend two images and their annotations.

Standalone usage:
    uv run python -m src.s2_augments.mixup [--log-level INFO]
"""

from __future__ import annotations

import numpy as np
import structlog

from src.config import MixupConfig
from src.s2_augments.base import register_augmentation
from src.utils import BBox

logger = structlog.get_logger(__name__)


class MixupAugmentor:
    """Blend two images with their bounding boxes using MixUp."""

    name = "mixup"

    def __init__(self, config: MixupConfig | None = None) -> None:
        self.config = config or MixupConfig()

    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: MixupConfig | None = None,
        *,
        other_image: np.ndarray | None = None,
        other_bboxes: list[BBox] | None = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply MixUp augmentation.

        Args:
            image: First image (H, W, 3) BGR.
            bboxes: Bounding boxes for the first image.
            config: Optional override config.
            other_image: Second image to blend with.
            other_bboxes: Bounding boxes for the second image.

        Returns:
            Tuple of (blended_image, merged_bboxes).
        """
        if config is not None:
            self.config = config

        if other_image is None or other_bboxes is None:
            logger.warning("mixup_missing_pair")
            return image, bboxes

        # Placeholder: actual MixUp blending logic goes here
        pass


register_augmentation("mixup", MixupAugmentor)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=MixupConfig,
        run_fn=lambda cfg: logger.info("mixup_config", **cfg.model_dump()),
        description="Apply MixUp augmentation",
    )
