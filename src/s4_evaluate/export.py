"""Export evaluation results to standardized JSON format.

Standalone usage:
    uv run python -m src.s4_evaluate.export [--output PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.constants import S4_OUTPUT

logger = structlog.get_logger(__name__)


def export_results(
    results: dict[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write evaluation results to a JSON file.

    Args:
        results: Dictionary of metric results to persist.
        output_path: Destination file. Defaults to S4_OUTPUT / ``results.json``.

    Returns:
        Path to the written JSON file.
    """
    output_path = Path(output_path) if output_path else S4_OUTPUT / "results.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: implement structured export with model name, augmentation, timestamp
    logger.info("export_results_stub", output=str(output_path), keys=list(results.keys()))

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)

    return output_path


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import EvalConfig

    standalone_main(
        config_model=EvalConfig,
        run_fn=lambda cfg: export_results(json.loads(cfg.output_path or "{}"), cfg.output_path or None),
        description="Export evaluation results",
    )
