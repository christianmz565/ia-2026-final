"""s5_analysis pipeline — aggregate -> tables -> figures.

Standalone usage:
    uv run python -m src.s5_analysis.pipeline
"""

from __future__ import annotations

import structlog

from src.config import S5Config
from src.s5_analysis.aggregate import aggregate_results
from src.s5_analysis.figures import generate_figures
from src.s5_analysis.tables import generate_tables

logger = structlog.get_logger(__name__)


def run_pipeline(config: S5Config | None = None) -> None:
    """Run the analysis pipeline: aggregate, generate tables, generate figures.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S5Config()

    logger.info("s5_pipeline_start")

    logger.info("s5_step", step="aggregate")
    aggregated = aggregate_results()

    logger.info("s5_step", step="tables")
    generate_tables(aggregated, fmt=config.analysis.output_format)

    logger.info("s5_step", step="figures")
    generate_figures(aggregated, config=config.analysis)

    logger.info("s5_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S5Config,
        run_fn=run_pipeline,
        description="s5_analysis pipeline",
        skip_fields=["analysis", "results_dir"],
    )
