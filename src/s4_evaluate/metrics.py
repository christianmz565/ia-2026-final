"""Standardized detection metrics: mAP, precision, recall, F1, IoU.

Standalone usage:
    uv run python -m src.s4_evaluate.metrics [--predictions PATH] [--ground-truth PATH]
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import structlog

logger = structlog.get_logger(__name__)


def compute_metrics(
    predictions: Path | str,
    ground_truth: Path | str,
    iou_threshold: float = 0.5,
) -> dict[str, Any]:
    """Compute detection metrics for a single model/augmentation combination.

    Args:
        predictions: Path to predictions file (COCO JSON or YOLO txt).
        ground_truth: Path to ground truth annotations.
        iou_threshold: IoU threshold for positive matches.

    Returns:
        Dict with keys: mAP_50, mAP_50_95, precision, recall, f1,
        per_class_ap, inference_time_ms, model_params, model_size_mb.
    """
    # TODO: implement metric computation using pycocotools or manual TP/FP/FN
    logger.info(
        "compute_metrics_stub",
        predictions=str(predictions),
        ground_truth=str(ground_truth),
        iou_threshold=iou_threshold,
    )
    return {
        "mAP_50": 0.0,
        "mAP_50_95": 0.0,
        "precision": 0.0,
        "recall": 0.0,
        "f1": 0.0,
        "per_class_ap": {},
        "inference_time_ms": 0.0,
        "model_params": 0,
        "model_size_mb": 0.0,
    }


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import EvalConfig

    standalone_main(
        config_model=EvalConfig,
        run_fn=lambda cfg: logger.info(
            "metrics_result", **compute_metrics(cfg.predictions, cfg.ground_truth, cfg.iou_threshold)
        ),
        description="Compute detection metrics",
        required_fields=["predictions", "ground_truth"],
    )
