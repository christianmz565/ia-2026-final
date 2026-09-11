"""Export evaluation results to standardized JSON format.

Standalone usage:
    uv run python -m src.s4_evaluate.export [--output PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import config_fingerprint, run_cached_step
from src.constants import S4_OUTPUT

logger = structlog.get_logger(__name__)


def export_results(
    results: dict[str, Any],
    output_path: Path | str | None = None,
    force: bool = False,
) -> Path:
    """Write evaluation results to a JSON file.

    Args:
        results: Dictionary of metric results to persist.
        output_path: Destination file. Defaults to S4_OUTPUT / ``results.json``.
        force: If True, bypass cache and re-export results.

    Returns:
        Path to the written JSON file.
    """
    resolved_output = Path(output_path) if output_path else S4_OUTPUT / "results.json"

    def _export() -> Path:
        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        logger.info("export_results_stub", output=str(resolved_output), keys=list(results.keys()))

        with open(resolved_output, "w") as f:
            json.dump(results, f, indent=2, default=str)

        return resolved_output

    return run_cached_step(
        step_name="export",
        target_path=resolved_output,
        fn=_export,
        force=force,
        fingerprint=config_fingerprint({"output": str(resolved_output), "keys": sorted(results.keys())}),
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import EvalConfig

    standalone_main(
        config_model=EvalConfig,
        run_fn=lambda cfg: export_results(json.loads(cfg.output_path or "{}"), cfg.output_path or None),
        description="Export evaluation results",
    )
