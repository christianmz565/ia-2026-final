"""Run model inference on test set with timing measurements.

Standalone usage:
    uv run python -m src.s4_evaluate.inference [--model-path PATH] [--data-dir PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.constants import S4_OUTPUT

logger = structlog.get_logger(__name__)


def run_inference(
    model_path: Path | str,
    data_dir: Path | str,
    output_path: Path | str | None = None,
    device: str = "cuda:0",
    conf_threshold: float = 0.25,
    force: bool = False,
) -> dict[str, Any]:
    """Run inference and produce predictions with timing.

    Args:
        model_path: Path to trained model weights/checkpoint.
        data_dir: Directory with test images.
        output_path: Where to save prediction results.
        device: Device string for inference.
        conf_threshold: Confidence threshold for detections.
        force: If True, bypass cache and re-run inference.

    Returns:
        Dict with keys: predictions_path, total_time_ms, avg_time_ms,
        num_images, num_detections.
    """
    resolved_output = Path(output_path or S4_OUTPUT / "predictions.json")

    def _do_inference() -> dict[str, Any]:
        logger.info(
            "inference_stub",
            model=str(model_path),
            data_dir=str(data_dir),
            device=device,
            conf=conf_threshold,
        )
        res = {
            "predictions_path": str(resolved_output),
            "total_time_ms": 0.0,
            "avg_time_ms": 0.0,
            "num_images": 0,
            "num_detections": 0,
        }
        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        resolved_output.write_text(json.dumps(res, indent=2))
        return res

    return run_cached_step(
        step_name="inference",
        target_path=resolved_output,
        fn=_do_inference,
        force=force,
        loader=lambda p: json.loads(p.read_text()),
    )


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
