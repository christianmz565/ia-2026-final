"""Generate paper-ready comparison figures (Seaborn + XITS font) from aggregated results.

Standalone usage:
    uv run python -m src.s5_analysis.figures [--input PATH] [--figure-dpi 300]
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import matplotlib
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import structlog

from src.caching import run_cached_step
from src.config import AnalysisConfig
from src.constants import S5_OUTPUT

logger = structlog.get_logger(__name__)

MODEL_LABELS = {
    "rf_detr": "RF-DETR",
    "cascade_rcnn": "Cascade R-CNN",
    "yolo26": "YOLO26",
}

AUG_LABELS = {
    "baseline": "Baseline",
    "albumentations_balanced": "Albumentations",
    "boxaug_standard": "BoxAug Std",
    "boxaug_libcom": "BoxAug LibCom",
}


def _setup_style() -> None:
    """Set seaborn theme and attempt to load XITS font."""
    sns.set_theme(style="whitegrid")
    try:
        font_path = subprocess.check_output(["fc-match", "-f", "%{file}", "XITS"]).decode().strip()
        font_manager.fontManager.addfont(font_path)
        plt.rcParams["font.family"] = "XITS"
    except Exception as e:
        logger.debug("font_xits_not_loaded", error=str(e))


def _save_fig(fig: plt.Figure, output_dir: Path, stem: str, dpi: int = 300) -> list[Path]:
    """Save figure as both SVG and PNG."""
    output_dir.mkdir(parents=True, exist_ok=True)
    svg_out = output_dir / f"{stem}.svg"
    png_out = output_dir / f"{stem}.png"
    fig.savefig(svg_out, bbox_inches="tight")
    fig.savefig(png_out, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return [svg_out, png_out]


# --- Group A: Accuracy Overview ---

def _fig_map_overview(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 1: mAP@50 and mAP@50:95 comparison across model/augmentation combos."""
    data = []
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        data.append({"Combo": label, "Metric": "mAP@50", "Score": float(r.get("mAP_50", 0.0))})
        data.append({"Combo": label, "Metric": "mAP@50:95", "Score": float(r.get("mAP_50_95", 0.0))})

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    if not df.empty:
        sns.barplot(data=df, x="Score", y="Combo", hue="Metric", palette="muted", ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt="%.3f", padding=3, fontsize=9)
        ax.set_xlim(0, 1.0)
    else:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")

    ax.set_xlabel("mAP Score", fontsize=10)
    ax.set_ylabel("")
    ax.set_title("Detection Performance Overview (mAP@50 & mAP@50:95)", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "map_overview", dpi)


def _fig_precision_recall_f1(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 2: Precision, Recall, and F1 per model."""
    data = []
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        data.append({"Model": label, "Metric": "Precision", "Score": float(r.get("precision", 0.0))})
        data.append({"Model": label, "Metric": "Recall", "Score": float(r.get("recall", 0.0))})
        data.append({"Model": label, "Metric": "F1", "Score": float(r.get("f1", 0.0))})

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    if not df.empty:
        sns.barplot(data=df, x="Model", y="Score", hue="Metric", palette="Set2", ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt="%.3f", padding=3, fontsize=9)
        ax.set_ylim(0, 1.0)
    else:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")

    ax.set_ylabel("Score", fontsize=10)
    ax.set_xlabel("")
    ax.set_title("Precision, Recall, and F1 Score by Model", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "precision_recall_f1", dpi)


# --- Group B: Augmentation x Paradigm Matrix ---

def _fig_aug_paradigm_heatmap(
    rows: list[dict[str, Any]], metric_key: str, title: str, stem: str, cmap: str, output_dir: Path, dpi: int
) -> list[Path]:
    """Figures 3 & 4: Model x Augmentation heatmap for a given metric."""
    grid_data: dict[str, dict[str, float]] = {}
    for r in rows:
        m = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", "N/A"))
        if m not in grid_data:
            grid_data[m] = {}
        grid_data[m][a] = float(r.get(metric_key, 0.0))

    df = pd.DataFrame(grid_data).T
    fig, ax = plt.subplots(figsize=(7, 4))
    if not df.empty:
        sns.heatmap(df, annot=True, fmt=".3f", cmap=cmap, cbar=True, ax=ax, linewidths=0.5)
        ax.set_ylabel("Model Architecture", fontsize=10)
        ax.set_xlabel("Augmentation Strategy", fontsize=10)
    else:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")

    ax.set_title(title, fontsize=12)
    plt.tight_layout()
    return _save_fig(fig, output_dir, stem, dpi)


def _fig_aug_effect_per_model(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 5: Augmentation effect per model architecture."""
    data = []
    for r in rows:
        data.append({
            "Model": MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A")),
            "Augmentation": AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", "N/A")),
            "mAP_50": float(r.get("mAP_50", 0.0)),
        })

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    if not df.empty:
        sns.barplot(data=df, x="Augmentation", y="mAP_50", hue="Model", palette="muted", ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt="%.3f", padding=3, fontsize=9)
        ax.set_ylim(0, 1.0)
    else:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")

    ax.set_ylabel("mAP@50", fontsize=10)
    ax.set_xlabel("Augmentation Strategy", fontsize=10)
    ax.set_title("Effect of Augmentation Strategy per Paradigm (mAP@50)", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "aug_effect_per_model", dpi)


def _fig_aug_delta_vs_baseline(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 6: Delta mAP@50 vs baseline for each augmentation."""
    baselines: dict[str, float] = {}
    for r in rows:
        if r.get("augmentation") == "baseline":
            baselines[r.get("model", "")] = float(r.get("mAP_50", 0.0))

    data = []
    for r in rows:
        m = r.get("model", "")
        aug = r.get("augmentation", "")
        if aug != "baseline" and m in baselines:
            delta = float(r.get("mAP_50", 0.0)) - baselines[m]
            data.append({
                "Model": MODEL_LABELS.get(m, m),
                "Augmentation": AUG_LABELS.get(aug, aug),
                "Delta_mAP_50": delta,
            })

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    if not df.empty:
        sns.barplot(data=df, x="Delta_mAP_50", y="Augmentation", hue="Model", palette="coolwarm", ax=ax)
        ax.axvline(0, color="black", linestyle="--", linewidth=0.8)
        for container in ax.containers:
            ax.bar_label(container, fmt="%+.3f", padding=3, fontsize=9)
    else:
        ax.text(0.5, 0.5, "No multi-augmentation data available vs baseline", ha="center", va="center")

    ax.set_xlabel("Δ mAP@50 (vs Baseline)", fontsize=10)
    ax.set_ylabel("")
    ax.set_title("Augmentation Impact Relative to Baseline (Δ mAP@50)", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "aug_delta_vs_baseline", dpi)


# --- Group C: Per-Class Performance ---

def _fig_per_class_ap_heatmap(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 7: Per-class AP heatmap across models."""
    class_map: dict[str, dict[str, float]] = {}
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        per_class = r.get("per_class_ap", {})
        if per_class:
            class_map[label] = {cls: float(val) for cls, val in per_class.items()}

    df = pd.DataFrame(class_map).T
    fig, ax = plt.subplots(figsize=(9, 4.5))
    if not df.empty:
        sns.heatmap(df, annot=True, fmt=".3f", cmap="YlGnBu", cbar=True, ax=ax, linewidths=0.5)
        ax.set_ylabel("Model / Augmentation", fontsize=10)
        ax.set_xlabel("Defect Class", fontsize=10)
        plt.xticks(rotation=35, ha="right")
    else:
        ax.text(0.5, 0.5, "No per-class AP data available", ha="center", va="center")

    ax.set_title("Per-Class Average Precision (AP@50:95) Heatmap", fontsize=12)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "per_class_ap_heatmap", dpi)


def _fig_per_class_ap_bars(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 8: Horizontal bar chart for per-class AP."""
    data = []
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        for cls, val in r.get("per_class_ap", {}).items():
            data.append({"Model": label, "Class": cls, "AP": float(val)})

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(9, 6))
    if not df.empty:
        sns.barplot(data=df, x="AP", y="Class", hue="Model", palette="tab10", ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt="%.2f", padding=3, fontsize=8)
        ax.set_xlim(0, 1.0)
    else:
        ax.text(0.5, 0.5, "No per-class AP data available", ha="center", va="center")

    ax.set_xlabel("Average Precision (AP@50:95)", fontsize=10)
    ax.set_ylabel("")
    ax.set_title("Per-Class Detection Performance Across Models", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "per_class_ap_bars", dpi)


# --- Group D: Training Dynamics ---

def _fig_training_curves_map(history: dict[str, list[dict[str, Any]]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 9: Validation mAP@50 over epochs for all runs."""
    data = []
    for key, epochs in history.items():
        parts = key.split("/")
        m = MODEL_LABELS.get(parts[0], parts[0])
        a = AUG_LABELS.get(parts[1], parts[1]) if len(parts) > 1 else ""
        label = f"{m} ({a})" if a else m
        for ep in epochs:
            data.append({
                "Run": label,
                "Epoch": int(ep.get("epoch", 0)),
                "val_mAP_50": float(ep.get("val_mAP_50", 0.0)),
            })

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    if not df.empty:
        sns.lineplot(data=df, x="Epoch", y="val_mAP_50", hue="Run", style="Run", markers=True, dashes=False, ax=ax)
        ax.set_ylim(0, 1.0)
    else:
        ax.text(0.5, 0.5, "No epoch history available", ha="center", va="center")

    ax.set_ylabel("Validation mAP@50", fontsize=10)
    ax.set_xlabel("Epoch", fontsize=10)
    ax.set_title("Validation Convergence Curves (mAP@50 over Epochs)", fontsize=12)
    sns.despine()
    plt.tight_layout()
    return _save_fig(fig, output_dir, "training_curves_map", dpi)


def _fig_training_curves_loss(history: dict[str, list[dict[str, Any]]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 10: Training loss over epochs (train_loss only)."""
    data = []
    for key, epochs in history.items():
        parts = key.split("/")
        m = MODEL_LABELS.get(parts[0], parts[0])
        a = AUG_LABELS.get(parts[1], parts[1]) if len(parts) > 1 else ""
        label = f"{m} ({a})" if a else m
        for ep in epochs:
            data.append({
                "Run": label,
                "Epoch": int(ep.get("epoch", 0)),
                "train_loss": float(ep.get("train_loss", 0.0)),
            })

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    if not df.empty:
        sns.lineplot(data=df, x="Epoch", y="train_loss", hue="Run", style="Run", markers=True, dashes=False, ax=ax)
    else:
        ax.text(0.5, 0.5, "No epoch loss history available", ha="center", va="center")

    ax.set_ylabel("Training Loss", fontsize=10)
    ax.set_xlabel("Epoch", fontsize=10)
    ax.set_title("Training Loss Progression over Epochs", fontsize=12)
    sns.despine()
    plt.tight_layout()
    return _save_fig(fig, output_dir, "training_curves_loss", dpi)


# --- Group E: Timing & Efficiency ---

def _fig_training_time_comparison(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 11: Total training duration in hours per model/augmentation."""
    data = []
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        data.append({"Combo": label, "Hours": float(r.get("train_total_hours", 0.0))})

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4))
    if not df.empty and df["Hours"].sum() > 0:
        sns.barplot(data=df, x="Hours", y="Combo", hue="Combo", palette="crest", legend=False, ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt="%.2fh", padding=3, fontsize=9)
    else:
        ax.text(0.5, 0.5, "No training time data available", ha="center", va="center")

    ax.set_xlabel("Total Training Time (Hours)", fontsize=10)
    ax.set_ylabel("")
    ax.set_title("Training Time Comparison Across Models", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "training_time_comparison", dpi)


def _fig_inference_time_comparison(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 12: Average inference latency in ms per image."""
    data = []
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        data.append({"Combo": label, "Latency_ms": float(r.get("avg_inference_ms", 0.0))})

    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4))
    if not df.empty and df["Latency_ms"].sum() > 0:
        sns.barplot(data=df, x="Latency_ms", y="Combo", hue="Combo", palette="viridis", legend=False, ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt="%.1f ms", padding=3, fontsize=9)
    else:
        ax.text(0.5, 0.5, "No inference timing data available", ha="center", va="center")

    ax.set_xlabel("Average Latency per Image (ms)", fontsize=10)
    ax.set_ylabel("")
    ax.set_title("Inference Speed Comparison (ms / Image)", fontsize=12)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return _save_fig(fig, output_dir, "inference_time_comparison", dpi)


def _fig_speed_accuracy_tradeoff(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 13: Scatter plot of mAP@50 vs inference latency."""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    has_data = False
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        x = float(r.get("avg_inference_ms", 0.0))
        y = float(r.get("mAP_50", 0.0))
        if x > 0 or y > 0:
            has_data = True
            ax.scatter(x, y, s=100, label=label)
            ax.annotate(label, (x, y), xytext=(5, 5), textcoords="offset points", fontsize=9)

    if not has_data:
        ax.text(0.5, 0.5, "No timing/accuracy trade-off data available", ha="center", va="center")

    ax.set_xlabel("Avg Inference Time per Image (ms)", fontsize=10)
    ax.set_ylabel("mAP@50 Score", fontsize=10)
    ax.set_title("Speed vs. Accuracy Trade-off", fontsize=12)
    ax.set_ylim(0, 1.0)
    sns.despine()
    plt.tight_layout()
    return _save_fig(fig, output_dir, "speed_accuracy_tradeoff", dpi)


def _fig_efficiency_tradeoff(rows: list[dict[str, Any]], output_dir: Path, dpi: int) -> list[Path]:
    """Figure 14: Scatter plot of mAP@50 vs total training hours."""
    fig, ax = plt.subplots(figsize=(7, 4.5))
    has_data = False
    for r in rows:
        m_lbl = MODEL_LABELS.get(r.get("model", ""), r.get("model", "N/A"))
        a_lbl = AUG_LABELS.get(r.get("augmentation", ""), r.get("augmentation", ""))
        label = f"{m_lbl} ({a_lbl})" if a_lbl else m_lbl
        x = float(r.get("train_total_hours", 0.0))
        y = float(r.get("mAP_50", 0.0))
        if x > 0 or y > 0:
            has_data = True
            ax.scatter(x, y, s=100, label=label)
            ax.annotate(label, (x, y), xytext=(5, 5), textcoords="offset points", fontsize=9)

    if not has_data:
        ax.text(0.5, 0.5, "No efficiency trade-off data available", ha="center", va="center")

    ax.set_xlabel("Total Training Time (Hours)", fontsize=10)
    ax.set_ylabel("mAP@50 Score", fontsize=10)
    ax.set_title("Training Cost vs. Accuracy Trade-off", fontsize=12)
    ax.set_ylim(0, 1.0)
    sns.despine()
    plt.tight_layout()
    return _save_fig(fig, output_dir, "efficiency_tradeoff", dpi)


# --- Public API ---

def generate_figures(
    aggregated: dict[str, Any],
    output_dir: Path | str | None = None,
    config: AnalysisConfig | None = None,
    force: bool = False,
) -> list[Path]:
    """Generate all 14 paper-ready comparison figures.

    Args:
        aggregated: Output of ``aggregate_results()``.
        output_dir: Where to write figure files.
        config: Analysis configuration (DPI, backend).
        force: If True, bypass cache and re-generate figures.

    Returns:
        List of paths to all generated figure files (SVG and PNG).
    """
    config = config or AnalysisConfig()
    matplotlib.use(config.figure_backend or "Agg")
    _setup_style()

    resolved_output_dir = Path(output_dir or S5_OUTPUT / "figures")

    def _do_generate() -> list[Path]:
        resolved_output_dir.mkdir(parents=True, exist_ok=True)
        rows = aggregated.get("rows", [])
        history = aggregated.get("history", {})

        logger.info(
            "generate_figures_start",
            rows=len(rows),
            history_keys=len(history),
            dpi=config.figure_dpi,
            output=str(resolved_output_dir),
        )

        all_paths: list[Path] = []

        # Group A: Accuracy Overview
        all_paths.extend(_fig_map_overview(rows, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_precision_recall_f1(rows, resolved_output_dir, config.figure_dpi))

        # Group B: Augmentation x Paradigm Matrix
        all_paths.extend(_fig_aug_paradigm_heatmap(rows, "mAP_50", "Augmentation x Paradigm (mAP@50)", "aug_paradigm_map50_heatmap", "YlGnBu", resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_aug_paradigm_heatmap(rows, "mAP_50_95", "Augmentation x Paradigm (mAP@50:95)", "aug_paradigm_map50_95_heatmap", "YlOrRd", resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_aug_effect_per_model(rows, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_aug_delta_vs_baseline(rows, resolved_output_dir, config.figure_dpi))

        # Group C: Per-Class Performance
        all_paths.extend(_fig_per_class_ap_heatmap(rows, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_per_class_ap_bars(rows, resolved_output_dir, config.figure_dpi))

        # Group D: Training Dynamics
        all_paths.extend(_fig_training_curves_map(history, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_training_curves_loss(history, resolved_output_dir, config.figure_dpi))

        # Group E: Timing & Efficiency
        all_paths.extend(_fig_training_time_comparison(rows, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_inference_time_comparison(rows, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_speed_accuracy_tradeoff(rows, resolved_output_dir, config.figure_dpi))
        all_paths.extend(_fig_efficiency_tradeoff(rows, resolved_output_dir, config.figure_dpi))

        marker = resolved_output_dir / ".figures_generated"
        marker.touch()
        all_paths.append(marker)

        logger.info("generate_figures_complete", count=len(all_paths))
        return all_paths

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
