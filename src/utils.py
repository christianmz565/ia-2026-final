"""Shared utilities: bounding-box helpers, image I/O, path operations."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np

# ── Bounding Box ─────────────────────────────────────────────────────────────


@dataclass
class BBox:
    """Normalized bounding box in YOLO format (center_x, center_y, w, h).

    All coordinates are relative to image dimensions (0.0 – 1.0).
    """

    class_id: int
    cx: float
    cy: float
    w: float
    h: float
    confidence: float | None = None

    # ── conversions ──────────────────────────────────────────────────────

    def to_xyxy(self, img_w: int, img_h: int) -> tuple[int, int, int, int]:
        """Convert to absolute (x1, y1, x2, y2) pixel coordinates."""
        abs_cx = self.cx * img_w
        abs_cy = self.cy * img_h
        abs_w = self.w * img_w
        abs_h = self.h * img_h
        x1 = int(abs_cx - abs_w / 2)
        y1 = int(abs_cy - abs_h / 2)
        x2 = int(abs_cx + abs_w / 2)
        y2 = int(abs_cy + abs_h / 2)
        return (max(x1, 0), max(y1, 0), min(x2, img_w), min(y2, img_h))

    @classmethod
    def from_xyxy(
        cls,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        img_w: int,
        img_h: int,
        class_id: int = 0,
    ) -> BBox:
        """Create from absolute pixel (x1, y1, x2, y2)."""
        cx = ((x1 + x2) / 2) / img_w
        cy = ((y1 + y2) / 2) / img_h
        w = (x2 - x1) / img_w
        h = (y2 - y1) / img_h
        return cls(class_id=class_id, cx=cx, cy=cy, w=w, h=h)

    def area(self) -> float:
        """Return normalized area (fraction of total image)."""
        return self.w * self.h

    def aspect_ratio(self) -> float:
        """Return width / height ratio."""
        return self.w / self.h if self.h > 0 else 0.0


# ── I/O helpers ──────────────────────────────────────────────────────────────


def read_image(path: Path | str, *, color: bool = True) -> np.ndarray:
    """Read an image from disk.

    Args:
        path: File path.
        color: If True return BGR, else grayscale.

    Returns:
        numpy array (H, W, 3) or (H, W).
    """
    flag = cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE
    img = cv2.imread(str(path), flag)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {path}")
    return img


def write_image(path: Path | str, image: np.ndarray) -> None:
    """Write an image to disk, creating parent directories."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), image)


# ── YOLO annotation I/O ─────────────────────────────────────────────────────


def read_yolo_labels(label_path: Path | str) -> list[BBox]:
    """Parse a YOLO-format .txt label file."""
    bboxes: list[BBox] = []
    path = Path(label_path)
    if not path.exists():
        return bboxes
    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            class_id = int(parts[0])
            cx, cy, w, h = map(float, parts[1:5])
            conf = float(parts[5]) if len(parts) > 5 else None
            bboxes.append(BBox(class_id=class_id, cx=cx, cy=cy, w=w, h=h, confidence=conf))
    return bboxes


def write_yolo_labels(label_path: Path | str, bboxes: list[BBox]) -> None:
    """Write bboxes to a YOLO-format .txt label file."""
    Path(label_path).parent.mkdir(parents=True, exist_ok=True)
    with open(label_path, "w") as f:
        for b in bboxes:
            line = f"{b.class_id} {b.cx:.6f} {b.cy:.6f} {b.w:.6f} {b.h:.6f}"
            if b.confidence is not None:
                line += f" {b.confidence:.6f}"
            f.write(line + "\n")


# ── Path helpers ─────────────────────────────────────────────────────────────


def ensure_dir(path: Path | str) -> Path:
    """Create directory (and parents) if it doesn't exist, return Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def resolve_labels_dir(input_dir: Path) -> Path:
    """Return the labels directory if it exists, falling back to input_dir."""
    labels_dir = input_dir / "labels"
    if labels_dir.exists():
        return labels_dir
    # Check for Kaggle or nested Bounding Boxes directory
    bbox_dirs = list(input_dir.rglob("*Bounding Boxes*")) + list(input_dir.rglob("*labels*"))
    for d in bbox_dirs:
        if d.is_dir():
            return d
    return input_dir


def find_image_label_pairs(input_dir: Path) -> list[tuple[Path, Path]]:
    """Find all (image_path, label_path) pairs in a dataset.

    Handles structured (images/, labels/), flat, or Kaggle-extracted layouts.

    Args:
        input_dir: Root dataset directory.

    Returns:
        Sorted list of ``(image_path, label_path)`` tuples.
    """
    images_dir = input_dir / "images"
    if images_dir.exists():
        image_files = sorted(images_dir.rglob("*.jpg")) + sorted(images_dir.rglob("*.png"))
    else:
        image_files = sorted(input_dir.rglob("*.jpg")) + sorted(input_dir.rglob("*.png"))

    txt_files = list(input_dir.rglob("*.txt"))
    label_map: dict[str, Path] = {f.stem: f for f in txt_files}
    labels_dir = resolve_labels_dir(input_dir)

    pairs: list[tuple[Path, Path]] = []
    for img_path in image_files:
        if img_path.stem in label_map:
            label_path = label_map[img_path.stem]
        else:
            label_path = labels_dir / img_path.with_suffix(".txt").name
        pairs.append((img_path, label_path))

    return pairs
