"""s4_evaluate pipeline — runs inference -> metrics -> export for all model/aug combos.

Standalone usage:
    uv run python -m src.s4_evaluate.pipeline [--models rf_detr,cascade_rcnn,yolo26] [--augments baseline,geometric,photometric]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.config import S4Config
from src.constants import AUGMENTED_DIR, S3_OUTPUT, S4_OUTPUT, SPLIT_DATASET, TEST_SPLIT
from src.s4_evaluate.export import export_results
from src.s4_evaluate.inference import run_inference
from src.s4_evaluate.metrics import compute_metrics

logger = structlog.get_logger(__name__)


def run_pipeline(config: S4Config | None = None) -> None:
    """Evaluate all trained models on all augmented test sets.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S4Config()

    logger.info("s4_pipeline_start", models=config.models, augments=config.augments)

    if config.eval.model_path:
        out_dir = S4_OUTPUT
        out_dir.mkdir(parents=True, exist_ok=True)
        pred_path = out_dir / "predictions.json"
        predictions = run_inference(
            model_path=config.eval.model_path,
            data_dir=config.eval.data_dir or (SPLIT_DATASET / TEST_SPLIT),
            output_path=pred_path,
            device=config.eval.device,
            conf_threshold=config.eval.conf_threshold,
        )
        metrics_path = out_dir / "metrics.json"
        gt_path = config.eval.ground_truth or (
            (config.eval.data_dir or (SPLIT_DATASET / TEST_SPLIT)) / "_annotations.coco.json"
        )
        metrics = compute_metrics(
            predictions=config.eval.predictions or pred_path,
            ground_truth=gt_path,
            iou_threshold=config.eval.iou_threshold,
            output_path=metrics_path,
        )
        results_path = out_dir / "results.json"
        export_results(
            results=metrics if isinstance(metrics, dict) else predictions,
            output_path=results_path,
        )
        logger.info("s4_pipeline_complete")
        return

    for model_name in config.models:
        for aug_name in config.augments:
            eval_out_dir = S4_OUTPUT / model_name / aug_name
            eval_out_dir.mkdir(parents=True, exist_ok=True)

            from src.constants import PROJECT_ROOT
            model_weights = S3_OUTPUT / model_name / aug_name / "best.pt"
            if not model_weights.exists() or model_weights.stat().st_size == 0:
                model_weights = S3_OUTPUT / model_name / aug_name
                checkpoints = [p for p in list(model_weights.glob("*.pt")) + list(model_weights.glob("*.pth")) if p.is_file() and p.stat().st_size > 0] if model_weights.exists() else []
                if not checkpoints:
                    alt_dir = PROJECT_ROOT / "results" / model_name / aug_name
                    if alt_dir.exists():
                        model_weights = alt_dir

            data_dir = (SPLIT_DATASET / TEST_SPLIT) if aug_name == "baseline" else (AUGMENTED_DIR / aug_name / TEST_SPLIT)
            if not Path(data_dir).exists():
                data_dir = SPLIT_DATASET / TEST_SPLIT

            pred_path = eval_out_dir / "predictions.json"
            predictions = run_inference(
                model_path=model_weights,
                data_dir=data_dir,
                output_path=pred_path,
                device=config.eval.device,
                conf_threshold=config.eval.conf_threshold,
            )

            metrics_path = eval_out_dir / "metrics.json"
            gt_path = config.eval.ground_truth or (data_dir / "_annotations.coco.json")
            if not Path(gt_path).exists():
                gt_path = SPLIT_DATASET / TEST_SPLIT / "_annotations.coco.json"

            metrics = compute_metrics(
                predictions=config.eval.predictions or pred_path,
                ground_truth=gt_path,
                iou_threshold=config.eval.iou_threshold,
                output_path=metrics_path,
            )

            results_path = eval_out_dir / "results.json"
            export_results(
                results=metrics if isinstance(metrics, dict) else predictions,
                output_path=results_path,
            )
            logger.info("s4_combo_complete", model=model_name, augment=aug_name, out_dir=str(eval_out_dir))

    logger.info("s4_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S4Config,
        run_fn=run_pipeline,
        description="s4_evaluate pipeline",
        skip_fields=["eval"],
    )
