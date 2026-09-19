"""Simultaneous per-class confidence intervals with Bonferroni correction.

Extension to the operating-point analysis: per-class TP/FP/FN counts come from
the same IoU>=0.5 greedy same-class matching as ``operating_point_metrics``
(see ``src.coco_utils.per_class_operating_point_counts``); per-class precision
and recall are binomial proportions, each reported with a Wilson score interval
at level ``1 - ALPHA / K`` for simultaneous 95% family-wise coverage over the
``K = NUM_CLASSES`` defect classes.

Ground truth / prediction pairing: ``s4_evaluate_new`` predictions were
produced from the re-split dataset, so the matching ground truth is
``s1_prepare_meta/split/test/_annotations.coco.json`` (NOT ``s1_prepare``,
which is the older split in a different coordinate space; that pairing yields
near-zero recall). Confidence thresholds are the per-model calibrated operating
points from Methods (RF-DETR 0.20 / YOLO26 0.30 / Cascade R-CNN 0.50), verified
as the observed score floors of the stored ``predictions.json`` files.

Standalone usage:
    uv run python -m src.s5_analysis.bonferroni_intervals
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from statistics import NormalDist
from typing import Any

import structlog
from pycocotools.coco import COCO

from src.coco_utils import per_class_operating_point_counts
from src.constants import ID_TO_CLASS, NUM_CLASSES, PARTIALS_DIR

logger = structlog.get_logger(__name__)

ALPHA = 0.05
K = NUM_CLASSES
CONFIDENCE_PER_INTERVAL = 1 - ALPHA / K
Z = NormalDist().inv_cdf(1 - ALPHA / (2 * K))
IOU_THRESHOLD = 0.5

MODELS: list[str] = ["rf_detr", "cascade_rcnn", "yolo26"]
AUGMENTATIONS: list[str] = ["baseline", "albumentations_balanced", "boxaug_standard", "boxaug_libcom"]

MODEL_CONF_THRESHOLDS: dict[str, float] = {
    "rf_detr": 0.20,
    "yolo26": 0.30,
    "cascade_rcnn": 0.50,
}

GT_PATH = PARTIALS_DIR / "s1_prepare_meta" / "split" / "test" / "_annotations.coco.json"
PREDICTIONS_ROOT = PARTIALS_DIR / "s4_evaluate_new"
OUTPUT_DIR = PARTIALS_DIR / "s5_analysis_new"
JSON_OUTPUT = OUTPUT_DIR / "bonferroni_per_class_intervals.json"
CSV_OUTPUT = OUTPUT_DIR / "bonferroni_per_class_intervals.csv"

METRICS: tuple[str, str] = ("precision", "recall")


def wilson_interval(x: int, n: int) -> tuple[float, float] | None:
    """Wilson score interval for a binomial proportion at the module level ``Z``.

    Returns ``None`` when ``n == 0`` (no trials: precision with no predictions
    of the class, or recall with zero class support in test). Never returns a
    zero-width interval and never imputes.
    """
    if n == 0:
        return None
    if x < 0:
        raise ValueError(f"Success count below zero: x={x}")
    if x > n:
        raise ValueError(f"Success count exceeds trials: x={x} > n={n}")
    p_hat = x / n
    z2_over_n = Z * Z / n
    denominator = 1 + z2_over_n
    center = (p_hat + z2_over_n / 2) / denominator
    half = Z * math.sqrt(p_hat * (1 - p_hat) / n + Z * Z / (4 * n * n)) / denominator
    return (max(0.0, center - half), min(1.0, center + half))


def bonferroni_table(counts: dict[int, dict[str, int]]) -> dict[str, dict[str, Any]]:
    """Per-class precision/recall point estimates with simultaneous intervals.

    Args:
        counts: Output of ``per_class_operating_point_counts``.

    Returns:
        Dict keyed by class name with ``tp``/``fp``/``fn``/``support`` plus a
        ``precision`` and a ``recall`` entry, each holding ``estimate``, ``lo``,
        ``hi`` (``None`` when undefined: ``n == 0``), and ``n``. Full precision;
        rounding happens only at serialization.
    """
    table: dict[str, dict[str, Any]] = {}
    for class_id in sorted(counts):
        entry = counts[class_id]
        class_name = ID_TO_CLASS.get(class_id, f"class_{class_id}")
        tp = entry["tp"]
        fp = entry["fp"]
        support = entry["support"]
        n_precision = tp + fp
        precision_estimate = tp / n_precision if n_precision > 0 else None
        precision_interval = wilson_interval(tp, n_precision)
        recall_estimate = tp / support if support > 0 else None
        recall_interval = wilson_interval(tp, support)
        table[class_name] = {
            "tp": tp,
            "fp": fp,
            "fn": entry["fn"],
            "support": support,
            "precision": {
                "estimate": precision_estimate,
                "lo": precision_interval[0] if precision_interval is not None else None,
                "hi": precision_interval[1] if precision_interval is not None else None,
                "n": n_precision,
            },
            "recall": {
                "estimate": recall_estimate,
                "lo": recall_interval[0] if recall_interval is not None else None,
                "hi": recall_interval[1] if recall_interval is not None else None,
                "n": support,
            },
        }
    return table


def build_all_intervals() -> dict[str, Any]:
    """Compute simultaneous intervals for all 12 model x augmentation configs."""
    if not GT_PATH.exists():
        raise FileNotFoundError(f"Ground truth not found: {GT_PATH}")
    coco_gt = COCO(str(GT_PATH))
    configs: dict[str, Any] = {}
    for model in MODELS:
        if model not in MODEL_CONF_THRESHOLDS:
            raise KeyError(f"No calibrated operating point for model {model!r}")
        conf_threshold = MODEL_CONF_THRESHOLDS[model]
        for aug in AUGMENTATIONS:
            pred_path = PREDICTIONS_ROOT / model / aug / "predictions.json"
            if not pred_path.exists():
                raise FileNotFoundError(f"Predictions not found: {pred_path}")
            coco_dt = COCO(str(pred_path))
            pred_anns = coco_dt.loadAnns(coco_dt.getAnnIds())
            counts = per_class_operating_point_counts(
                coco_gt, pred_anns, conf_threshold=conf_threshold, iou_threshold=IOU_THRESHOLD
            )
            configs[f"{model}/{aug}"] = {
                "model": model,
                "augmentation": aug,
                "conf_threshold": conf_threshold,
                "classes": bonferroni_table(counts),
            }
    return {
        "alpha": ALPHA,
        "k": K,
        "confidence_per_interval": CONFIDENCE_PER_INTERVAL,
        "z": Z,
        "iou_threshold": IOU_THRESHOLD,
        "configs": configs,
    }


def _round_payload(value: Any) -> Any:
    if isinstance(value, float):
        return round(value, 4)
    if isinstance(value, dict):
        return {key: _round_payload(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_round_payload(item) for item in value]
    return value


def _rounded(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 4)


def write_artifacts(payload: dict[str, Any]) -> tuple[Path, Path]:
    """Serialize the full numeric record to JSON and flat CSV (4 dp)."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT.write_text(json.dumps(_round_payload(payload), indent=2))
    rows: list[dict[str, Any]] = []
    for key in sorted(payload["configs"]):
        config = payload["configs"][key]
        for class_name, class_entry in config["classes"].items():
            for metric in METRICS:
                cell = class_entry[metric]
                rows.append(
                    {
                        "model": config["model"],
                        "augmentation": config["augmentation"],
                        "class": class_name,
                        "metric": metric,
                        "estimate": _rounded(cell["estimate"]),
                        "lo": _rounded(cell["lo"]),
                        "hi": _rounded(cell["hi"]),
                        "n": cell["n"],
                    }
                )
    with open(CSV_OUTPUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["model", "augmentation", "class", "metric", "estimate", "lo", "hi", "n"])
        writer.writeheader()
        writer.writerows(rows)
    logger.info("bonferroni_artifacts_written", json=str(JSON_OUTPUT), csv=str(CSV_OUTPUT), rows=len(rows))
    return JSON_OUTPUT, CSV_OUTPUT


def main() -> tuple[Path, Path]:
    """Build intervals for all configs and write the JSON+CSV record."""
    return write_artifacts(build_all_intervals())


if __name__ == "__main__":
    main()
