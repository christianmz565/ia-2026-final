"""Shared COCO format utilities: bbox conversion, schema helpers, category builders."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

from src.constants import CLASS_NAMES, DEFAULT_CONF_THRESHOLD


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
    x_top_left = max(0.0, x_center * img_w - abs_w / 2.0)
    y_top_left = max(0.0, y_center * img_h - abs_h / 2.0)
    abs_w = max(0.1, min(float(img_w) - x_top_left, abs_w))
    abs_h = max(0.1, min(float(img_h) - y_top_left, abs_h))
    return [round(x_top_left, 2), round(y_top_left, 2), round(abs_w, 2), round(abs_h, 2)]


def build_categories(class_names: list[str] | None = None) -> list[dict[str, Any]]:
    """Build a COCO-format categories list with 0-based IDs.

    Args:
        class_names: List of class names. Defaults to ``CLASS_NAMES``.

    Returns:
        List of category dicts with ``id`` (0-based), ``name``, and ``supercategory``.
    """
    if class_names is None:
        names = CLASS_NAMES
    elif len(class_names) == 0:
        raise ValueError("class_names must not be empty")
    else:
        names = class_names
    return [
        {"id": i, "name": name, "supercategory": "object"}
        for i, name in enumerate(names)
    ]


SUPPORTED_IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".bmp"}


def _bbox_iou_xywh(a: list[float], b: list[float]) -> float:
    """IoU of two ``[x, y, w, h]`` boxes."""
    ax, ay, aw, ah = (float(v) for v in a)
    bx, by, bw, bh = (float(v) for v in b)
    inter_w = max(0.0, min(ax + aw, bx + bw) - max(ax, bx))
    inter_h = max(0.0, min(ay + ah, by + bh) - max(ay, by))
    inter = inter_w * inter_h
    union = aw * ah + bw * bh - inter
    return inter / union if union > 0 else 0.0


def operating_point_metrics(
    coco_gt: COCO,
    pred_anns: list[dict[str, Any]],
    conf_threshold: float = 0.5,
    iou_threshold: float = 0.5,
) -> dict[str, float]:
    """Greedy operating-point precision/recall/F1 at a fixed confidence threshold.

    Predictions below ``conf_threshold`` are ignored. Remaining predictions, in
    descending score order, each match the highest-IoU unmatched ground truth of
    the same image and category at ``iou_threshold`` (ties take the first box).
    Crowd annotations never match. Empty-GT/empty-prediction edge: precision is
    1.0 only when nothing was predicted and nothing was missed, else 0.0; recall
    is 1.0 when there is nothing to miss.
    """
    gt_by_key: dict[tuple[int, int], list[dict[str, Any]]] = {}
    for ann in coco_gt.loadAnns(coco_gt.getAnnIds()):
        if ann.get("iscrowd", 0):
            continue
        gt_by_key.setdefault((ann["image_id"], ann["category_id"]), []).append(ann)
    matched: set[tuple[tuple[int, int], int]] = set()
    tp = 0
    fp = 0
    candidates = [p for p in pred_anns if float(p.get("score", 0.0)) >= conf_threshold]
    candidates.sort(key=lambda p: float(p.get("score", 0.0)), reverse=True)
    for pred in candidates:
        key = (pred["image_id"], pred["category_id"])
        best_iou = iou_threshold
        best_idx = -1
        for idx, gt_ann in enumerate(gt_by_key.get(key, [])):
            if (key, idx) in matched:
                continue
            iou = _bbox_iou_xywh(pred["bbox"], gt_ann["bbox"])
            if iou >= best_iou:
                best_iou = iou
                best_idx = idx
        if best_idx >= 0:
            matched.add((key, best_idx))
            tp += 1
        else:
            fp += 1
    fn = sum(
        1 for key, anns in gt_by_key.items() for idx in range(len(anns)) if (key, idx) not in matched
    )
    precision = tp / (tp + fp) if (tp + fp) > 0 else (1.0 if fn == 0 else 0.0)
    recall = tp / (tp + fn) if (tp + fn) > 0 else 1.0
    f1 = round(2 * precision * recall / (precision + recall), 4) if (precision + recall) > 0 else 0.0
    return {"precision": round(precision, 4), "recall": round(recall, 4), "f1": f1}



def run_coco_eval(
    gt_path: Path | str,
    pred_path: Path | str,
    conf_threshold: float = DEFAULT_CONF_THRESHOLD,
) -> dict[str, Any]:
    """Run pycocotools COCOeval and return summary stats.

    Args:
        gt_path: Path to ground truth COCO JSON.
        pred_path: Path to predictions COCO JSON.
        conf_threshold: Operating confidence for precision/recall/F1.

    Returns:
        Dict with ``mAP_50``, ``mAP_50_95`` (COCO-standard), operating-point
        ``precision``/``recall``/``f1`` at ``conf_threshold``, per-class AP@50
        (``per_class_ap``), ``num_images``, ``num_predictions``.
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
    mAP_50 = float(stats[1])
    mAP_50_95 = float(stats[0])

    P = coco_eval.eval["precision"]

    per_class_ap: dict[str, float] = {}
    cat_ids = coco_gt.getCatIds()
    for i, cat in enumerate(coco_gt.loadCats(cat_ids)):
        cat_name = cat.get("name")
        if cat_name is None:
            raise ValueError(f"Ground truth category at index {i} is missing its name")
        p_class = P[0, :, i, 0, 2]
        valid_p_class = p_class[p_class > -1]
        if len(valid_p_class) == 0:
            raise ValueError(f"No valid AP@50 samples for ground truth category {cat_name!r}")
        per_class_ap[cat_name] = round(float(np.mean(valid_p_class)), 4)

    pred_anns = coco_dt.loadAnns(coco_dt.getAnnIds())
    op = operating_point_metrics(coco_gt, pred_anns, conf_threshold=conf_threshold)

    metrics: dict[str, Any] = {
        "mAP_50": mAP_50,
        "mAP_50_95": mAP_50_95,
        "precision": op["precision"],
        "recall": op["recall"],
        "f1": op["f1"],
        "per_class_ap": per_class_ap,
        "num_images": len(coco_gt.getImgIds()),
        "num_predictions": len(coco_dt.getAnnIds()),
    }
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
