"""Run model inference on test set with timing measurements.

Standalone usage:
    uv run python -m src.s4_evaluate.inference [--model-path PATH] [--data-dir PATH]
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import structlog

logger = structlog.get_logger(__name__)


def run_inference(
    model_path: Path | str,
    data_dir: Path | str,
    output_path: Path | str | None = None,
    device: str = "cuda:0",
    conf_threshold: float = 0.25,
) -> dict[str, Any]:
    """Run inference and produce predictions with timing.

    Args:
        model_path: Path to trained model weights/checkpoint.
        data_dir: Directory with test images.
        output_path: Where to save prediction results.
        device: Device string for inference.
        conf_threshold: Confidence threshold for detections.

    Returns:
        Dict with keys: predictions_path, total_time_ms, avg_time_ms,
        num_images, num_detections.
    """
    # TODO: implement inference loop for each model paradigm
    logger.info(
        "inference_stub",
        model=str(model_path),
        data_dir=str(data_dir),
        device=device,
        conf=conf_threshold,
    )
    return {
        "predictions_path": str(output_path) if output_path else None,
        "total_time_ms": 0.0,
        "avg_time_ms": 0.0,
        "num_images": 0,
        "num_detections": 0,
    }


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import EvalConfig

    standalone_main(
        config_model=EvalConfig,
        run_fn=lambda cfg: logger.info(
            "inference_result",
            **run_inference(cfg.model_path, cfg.data_dir, cfg.output_path or None, cfg.device, cfg.conf_threshold),
        ),
        description="Run model inference",
        required_fields=["model_path", "data_dir"],
    )
