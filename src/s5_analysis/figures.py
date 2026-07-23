"""Generate comparison figures (charts, heatmaps) from aggregated results.

Standalone usage:
    uv run python -m src.s5_analysis.figures [--input PATH] [--figure-dpi 300]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib
import matplotlib.pyplot as plt
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
    matplotlib.use(config.figure_backend or "Agg")

    resolved_output_dir = Path(output_dir or S5_OUTPUT / "figures")
    fig_path = resolved_output_dir / "map_comparison.png"

    def _do_generate() -> list[Path]:
        resolved_output_dir.mkdir(parents=True, exist_ok=True)
        rows = aggregated.get("rows", [])
        logger.info(
            "generate_figures_start",
            rows=len(rows),
            dpi=config.figure_dpi,
            output=str(resolved_output_dir),
        )

        labels: list[str] = []
        map50_scores: list[float] = []
        map50_95_scores: list[float] = []

        for r in rows:
            lbl = f"{r.get('model', 'N/A')} ({r.get('augmentation', 'baseline')})"
            labels.append(lbl)
            map50_scores.append(float(r.get("mAP_50", 0.0)))
            map50_95_scores.append(float(r.get("mAP_50_95", 0.0)))

        fig, ax = plt.subplots(figsize=(10, 6))
        if labels:
            x = range(len(labels))
            width = 0.35
            ax.bar([i - width / 2 for i in x], map50_scores, width, label="mAP@50")
            ax.bar([i + width / 2 for i in x], map50_95_scores, width, label="mAP@50:95")
            ax.set_xticks(list(x))
            ax.set_xticklabels(labels, rotation=45, ha="right")
        else:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center")

        ax.set_ylabel("mAP Score")
        ax.set_title("Wood Defect Detection Model Benchmark")
        ax.set_ylim(0, 1.0)
        ax.legend()
        plt.tight_layout()

        fig.savefig(fig_path, dpi=config.figure_dpi)
        plt.close(fig)

        marker = resolved_output_dir / ".figures_generated"
        marker.touch()

        logger.info("generate_figures_complete", figure=str(fig_path))
        return [fig_path, marker]

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
