"""Augmentation protocol, base classes, and registry.

Every augmentation module must implement the ``Augmentor`` protocol and call
``register_augmentation()`` to make itself discoverable by the pipeline.
``AlbumentationsAugmentor`` provides a shared implementation for augmentations
that use albumentations as their backend (geometric, photometric, etc.).
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

import albumentations as A
import numpy as np
from pydantic import BaseModel

from src.utils import BBox


@runtime_checkable
class Augmentor(Protocol):
    """Interface that every augmentation method must implement."""

    name: str

    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: Any,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply augmentation to an image and its bounding boxes.

        Args:
            image: Input image (H, W, 3) in BGR format.
            bboxes: List of bounding boxes associated with the image.
            config: Method-specific configuration object.

        Returns:
            Tuple of (augmented_image, transformed_bboxes).
        """
        ...


# ── Albumentations base ─────────────────────────────────────────────────────

_BBOX_PARAMS = A.BboxParams(
    format="yolo",
    label_fields=["class_labels"],
    min_area=0.0,
    min_visibility=0.3,
)


class AlbumentationsAugmentor:
    """Base class for augmentations backed by albumentations.

    Subclasses only need to implement ``_build_pipeline(config)`` which
    returns an ``A.Compose`` instance.  The shared ``apply()`` method
    handles bbox extraction, transform invocation, and BBox reconstruction.
    """

    name: str = ""

    def _build_pipeline(self, config: BaseModel) -> A.Compose:
        """Build the albumentations pipeline from config. Must be overridden."""
        raise NotImplementedError

    def _apply_config(self, config: BaseModel | None) -> BaseModel:
        """Return the effective config, rebuilding the pipeline if config changes."""
        if config is not None:
            self._pipeline = self._build_pipeline(config)
        return config  # type: ignore[return-value]

    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: BaseModel | None = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply albumentations transform with automatic bbox handling.

        Args:
            image: Input image (H, W, 3) BGR.
            bboxes: Original bounding boxes.
            config: Optional config override. If provided, rebuilds the pipeline.

        Returns:
            Tuple of (augmented_image, transformed_bboxes).
        """
        if not hasattr(self, "_pipeline"):
            raise RuntimeError(f"{self.__class__.__name__}._build_pipeline() was never called")

        self._apply_config(config)

        yolo_boxes = [[b.cx, b.cy, b.w, b.h] for b in bboxes]
        class_labels = [b.class_id for b in bboxes]

        result = self._pipeline(image=image, bboxes=yolo_boxes, class_labels=class_labels)

        new_bboxes = [
            BBox(class_id=cls, cx=cx, cy=cy, w=w, h=h)
            for cls, (cx, cy, w, h) in zip(result["class_labels"], result["bboxes"], strict=False)
        ]
        return result["image"], new_bboxes


# ── Global registry ──────────────────────────────────────────────────────────

_AUGMENTATION_REGISTRY: dict[str, type[Augmentor]] = {}


def register_augmentation(name: str, cls: type[Augmentor]) -> None:
    """Register an augmentation class by name.

    Args:
        name: String key used in pipeline config (e.g. ``"geometric"``).
        cls: The Augmentor implementation class.
    """
    _AUGMENTATION_REGISTRY[name] = cls


def get_augmentation(name: str) -> Augmentor:
    """Instantiate and return an augmentation by registered name.

    Args:
        name: Key used during registration.

    Raises:
        KeyError: If name is not registered.
    """
    if name not in _AUGMENTATION_REGISTRY:
        available = ", ".join(sorted(_AUGMENTATION_REGISTRY))
        raise KeyError(f"Unknown augmentation '{name}'. Available: {available}")
    return _AUGMENTATION_REGISTRY[name]()


def list_augmentations() -> list[str]:
    """Return sorted list of registered augmentation names."""
    return sorted(_AUGMENTATION_REGISTRY)
