"""Generate LaTeX / Markdown / CSV comparison tables from aggregated results.

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
    ext = "tex" if fmt == "latex" else (fmt if fmt in ("md", "csv") else "md")
    table_path = resolved_output_dir / f"comparison_table.{ext}"

    def _do_generate() -> Path:
        resolved_output_dir.mkdir(parents=True, exist_ok=True)
        rows = aggregated.get("rows", [])
        logger.info(
            "generate_tables_start",
            rows=len(rows),
            format=fmt,
            output=str(table_path),
        )

        headers = ["Model", "Augmentation", "mAP@50", "mAP@50-95", "Precision", "Recall", "F1"]
        extracted_rows: list[dict[str, Any]] = []

        for r in rows:
            extracted_rows.append(
                {
                    "Model": r.get("model", "N/A"),
                    "Augmentation": r.get("augmentation", "N/A"),
                    "mAP@50": round(float(r.get("mAP_50", 0.0)), 4),
                    "mAP@50-95": round(float(r.get("mAP_50_95", 0.0)), 4),
                    "Precision": round(float(r.get("precision", 0.0)), 4),
                    "Recall": round(float(r.get("recall", 0.0)), 4),
                    "F1": round(float(r.get("f1", 0.0)), 4),
                }
            )

        if fmt == "csv":
            lines = [",".join(headers)]
            for r in extracted_rows:
                lines.append(",".join(str(r[h]) for h in headers))
            content = "\n".join(lines) + "\n"

        elif fmt == "latex":
            lines = [
                "\\begin{table}[htbp]",
                "\\centering",
                "\\caption{Model Performance Comparison Across Augmentation Datasets}",
                "\\begin{tabular}{llccccc}",
                "\\hline",
                " & ".join(["\\textbf{" + h + "}" for h in headers]) + " \\\\",
                "\\hline",
            ]
            for r in extracted_rows:
                lines.append(" & ".join(str(r[h]) for h in headers) + " \\\\")
            lines.extend(["\\hline", "\\end{tabular}", "\\end{table}"])
            content = "\n".join(lines) + "\n"

        else:
            lines = [
                "| " + " | ".join(headers) + " |",
                "|" + "|".join(["---"] * len(headers)) + "|",
            ]
            for r in extracted_rows:
                lines.append("| " + " | ".join(str(r[h]) for h in headers) + " |")
            content = "\n".join(lines) + "\n"

        table_path.write_text(content, encoding="utf-8")
        logger.info("generate_tables_complete", path=str(table_path))
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
