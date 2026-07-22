"""Generate comparison figures (charts, heatmaps) from aggregated results.

Standalone usage:
    uv run python -m src.s5_analysis.figures [--input PATH] [--figure-dpi 300]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.config import AnalysisConfig
from src.constants import S5_OUTPUT

logger = structlog.get_logger(__name__)


def generate_figures(
    aggregated: dict[str, Any],
    output_dir: Path | str | None = None,
    config: AnalysisConfig | None = None,
    force: bool = False,
) -> list[Path]:
    """Generate comparison figures from aggregated results.

    Args:
        aggregated: Output of ``aggregate_results()``.
        output_dir: Where to write figure files.
        config: Analysis configuration (DPI, backend).
        force: If True, bypass cache and re-generate figures.

    Returns:
        List of paths to generated figure files.
    """
    config = config or AnalysisConfig()
    resolved_output_dir = Path(output_dir or S5_OUTPUT / "figures")

    def _do_generate() -> list[Path]:
        resolved_output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(
            "generate_figures_stub",
            rows=len(aggregated.get("rows", [])),
            dpi=config.figure_dpi,
            output=str(resolved_output_dir),
        )
        marker = resolved_output_dir / ".figures_generated"
        marker.touch()
        return [marker]

    res = run_cached_step(
        step_name="generate_figures",
        target_path=resolved_output_dir,
        fn=_do_generate,
        force=force,
    )
    return res if isinstance(res, list) else list(resolved_output_dir.glob("*"))


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=AnalysisConfig,
        run_fn=lambda cfg: generate_figures(
            json.loads(Path(cfg.input).read_text()) if cfg.input else {},
            config=cfg,
        ),
        description="Generate comparison figures",
        required_fields=["input"],
    )
