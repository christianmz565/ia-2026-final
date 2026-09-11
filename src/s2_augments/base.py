"""Augmentation protocol, base classes, registry, and spatial priors.

Every augmentation method implements the ``Augmentor`` protocol and registers itself via
``register_augmentation()``.
"""

from __future__ import annotations

from pathlib import Path
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
        config: Any = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply augmentation to a single image and its bounding boxes."""
        ...

    def generate_dataset(
        self,
        input_dir: Path,
        output_dir: Path,
        config: Any = None,
    ) -> Path:
        """Generate full augmented dataset split under output_dir."""
        ...


CLASS_SPATIAL_PRIORS: dict[str, dict[str, Any]] = {
    "Knot_missing": {"cx_ranges": [(0.005, 0.08), (0.92, 0.995)], "cy_range": (0.05, 0.95)},
    "Marrow": {"cx_ranges": [(0.35, 0.65)], "cy_range": (0.05, 0.95)},
    "Crack": {"cx_ranges": [(0.35, 0.65)], "cy_range": (0.05, 0.95)},
    "Quartzity": {"cx_ranges": [(0.15, 0.85)], "cy_range": (0.05, 0.95)},
    "Live_Knot": {"cx_ranges": [(0.10, 0.90)], "cy_range": (0.05, 0.95)},
    "Dead_Knot": {"cx_ranges": [(0.10, 0.90)], "cy_range": (0.05, 0.95)},
    "resin": {"cx_ranges": [(0.05, 0.95)], "cy_range": (0.05, 0.95)},
    "knot_with_crack": {"cx_ranges": [(0.10, 0.90)], "cy_range": (0.05, 0.95)},
}


def sample_spatial_location(class_name: str, bbox_w: float, bbox_h: float) -> tuple[float, float]:
    """Sample valid (cx, cy) center coordinates adhering to empirical class spatial priors."""
    prior = CLASS_SPATIAL_PRIORS.get(
        class_name,
        {"cx_ranges": [(0.1, 0.9)], "cy_range": (0.05, 0.95)},
    )
    cx_ranges: list[tuple[float, float]] = prior["cx_ranges"]
    range_idx = int(np.random.randint(0, len(cx_ranges)))
    cx_min, cx_max = cx_ranges[range_idx]
    half_w = bbox_w / 2.0
    half_h = bbox_h / 2.0

    margin_w = half_w + 0.005
    margin_h = half_h + 0.005

    cx_low = max(margin_w, cx_min)
    cx_high = min(1.0 - margin_w, cx_max)
    if cx_low >= cx_high:
        valid_min = min(margin_w, 1.0 - margin_w)
        valid_max = max(margin_w, 1.0 - margin_w)
        cx = 0.5 if valid_min >= valid_max else float(np.random.uniform(valid_min, valid_max))
    else:
        cx = float(np.random.uniform(cx_low, cx_high))

    cy_min, cy_max = prior["cy_range"]
    cy_low = max(margin_h, cy_min)
    cy_high = min(1.0 - margin_h, cy_max)
    if cy_low >= cy_high:
        valid_min = min(margin_h, 1.0 - margin_h)
        valid_max = max(margin_h, 1.0 - margin_h)
        cy = 0.5 if valid_min >= valid_max else float(np.random.uniform(valid_min, valid_max))
    else:
        cy = float(np.random.uniform(cy_low, cy_high))

    cx = float(np.clip(cx, half_w, max(half_w, 1.0 - half_w)))
    cy = float(np.clip(cy, half_h, max(half_h, 1.0 - half_h)))

    return cx, cy


def check_overlap(box1: BBox, box2: BBox, iou_threshold: float = 0.05) -> bool:
    """Check if two normalized bboxes overlap beyond iou_threshold."""
    x1_1, y1_1 = box1.cx - box1.w / 2, box1.cy - box1.h / 2
    x2_1, y2_1 = box1.cx + box1.w / 2, box1.cy + box1.h / 2

    x1_2, y1_2 = box2.cx - box2.w / 2, box2.cy - box2.h / 2
    x2_2, y2_2 = box2.cx + box2.w / 2, box2.cy + box2.h / 2

    inter_x1 = max(x1_1, x1_2)
    inter_y1 = max(y1_1, y1_2)
    inter_x2 = min(x2_1, x2_2)
    inter_y2 = min(y2_1, y2_2)

    if inter_x2 <= inter_x1 or inter_y2 <= inter_y1:
        return False

    inter_area = (inter_x2 - inter_x1) * (inter_y2 - inter_y1)
    area1 = box1.w * box1.h
    area2 = box2.w * box2.h
    union_area = area1 + area2 - inter_area
    iou = inter_area / union_area if union_area > 0 else 0.0
    return iou > iou_threshold


class AlbumentationsAugmentor:
    """Base class for augmentations backed by Albumentations."""

    name: str = ""

    def _build_pipeline(self, config: BaseModel) -> A.Compose:
        """Build the albumentations pipeline from config."""
        raise NotImplementedError

    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: BaseModel | None = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply albumentations transform with automatic bbox handling."""
        if config is not None:
            self._pipeline = self._build_pipeline(config)

        yolo_boxes = []
        class_labels = []
        for b in bboxes:
            cx = max(0.0001, min(0.9999, b.cx))
            cy = max(0.0001, min(0.9999, b.cy))
            w = max(0.0001, min(0.9999, b.w))
            h = max(0.0001, min(0.9999, b.h))

            x1 = max(0.0, cx - w / 2.0)
            y1 = max(0.0, cy - h / 2.0)
            x2 = min(1.0, cx + w / 2.0)
            y2 = min(1.0, cy + h / 2.0)

            clean_w = x2 - x1
            clean_h = y2 - y1
            clean_cx = (x1 + x2) / 2.0
            clean_cy = (y1 + y2) / 2.0

            if clean_w > 0 and clean_h > 0:
                yolo_boxes.append([clean_cx, clean_cy, clean_w, clean_h])
                class_labels.append(b.class_id)

        if not yolo_boxes:
            return image, bboxes

        result = self._pipeline(image=image, bboxes=yolo_boxes, class_labels=class_labels)

        new_bboxes = [
            BBox(class_id=cls, cx=cx, cy=cy, w=w, h=h)
            for cls, (cx, cy, w, h) in zip(result["class_labels"], result["bboxes"], strict=False)
        ]
        return result["image"], new_bboxes


_AUGMENTATION_REGISTRY: dict[str, type[Augmentor]] = {}


def register_augmentation(name: str, cls: type[Augmentor]) -> None:
    """Register an augmentation class by name."""
    _AUGMENTATION_REGISTRY[name] = cls


def get_augmentation(name: str) -> Augmentor:
    """Instantiate and return an augmentation by registered name."""
    if name not in _AUGMENTATION_REGISTRY:
        available = ", ".join(sorted(_AUGMENTATION_REGISTRY))
        raise KeyError(f"Unknown augmentation '{name}'. Available: {available}")
    return _AUGMENTATION_REGISTRY[name]()


def list_augmentations() -> list[str]:
    """Return sorted list of registered augmentation names."""
    return sorted(_AUGMENTATION_REGISTRY)
