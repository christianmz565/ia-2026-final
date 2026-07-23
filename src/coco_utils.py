"""Shared COCO format utilities: bbox conversion, schema helpers, category builders."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

from src.constants import CLASS_NAMES


def yolo_to_coco_bbox(
    x_center: float,
    y_center: float,
    w: float,
    h: float,
    img_w: int,
    img_h: int,
) -> list[float]:
    """Convert normalized YOLO bbox ``[cx, cy, w, h]`` to COCO ``[x_top_left, y_top_left, w, h]`` in pixels."""
    abs_w = w * img_w
    abs_h = h * img_h
    x_top_left = x_center * img_w - abs_w / 2
    y_top_left = y_center * img_h - abs_h / 2
    return [round(x_top_left, 2), round(y_top_left, 2), round(abs_w, 2), round(abs_h, 2)]


def build_categories(class_names: list[str] | None = None) -> list[dict[str, Any]]:
    """Build a COCO-format categories list with 0-based IDs.

    Args:
        class_names: List of class names. Defaults to ``CLASS_NAMES``.

    Returns:
        List of category dicts with ``id`` (0-based), ``name``, and ``supercategory``.
    """
    names = class_names or CLASS_NAMES
    return [
        {"id": i, "name": name, "supercategory": "object"}
        for i, name in enumerate(names)
    ]


SUPPORTED_IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".bmp"}


def run_coco_eval(
    gt_path: Path | str,
    pred_path: Path | str,
) -> dict[str, Any]:
    """Run pycocotools COCOeval and return summary stats.

    Args:
        gt_path: Path to ground truth COCO JSON.
        pred_path: Path to predictions COCO JSON.

    Returns:
        Dict with ``mAP_50``, ``mAP_50_95``, ``precision``, ``recall``, ``f1``,
        ``per_class_ap``, ``num_images``, ``num_predictions``.
    """
    gt_path = str(gt_path)
    pred_path = str(pred_path)

    coco_gt = COCO(gt_path)
    coco_dt = COCO(pred_path)

    coco_eval = COCOeval(coco_gt, coco_dt, "bbox")
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    stats = coco_eval.stats
    metrics: dict[str, Any] = {
        "mAP_50": float(stats[1]),
        "mAP_50_95": float(stats[0]),
        "precision": float(stats[5]),
        "recall": float(stats[6]),
    }

    p, r = metrics["precision"], metrics["recall"]
    metrics["f1"] = round(2 * p * r / (p + r + 1e-8), 4)

    precision_per_class = coco_eval.eval["precision"]
    per_class_values = precision_per_class[:, :, :, 0, 0].mean(axis=(0, 1))
    per_class_ap: dict[str, float] = {}
    for i, cat in enumerate(coco_gt.loadCats(coco_gt.getCatIds())):
        cat_name = cat.get("name", CLASS_NAMES[i] if i < len(CLASS_NAMES) else str(cat["id"]))
        per_class_ap[cat_name] = round(float(per_class_values[i]), 4)

    metrics["per_class_ap"] = per_class_ap
    metrics["num_images"] = len(coco_gt.getImgIds())
    metrics["num_predictions"] = len(coco_dt.getAnnIds())

    return metrics


def coco_results_from_detections(
    val_coco_dict: dict[str, Any],
    detections: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Convert raw per-image detections to COCO results format for pycocotools.

    Each detection should have ``image_id``, ``boxes`` (N×4 tensor/array in
    ``[xmin, ymin, xmax, ymax]`` format), ``scores``, and ``labels``.

    Args:
        val_coco_dict: The ground truth COCO dict (used for category mapping).
        detections: List of per-image detection dicts.

    Returns:
        List of COCO result dicts with ``image_id``, ``category_id``, ``bbox``, ``score``.
    """
    categories = val_coco_dict.get("categories", [])
    label_to_cat_id = {i: cat["id"] for i, cat in enumerate(categories)}

    coco_results: list[dict[str, Any]] = []
    for det in detections:
        img_id = det["image_id"]
        boxes = det["boxes"]
        scores = det["scores"]
        labels = det["labels"]

        for box, score, label in zip(boxes, scores, labels, strict=False):
            xmin, ymin, xmax, ymax = box
            w = float(xmax - xmin)
            h = float(ymax - ymin)
            if w <= 0 or h <= 0:
                continue

            cat_id = label_to_cat_id.get(int(label), int(label))
            coco_results.append(
                {
                    "image_id": img_id,
                    "category_id": cat_id,
                    "bbox": [float(xmin), float(ymin), w, h],
                    "score": float(score),
                }
            )

    return coco_results
