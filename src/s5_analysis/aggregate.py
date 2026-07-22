"""Aggregate evaluation results from s4_evaluate into unified DataFrames.

Standalone usage:
    uv run python -m src.s5_analysis.aggregate [--results-dir PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.constants import S4_OUTPUT, S5_OUTPUT

logger = structlog.get_logger(__name__)


def aggregate_results(
    results_dir: Path | str | None = None,
    output_path: Path | str | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Load all JSON result files and merge into a single comparison dict.

    Args:
        results_dir: Directory containing per-run result JSONs.
        output_path: Where to write the aggregated comparison.
        force: If True, bypass cache and re-aggregate results.

    Returns:
        Dict with keys: rows (list of dicts), columns, summary_stats.
    """
    resolved_input = Path(results_dir or S4_OUTPUT)
    resolved_output = Path(output_path or S5_OUTPUT / "aggregated.json")

    def _aggregate() -> dict[str, Any]:
        result_files = list(resolved_input.rglob("*.json"))
        logger.info("aggregating_results", count=len(result_files), directory=str(resolved_input))

        rows: list[dict[str, Any]] = []
        for rf in result_files:
            with open(rf) as f:
                data = json.load(f)
            data["_source_file"] = str(rf.name)
            rows.append(data)

        aggregated = {
            "rows": rows,
            "columns": list(rows[0].keys()) if rows else [],
            "summary_stats": {},
        }

        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        with open(resolved_output, "w") as f:
            json.dump(aggregated, f, indent=2, default=str)

        logger.info("aggregation_complete", rows=len(rows))
        return aggregated

    return run_cached_step(
        step_name="aggregate",
        target_path=resolved_output,
        fn=_aggregate,
        force=force,
        loader=lambda p: json.loads(p.read_text()),
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import S5Config

    standalone_main(
        config_model=S5Config,
        run_fn=lambda cfg: aggregate_results(cfg.results_dir or S4_OUTPUT, None),
        description="Aggregate evaluation results",
        skip_fields=["analysis"],
    )
