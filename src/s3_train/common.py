"""Common utilities and protocols for s3_train model trainers.

Enforces unified standards across all detection models:
- Structured output directory format (checkpoints/, history.json, summary_report.json, summary_report.md).
- Progress bar logging (tqdm).
- Mixed precision training defaults.
- Standardized periodic metrics (including per-class mAP) and checkpoint tracking.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog
from tqdm import tqdm

from src.constants import CLASS_NAMES

logger = structlog.get_logger(__name__)


def setup_training_output_dir(output_dir: Path | str) -> tuple[Path, Path]:
    """Create and return standardized output and checkpoints directories.

    Args:
        output_dir: Path to model run output directory.

    Returns:
        Tuple of (output_dir, checkpoints_dir).
    """
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    checkpoints_dir = out_path / "checkpoints"
    checkpoints_dir.mkdir(parents=True, exist_ok=True)
    return out_path, checkpoints_dir


def create_epoch_pbar(epochs: int, model_name: str) -> tqdm:
    """Create a standardized tqdm progress bar for epoch iterations.

    Args:
        epochs: Total number of epochs.
        model_name: Name of the model being trained.

    Returns:
        tqdm progress bar instance.
    """
    return tqdm(
        range(1, epochs + 1),
        desc=f"Training [{model_name}]",
        unit="epoch",
        dynamic_ncols=True,
    )


def format_per_class_map(raw_per_class: dict[str, float] | None = None) -> dict[str, float]:
    """Format and fill missing per-class mAP entries for all standard dataset classes.

    Args:
        raw_per_class: Dictionary of class name to mAP score.

    Returns:
        Clean dict containing entries for all CLASS_NAMES rounded to 4 decimals.
    """
    raw = raw_per_class or {}
    formatted: dict[str, float] = {}
    for name in CLASS_NAMES:
        val = raw.get(name, 0.0)
        formatted[name] = round(float(val), 4)
    return formatted


def save_epoch_history(output_dir: Path, history: list[dict[str, Any]]) -> Path:
    """Save training metric history incrementally to history.json.

    Args:
        output_dir: Output directory path.
        history: List of per-epoch metric dicts (including val_per_class_mAP).

    Returns:
        Path to history.json file.
    """
    history_file = output_dir / "history.json"
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)
    return history_file


def save_summary_reports(
    output_dir: Path,
    pipeline_name: str,
    total_time_sec: float,
    target_epochs: int,
    history: list[dict[str, Any]],
    best_checkpoint: Path,
) -> dict[str, Any]:
    """Generate standardized summary_report.json, summary_report.md, and ensure best.pt exists.

    Args:
        output_dir: Root output directory.
        pipeline_name: Descriptive name of the trainer pipeline.
        total_time_sec: Total training wall-clock time in seconds.
        target_epochs: Total planned epochs.
        history: Metric records per epoch.
        best_checkpoint: Path to best checkpoint file.

    Returns:
        Summary report dictionary.
    """
    best_mAP_50_95 = max((h.get("val_mAP_50_95", 0.0) for h in history), default=0.0)
    best_epoch_record = next(
        (h for h in history if h.get("val_mAP_50_95", 0.0) == best_mAP_50_95),
        history[-1] if history else {},
    )
    best_epoch = best_epoch_record.get("epoch", len(history))

    final_mAP_50 = history[-1].get("val_mAP_50", 0.0) if history else 0.0
    final_mAP_50_95 = history[-1].get("val_mAP_50_95", 0.0) if history else 0.0
    best_per_class_mAP = best_epoch_record.get("val_per_class_mAP", format_per_class_map())

    summary = {
        "pipeline_name": pipeline_name,
        "mixed_precision": True,
        "total_elapsed_seconds": total_time_sec,
        "total_elapsed_hours": total_time_sec / 3600.0,
        "epochs_completed": len(history) if history else target_epochs,
        "target_epochs": target_epochs,
        "average_epoch_time_seconds": total_time_sec / max(1, len(history) if history else target_epochs),
        "best_epoch": best_epoch,
        "final_val_mAP_50": final_mAP_50,
        "final_val_mAP_50_95": final_mAP_50_95,
        "best_val_mAP_50_95": best_mAP_50_95,
        "best_val_per_class_mAP": best_per_class_mAP,
        "best_checkpoint_path": str(best_checkpoint),
        "training_history": history,
    }

    report_json = output_dir / "summary_report.json"
    with open(report_json, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    per_class_rows = "\n".join(f"- **{cls}**: {score:.4f}" for cls, score in best_per_class_mAP.items())

    report_md = f"""# {pipeline_name} Training Summary Report

## 1. Overview
- **Pipeline:** {pipeline_name}
- **Mixed Precision (AMP):** Enabled
- **Total Elapsed Time:** {total_time_sec / 60.0:.2f} minutes ({total_time_sec / 3600.0:.2f} hours)
- **Epochs Completed:** {len(history)} / {target_epochs}

## 2. Performance Metrics
- **Best Epoch:** {best_epoch}
- **Best Validation $mAP_{{50:95}}$:** {best_mAP_50_95:.4f}
- **Final Validation $mAP_{{50}}$:** {final_mAP_50:.4f}
- **Final Validation $mAP_{{50:95}}$:** {final_mAP_50_95:.4f}

### Per-Class Validation mAP (Best Epoch {best_epoch})
{per_class_rows}

## 3. Artifacts
- **Output Directory:** `{output_dir}`
- **Best Checkpoint:** `{best_checkpoint}`
- **Metrics History:** `{output_dir / "history.json"}`
"""
    with open(output_dir / "summary_report.md", "w", encoding="utf-8") as f:
        f.write(report_md)

    best_pt = output_dir / "best.pt"
    if best_checkpoint.exists() and best_checkpoint.resolve() != best_pt.resolve():
        try:
            if best_pt.exists() or best_pt.is_symlink():
                best_pt.unlink()
            rel_target = best_checkpoint.name if best_checkpoint.parent == output_dir else best_checkpoint.relative_to(output_dir)
            best_pt.symlink_to(rel_target)
            logger.info("standardized_best_pt_created", source=str(rel_target), target=str(best_pt))
        except Exception as err:
            logger.warning("failed_to_symlink_best_pt", error=str(err))

    return summary

