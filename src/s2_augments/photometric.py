"""Photometric augmentations: color jitter, brightness, contrast, noise.

Standalone usage:
    uv run python -m src.s2_augments.photometric [--brightness-limit 0.2] [--contrast-limit 0.2]
"""

from __future__ import annotations

import albumentations as A
import structlog
from pydantic import BaseModel

from src.s2_augments.base import _BBOX_PARAMS, AlbumentationsAugmentor, register_augmentation

logger = structlog.get_logger(__name__)


class PhotometricAugmentor(AlbumentationsAugmentor):
    """Apply color-space transformations that do not alter bounding box geometry."""

    name = "photometric"

    def __init__(self, config: BaseModel | None = None) -> None:
        config = config or self._default_config()
        self._pipeline = self._build_pipeline(config)

    @staticmethod
    def _default_config() -> BaseModel:
        from src.config import PhotometricConfig

        return PhotometricConfig()

    def _build_pipeline(self, config: BaseModel) -> A.Compose:
        """Build the albumentations pipeline from config."""
        from src.config import PhotometricConfig

        assert isinstance(config, PhotometricConfig)
        return A.Compose(
            [
                A.ColorJitter(
                    brightness=config.brightness_limit,
                    contrast=config.contrast_limit,
                    saturation=config.saturation_limit,
                    hue=config.hue_shift_limit / 100.0,
                    p=0.8,
                ),
                A.MotionBlur(blur_limit=7, p=config.motion_blur_prob),
                A.GaussNoise(var_limit=(10.0, 50.0), p=config.gaussian_noise_prob),
            ],
            bbox_params=_BBOX_PARAMS,
        )


register_augmentation("photometric", PhotometricAugmentor)


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=PhotometricAugmentor._default_config().__class__,
        run_fn=lambda cfg: logger.info("photometric_augmentation_config", **cfg.model_dump()),
        description="Apply photometric augmentations",
    )
