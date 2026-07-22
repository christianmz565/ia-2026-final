"""Generate LaTeX / Markdown comparison tables from aggregated results.

Standalone usage:
    uv run python -m src.s5_analysis.tables [--input PATH] [--format latex]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.constants import S5_OUTPUT

logger = structlog.get_logger(__name__)


def generate_tables(
    aggregated: dict[str, Any],
    output_dir: Path | str | None = None,
    fmt: str = "latex",
) -> Path:
    """Generate comparison tables from aggregated results.

    Args:
        aggregated: Output of ``aggregate_results()``.
        output_dir: Where to write table files.
        fmt: Output format — ``latex``, ``markdown``, or ``csv``.

    Returns:
        Path to the generated table file.
    """
    output_dir = Path(output_dir or S5_OUTPUT / "tables")
    output_dir.mkdir(parents=True, exist_ok=True)

    # TODO: build per-model and per-augmentation comparison tables
    logger.info(
        "generate_tables_stub",
        rows=len(aggregated.get("rows", [])),
        format=fmt,
        output=str(output_dir),
    )

    # Placeholder: write empty table
    table_path = output_dir / f"comparison_table.{fmt}"
    table_path.write_text("% Table generation not yet implemented\n")
    return table_path


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
