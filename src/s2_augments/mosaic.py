"""Mosaic augmentation: combine 4 images into a single training sample.

Standalone usage:
    uv run python -m src.s2_augments.mosaic [--log-level INFO]
"""

from __future__ import annotations

import numpy as np
import structlog

from src.config import MosaicConfig
from src.s2_augments.base import register_augmentation
from src.utils import BBox

logger = structlog.get_logger(__name__)


class MosaicAugmentor:
    """Create mosaic composites from 4 random images with adjusted bounding boxes."""

    name = "mosaic"

    def __init__(self, config: MosaicConfig | None = None) -> None:
        self.config = config or MosaicConfig()

    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: MosaicConfig | None = None,
        *,
        other_images: list[np.ndarray] | None = None,
        other_bboxes: list[list[BBox]] | None = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply mosaic augmentation.

        This method requires ``other_images`` and ``other_bboxes`` to form the
        4-image mosaic.  When called standalone, placeholder logic should supply
        these from the dataset.

        Args:
            image: Center image (H, W, 3) BGR.
            bboxes: Bounding boxes for the center image.
            config: Optional override config.
            other_images: Exactly 3 additional images for the mosaic.
            other_bboxes: Bounding boxes for those 3 images.

        Returns:
            Tuple of (mosaic_image, combined_bboxes).
        """
        if config is not None:
            self.config = config

        if not other_images or len(other_images) < 3:
            logger.warning("mosaic_insufficient_images", provided=len(other_images or []))
            return image, bboxes

        # Placeholder: actual mosaic stitching logic goes here
        pass

    def _place_image(
        self,
        canvas: np.ndarray,
        img: np.ndarray,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> np.ndarray:
        """Resize and place an image into a canvas region (placeholder)."""
        pass

    def _offset_bboxes(
        self,
        bboxes: list[BBox],
        x_offset: float,
        y_offset: float,
        scale: float,
    ) -> list[BBox]:
        """Offset and scale bounding boxes for a mosaic quadrant (placeholder)."""
        pass


register_augmentation("mosaic", MosaicAugmentor)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=MosaicConfig,
        run_fn=lambda cfg: logger.info("mosaic_config", **cfg.model_dump()),
        description="Apply mosaic augmentation",
    )
