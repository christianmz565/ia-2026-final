"""COCO-style detection metrics: mAP, precision, recall, F1, per-class AP.

Standalone usage:
    uv run python -m src.s4_evaluate.metrics [--predictions PATH] [--ground-truth PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
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

        stats = coco_eval.stats
        mAP_50 = float(stats[1])
        mAP_50_95 = float(stats[0])

        P = coco_eval.eval["precision"]
        R = coco_eval.eval["recall"]

        # IoU=0.50 (index 0), all areas (index 0), maxDets=100 (index 2)
        prec_50_all = P[0, :, :, 0, 2]
        valid_prec = prec_50_all[prec_50_all > -1]
        precision = float(np.mean(valid_prec)) if len(valid_prec) > 0 else 0.0

        rec_50_all = R[0, :, 0, 2]
        valid_rec = rec_50_all[rec_50_all > -1]
        recall = float(np.mean(valid_rec)) if len(valid_rec) > 0 else 0.0

        f1 = round(2 * precision * recall / (precision + recall + 1e-8), 4)

        per_class_ap: dict[str, float] = {}
        cat_ids = coco_gt.getCatIds()
        for i, cat in enumerate(coco_gt.loadCats(cat_ids)):
            cat_name = cat.get("name", CLASS_NAMES[i] if i < len(CLASS_NAMES) else str(cat["id"]))
            p_class = P[0, :, i, 0, 2]
            valid_p_class = p_class[p_class > -1]
            per_class_ap[cat_name] = round(float(np.mean(valid_p_class)), 4) if len(valid_p_class) > 0 else 0.0

        metrics: dict[str, Any] = {
            "mAP_50": mAP_50,
            "mAP_50_95": mAP_50_95,
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": f1,
            "per_class_ap": per_class_ap,
            "num_images": len(coco_gt.getImgIds()),
            "num_predictions": len(coco_dt.getAnnIds()),
        }

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
