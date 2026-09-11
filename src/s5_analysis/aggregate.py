"""Aggregate evaluation results from s4_evaluate into unified DataFrames.

Also enriches each row with training metadata from s3_train (total time,
epochs, best-epoch metrics) and per-epoch history for training curve figures.

Standalone usage:
    uv run python -m src.s5_analysis.aggregate [--results-dir PATH]
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import structlog

from src.caching import config_fingerprint, run_cached_step
from src.constants import S3_OUTPUT, S4_OUTPUT, S5_OUTPUT

logger = structlog.get_logger(__name__)


def _load_training_meta(model: str, aug: str) -> dict[str, Any]:
    """Load summary_report.json and history.json from s3_train for one combo.

    Wall-clock/epoch-count scalars come from the summary report; best-mAP
    fields come from the history-derived best epoch (per-epoch data wins).
    Absent files or keys stay absent, never zero-filled.
    """
    base = S3_OUTPUT / model / aug
    meta: dict[str, Any] = {}

    sr_path = base / "summary_report.json"
    if sr_path.exists():
        try:
            sr = json.loads(sr_path.read_text())
            for key, sr_key, conv in (
                ("train_total_seconds", "total_elapsed_seconds", float),
                ("train_total_hours", "total_elapsed_hours", float),
                ("train_epochs_completed", "epochs_completed", int),
                ("train_avg_epoch_sec", "average_epoch_time_seconds", float),
            ):
                if sr_key in sr:
                    meta[key] = conv(sr[sr_key])
        except Exception as err:
            logger.warning("failed_to_load_summary_report", model=model, aug=aug, error=str(err))

    hist_path = base / "history.json"
    history: list[dict[str, Any]] = []
    if hist_path.exists():
        try:
            history = json.loads(hist_path.read_text())
            # Derive best epoch metrics from history as ground truth
            if history:
                best = max(history, key=lambda e: e["val_mAP_50_95"])
                meta["train_best_epoch"] = int(best["epoch"])
                if "val_mAP_50" in best:
                    meta["train_best_val_mAP_50"] = float(best["val_mAP_50"])
                if "val_mAP_50_95" in best:
                    meta["train_best_val_mAP_50_95"] = float(best["val_mAP_50_95"])
                if "val_per_class_mAP" in best:
                    meta["train_best_val_per_class_mAP"] = best["val_per_class_mAP"]
        except Exception as err:
            logger.warning("failed_to_load_history", model=model, aug=aug, error=str(err))

    return meta, history


def aggregate_results(
    results_dir: Path | str | None = None,
    output_path: Path | str | None = None,
    force: bool = False,
) -> dict[str, Any]:
    """Load all result JSONs from s4_evaluate and join with s3_train metadata.

    Args:
        results_dir: Directory containing per-run result JSONs (defaults to S4_OUTPUT).
        output_path: Where to write the aggregated comparison JSON.
        force: If True, bypass cache and re-aggregate results.

    Returns:
        Dict with keys:
        - ``rows``: list of enriched result dicts (one per model×augmentation)
        - ``columns``: list of column names in rows[0]
        - ``history``: dict of ``"{model}/{aug}"`` → list of epoch dicts
    """
    resolved_input = Path(results_dir or S4_OUTPUT)
    resolved_output = Path(output_path or S5_OUTPUT / "aggregated.json")

    def _aggregate() -> dict[str, Any]:
        result_files = sorted(resolved_input.rglob("results.json"))
        if not result_files:
            raise FileNotFoundError(f"No results.json files found under {resolved_input}")
        logger.info("aggregating_results", count=len(result_files), directory=str(resolved_input))

        rows: list[dict[str, Any]] = []
        history: dict[str, list[dict[str, Any]]] = {}

        for rf in result_files:
            with open(rf) as f:
                data = json.load(f)

            data["_source_file"] = str(rf.relative_to(resolved_input))

            # Infer model/augmentation from directory structure if missing
            if "model" not in data or not data["model"]:
                logger.warning("inferring_model_from_directory", file=str(rf))
                data["model"] = (
                    rf.parent.parent.name
                    if rf.parent != resolved_input and rf.parent.parent != resolved_input
                    else "N/A"
                )
            if "augmentation" not in data or not data["augmentation"]:
                logger.warning("inferring_augmentation_from_directory", file=str(rf))
                data["augmentation"] = rf.parent.name if rf.parent != resolved_input else "baseline"

            model = data["model"]
            aug = data["augmentation"]

            # Join training metadata from s3_train
            train_meta, epoch_history = _load_training_meta(model, aug)
            data.update(train_meta)

            if epoch_history:
                history[f"{model}/{aug}"] = epoch_history

            rows.append(data)

        aggregated: dict[str, Any] = {
            "rows": rows,
            "columns": list(rows[0].keys()) if rows else [],
            "history": history,
        }

        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        with open(resolved_output, "w") as f:
            json.dump(aggregated, f, indent=2, default=str)

        logger.info("aggregation_complete", rows=len(rows), history_keys=list(history.keys()))
        return aggregated

    return run_cached_step(
        step_name="aggregate",
        target_path=resolved_output,
        fn=_aggregate,
        force=force,
        loader=lambda p: json.loads(p.read_text()),
        fingerprint=config_fingerprint({"results_dir": str(resolved_input)}),
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import S5Config

    standalone_main(
        config_model=S5Config,
        run_fn=lambda cfg: aggregate_results(cfg.results_dir or S4_OUTPUT, None),
        description="Aggregate evaluation results",
        skip_fields=["analysis"],
    )
