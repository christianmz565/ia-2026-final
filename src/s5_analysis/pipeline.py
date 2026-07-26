"""s5_analysis pipeline — aggregate -> figures.

Standalone usage:
    uv run python -m src.s5_analysis.pipeline
"""

from __future__ import annotations

import structlog

from src.config import S5Config
from src.constants import S4_OUTPUT, S5_OUTPUT
from src.s5_analysis.aggregate import aggregate_results
from src.s5_analysis.figures import generate_figures

logger = structlog.get_logger(__name__)


def run_pipeline(config: S5Config | None = None) -> None:
    """Run the analysis pipeline: aggregate results and generate comparison figures.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S5Config()

    logger.info("s5_pipeline_start")

    aggregated_path = S5_OUTPUT / "aggregated.json"
    aggregated = aggregate_results(
        results_dir=config.results_dir or S4_OUTPUT,
        output_path=aggregated_path,
        force=True,
    )

    figures_dir = S5_OUTPUT / "figures"
    generate_figures(
        aggregated=aggregated if isinstance(aggregated, dict) else {},
        output_dir=figures_dir,
        config=config.analysis,
        force=True,
    )

    logger.info("s5_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S5Config,
        run_fn=run_pipeline,
        description="s5_analysis pipeline",
        skip_fields=["analysis", "results_dir"],
    )
