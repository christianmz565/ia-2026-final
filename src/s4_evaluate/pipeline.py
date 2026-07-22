"""s4_evaluate pipeline — runs inference -> metrics -> export for all model/aug combos.

Standalone usage:
    uv run python -m src.s4_evaluate.pipeline
"""

from __future__ import annotations

import structlog

from src.config import S4Config
from src.constants import S3_OUTPUT, S4_OUTPUT, SPLIT_DATASET
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

    logger.info("s4_pipeline_start")

    pred_path = S4_OUTPUT / "predictions.json"
    predictions = run_inference(
        model_path=config.eval.model_path or (S3_OUTPUT / "yolo26" / "best.pt"),
        data_dir=config.eval.data_dir or (SPLIT_DATASET / "test"),
        output_path=pred_path,
        device=config.eval.device,
        conf_threshold=config.eval.conf_threshold,
    )

    metrics_path = S4_OUTPUT / "metrics.json"
    metrics = compute_metrics(
        predictions=config.eval.predictions or pred_path,
        ground_truth=config.eval.ground_truth or (SPLIT_DATASET / "test" / "labels"),
        iou_threshold=config.eval.iou_threshold,
        output_path=metrics_path,
    )

    results_path = S4_OUTPUT / "results.json"
    export_results(
        results=metrics if isinstance(metrics, dict) else predictions,
        output_path=results_path,
    )

    logger.info("s4_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S4Config,
        run_fn=run_pipeline,
        description="s4_evaluate pipeline",
        skip_fields=["eval"],
    )
