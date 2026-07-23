"""Shared utility functions for bounding-box and image-based data augmentation routines."""

from __future__ import annotations

from pathlib import Path


def load_yolo_labels(label_path: Path) -> list[tuple[int, float, float, float, float]]:
    """Read YOLO format annotations (class_id, x_center, y_center, width, height)."""
    if not label_path.exists():
        return []
    labels = []
    with open(label_path, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 5:
                cls_id = int(parts[0])
                coords = [float(x) for x in parts[1:5]]
                labels.append((cls_id, coords[0], coords[1], coords[2], coords[3]))
    return labels


def save_yolo_labels(label_path: Path, labels: list[tuple[int, float, float, float, float]]) -> None:
    """Save YOLO format annotations to file."""
    label_path.parent.mkdir(parents=True, exist_ok=True)
    with open(label_path, "w", encoding="utf-8") as f:
        for cls_id, x, y, w, h in labels:
            f.write(f"{cls_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")


def yolo_to_bbox_px(yolo_box: tuple[float, float, float, float], img_w: int, img_h: int) -> tuple[int, int, int, int]:
    """Convert normalized YOLO box (xc, yc, w, h) to pixel box (xmin, ymin, xmax, ymax)."""
    xc, yc, w, h = yolo_box
    xmin = int((xc - w / 2) * img_w)
    ymin = int((yc - h / 2) * img_h)
    xmax = int((xc + w / 2) * img_w)
    ymax = int((yc + h / 2) * img_h)
    return (
        max(0, xmin),
        max(0, ymin),
        min(img_w, xmax),
        min(img_h, ymax),
    )


def bbox_px_to_yolo(bbox_px: tuple[int, int, int, int], img_w: int, img_h: int) -> tuple[float, float, float, float]:
    """Convert pixel box (xmin, ymin, xmax, ymax) to normalized YOLO box (xc, yc, w, h)."""
    xmin, ymin, xmax, ymax = bbox_px
    bw = xmax - xmin
    bh = ymax - ymin
    xc = (xmin + bw / 2) / img_w
    yc = (ymin + bh / 2) / img_h
    w = bw / img_w
    h = bh / img_h
    return (xc, yc, w, h)


def calculate_iou_px(boxA: tuple[int, int, int, int], boxB: tuple[int, int, int, int]) -> float:
    """Calculate Intersection over Union (IoU) between two pixel bounding boxes."""
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    inter_w = max(0, xB - xA)
    inter_h = max(0, yB - yA)
    inter_area = inter_w * inter_h

    boxA_area = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxB_area = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    union_area = float(boxA_area + boxB_area - inter_area)
    if union_area <= 0:
        return 0.0
    return inter_area / union_area
