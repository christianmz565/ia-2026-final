"""Standardized detection metrics: mAP, precision, recall, F1, IoU.

Standalone usage:
    uv run python -m src.s4_evaluate.metrics [--predictions PATH] [--ground-truth PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.constants import S4_OUTPUT

logger = structlog.get_logger(__name__)


def compute_metrics(
    predictions: Path | str,
    ground_truth: Path | str,
    iou_threshold: float = 0.5,
    output_path: Path | str | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Compute detection metrics for a single model/augmentation combination.

    Args:
        predictions: Path to predictions file (COCO JSON or YOLO txt).
        ground_truth: Path to ground truth annotations.
        iou_threshold: IoU threshold for positive matches.
        output_path: Path to output metrics JSON file.
        force: If True, bypass cache and re-compute metrics.

    Returns:
        Dict with keys: mAP_50, mAP_50_95, precision, recall, f1,
        per_class_ap, inference_time_ms, model_params, model_size_mb.
    """
    resolved_output = Path(output_path or S4_OUTPUT / "metrics.json")

    def _compute() -> dict[str, Any]:
        logger.info(
            "compute_metrics_stub",
            predictions=str(predictions),
            ground_truth=str(ground_truth),
            iou_threshold=iou_threshold,
        )
        res = {
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
        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        resolved_output.write_text(json.dumps(res, indent=2))
        return res

    return run_cached_step(
        step_name="metrics",
        target_path=resolved_output,
        fn=_compute,
        force=force,
        loader=lambda p: json.loads(p.read_text()),
    )


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
