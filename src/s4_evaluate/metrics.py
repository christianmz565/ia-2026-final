"""COCO-style detection metrics: mAP, precision, recall, F1, per-class AP.

Standalone usage:
    uv run python -m src.s4_evaluate.metrics [--predictions PATH] [--ground-truth PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

from src.caching import run_cached_step
from src.constants import CLASS_NAMES, S4_OUTPUT

logger = structlog.get_logger(__name__)


def compute_metrics(
    predictions: Path | str,
    ground_truth: Path | str,
    iou_threshold: float = 0.5,
    output_path: Path | str | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Compute COCO-style detection metrics from predictions and ground truth.

    Args:
        predictions: Path to predictions COCO JSON file.
        ground_truth: Path to ground truth COCO JSON file.
        iou_threshold: IoU threshold for positive matches (used for F1 at threshold).
        output_path: Path to output metrics JSON file.
        force: If True, bypass cache and re-compute metrics.

    Returns:
        Dict with keys: mAP_50, mAP_50_95, precision, recall, f1,
        per_class_ap, num_images, num_predictions.
    """
    resolved_output = Path(output_path or S4_OUTPUT / "metrics.json")

    def _compute() -> dict[str, Any]:
        gt_path = Path(ground_truth)
        pred_path = Path(predictions)

        if not gt_path.exists():
            raise FileNotFoundError(f"Ground truth not found: {gt_path}")
        if not pred_path.exists():
            raise FileNotFoundError(f"Predictions not found: {pred_path}")

        coco_gt = COCO(str(gt_path))
        coco_dt = COCO(str(pred_path))

        coco_eval = COCOeval(coco_gt, coco_dt, "bbox")
        coco_eval.evaluate()
        coco_eval.accumulate()
        coco_eval.summarize()

        metrics: dict[str, Any] = {
            "mAP_50": float(coco_eval.stats[1]),
            "mAP_50_95": float(coco_eval.stats[0]),
            "precision": float(coco_eval.stats[5]),
            "recall": float(coco_eval.stats[6]),
        }

        p, r = metrics["precision"], metrics["recall"]
        metrics["f1"] = round(2 * p * r / (p + r + 1e-8), 4)

        per_class_ap: dict[str, float] = {}
        precision_per_class = coco_eval.eval["precision"]
        per_class_values = precision_per_class[:, :, :, 0, 0].mean(axis=(0, 1))
        for i, cat in enumerate(coco_gt.loadCats(coco_gt.getCatIds())):
            cat_name = cat.get("name", CLASS_NAMES[i] if i < len(CLASS_NAMES) else str(cat["id"]))
            per_class_ap[cat_name] = round(float(per_class_values[i]), 4)

        metrics["per_class_ap"] = per_class_ap
        metrics["num_images"] = len(coco_gt.getImgIds())
        metrics["num_predictions"] = len(coco_dt.getAnnIds())

        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        resolved_output.write_text(json.dumps(metrics, indent=2))
        logger.info("metrics_complete", output=str(resolved_output), mAP_50=metrics["mAP_50"])
        return metrics

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
            "metrics_result",
            **compute_metrics(cfg.predictions, cfg.ground_truth, cfg.iou_threshold),
        ),
        description="Compute COCO detection metrics",
        required_fields=["predictions", "ground_truth"],
    )
