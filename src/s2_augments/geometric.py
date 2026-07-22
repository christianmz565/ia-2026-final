"""Geometric augmentations: flip, rotate, scale, crop.

Standalone usage:
    uv run python -m src.s2_augments.geometric [--horizontal-flip-prob 0.5] [--rotation-limit 15]
"""

from __future__ import annotations

import albumentations as A
import structlog
from pydantic import BaseModel

from src.s2_augments.base import _BBOX_PARAMS, AlbumentationsAugmentor, register_augmentation

logger = structlog.get_logger(__name__)


class GeometricAugmentor(AlbumentationsAugmentor):
    """Apply geometric transformations while preserving bounding boxes."""

    name = "geometric"

    def __init__(self, config: BaseModel | None = None) -> None:
        config = config or self._default_config()
        self._pipeline = self._build_pipeline(config)

    @staticmethod
    def _default_config() -> BaseModel:
        from src.config import GeometricConfig

        return GeometricConfig()

    def _build_pipeline(self, config: BaseModel) -> A.Compose:
        """Build the albumentations pipeline from config."""
        from src.config import GeometricConfig

        assert isinstance(config, GeometricConfig)
        return A.Compose(
            [
                A.HorizontalFlip(p=config.horizontal_flip_prob),
                A.VerticalFlip(p=config.vertical_flip_prob),
                A.Rotate(limit=config.rotation_limit, p=0.5),
                A.RandomScale(scale_limit=config.scale_limit, p=0.5),
            ],
            bbox_params=_BBOX_PARAMS,
        )


register_augmentation("geometric", GeometricAugmentor)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=GeometricAugmentor._default_config().__class__,
        run_fn=lambda cfg: logger.info("geometric_augmentation_config", **cfg.model_dump()),
        description="Apply geometric augmentations",
    )
