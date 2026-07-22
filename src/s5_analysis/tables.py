"""Generate LaTeX / Markdown comparison tables from aggregated results.

Standalone usage:
    uv run python -m src.s5_analysis.tables [--input PATH] [--format latex]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.constants import S5_OUTPUT

logger = structlog.get_logger(__name__)


def generate_tables(
    aggregated: dict[str, Any],
    output_dir: Path | str | None = None,
    fmt: str = "latex",
    force: bool = False,
) -> Path:
    """Generate comparison tables from aggregated results.

    Args:
        aggregated: Output of ``aggregate_results()``.
        output_dir: Where to write table files.
        fmt: Output format — ``latex``, ``markdown``, or ``csv``.
        force: If True, bypass cache and re-generate tables.

    Returns:
        Path to the generated table file.
    """
    resolved_output_dir = Path(output_dir or S5_OUTPUT / "tables")
    table_path = resolved_output_dir / f"comparison_table.{fmt}"

    def _do_generate() -> Path:
        resolved_output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(
            "generate_tables_stub",
            rows=len(aggregated.get("rows", [])),
            format=fmt,
            output=str(resolved_output_dir),
        )
        table_path.write_text("% Table generation not yet implemented\n")
        return table_path

    return run_cached_step(
        step_name="generate_tables",
        target_path=table_path,
        fn=_do_generate,
        force=force,
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import AnalysisConfig

    standalone_main(
        config_model=AnalysisConfig,
        run_fn=lambda cfg: generate_tables(
            json.loads(Path(cfg.input).read_text()) if cfg.input else {},
            fmt=cfg.output_format,
        ),
        description="Generate comparison tables",
        required_fields=["input"],
    )
