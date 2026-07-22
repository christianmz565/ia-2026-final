"""s4_evaluate pipeline — runs inference -> metrics -> export for all model/aug combos.

Standalone usage:
    uv run python -m src.s4_evaluate.pipeline
"""

from __future__ import annotations

import structlog

from src.config import S4Config

logger = structlog.get_logger(__name__)


def run_pipeline(config: S4Config | None = None) -> None:
    """Evaluate all trained models on all augmented test sets.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S4Config()

    logger.info("s4_pipeline_start")

    # TODO: iterate over s3_train outputs x s2_augments splits
    # For each combo: inference -> metrics -> export

    logger.info("s4_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S4Config,
        run_fn=run_pipeline,
        description="s4_evaluate pipeline",
        skip_fields=["eval"],
    )
