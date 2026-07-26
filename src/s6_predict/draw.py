"""Draw bounding boxes and labels on images for visualization."""

from __future__ import annotations

import cv2
import numpy as np

from src.constants import CLASS_NAMES

# One distinct color per class (BGR format for OpenCV)
_COLORS = [
    (255, 100, 0),    # Quartzity - orange
    (0, 200, 255),    # Live_Knot - cyan
    (0, 150, 0),      # Marrow - green
    (200, 0, 200),    # resin - purple
    (0, 0, 255),      # Dead_Knot - red
    (128, 0, 128),    # knot_with_crack - dark purple
    (255, 165, 0),    # Knot_missing - dark orange
    (0, 255, 255),    # Crack - yellow
]

# Fallback color for unknown classes
_DEFAULT_COLOR = (255, 255, 255)


def draw_detections(
    image: np.ndarray,
    detections: list[dict],
    *,
    conf_threshold: float = 0.0,
    thickness: int = 2,
    font_scale: float = 0.6,
) -> np.ndarray:
    """Draw bounding boxes and labels on an image.

    Args:
        image: Input image (BGR).
        detections: List of dicts with keys: bbox [x1, y1, w, h], category_id, score.
        conf_threshold: Minimum confidence to draw a detection.
        thickness: Line thickness for bounding boxes.
        font_scale: Font scale for label text.

    Returns:
        Image with drawn detections.
    """
    vis = image.copy()
    h, w = vis.shape[:2]

    for det in detections:
        score = det.get("score", 0.0)
        if score < conf_threshold:
            continue

        cat_id = det.get("category_id", 0)
        class_name = CLASS_NAMES[cat_id - 1] if 1 <= cat_id <= len(CLASS_NAMES) else f"class_{cat_id}"
        color = _COLORS[cat_id - 1] if 1 <= cat_id <= len(_COLORS) else _DEFAULT_COLOR

        bbox = det.get("bbox", [])
        if len(bbox) < 4:
            continue
        x1, y1, bw, bh = bbox
        x2, y2 = x1 + bw, y1 + bh

        # Clamp to image bounds
        x1, y1 = max(0, int(x1)), max(0, int(y1))
        x2, y2 = min(w - 1, int(x2)), min(h - 1, int(y2))

        cv2.rectangle(vis, (x1, y1), (x2, y2), color, thickness)

        label = f"{class_name} {score:.2f}"
        (tw, th), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 1)

        # Label background
        label_y = max(y1 - 5, th + 5)
        cv2.rectangle(vis, (x1, label_y - th - 4), (x1 + tw + 4, label_y + 4), color, -1)
        cv2.putText(vis, label, (x1 + 2, label_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), 2)

    return vis
