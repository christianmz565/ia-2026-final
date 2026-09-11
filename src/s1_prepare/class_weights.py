"""Effective-number class weights (Cui et al., 2019) recomputed from a data split.

Replaces the frozen ``CLASS_WEIGHTS_LIST`` snapshot in ``src/constants.py`` with
weights derived from the actual training split before a rerun.

Standalone usage:
    uv run python -m src.s1_prepare.class_weights [--data-dir PATH] [--split train]
"""

from __future__ import annotations

import json
from pathlib import Path

import structlog
from pydantic import BaseModel, Field

from src.constants import CLASS_NAMES, NUM_CLASSES
from src.utils import read_yolo_labels

logger = structlog.get_logger(__name__)

EFFECTIVE_NUMBER_BETA = 0.999


def compute_class_weights(
    data_dir: Path | str,
    split: str = "train",
    beta: float = EFFECTIVE_NUMBER_BETA,
) -> list[float]:
    """Compute normalized effective-number weights from one split's labels.

    Weight per class is ``(1 - beta) / (1 - beta**n)`` normalized to mean 1.0.
    Classes with zero samples raise instead of receiving a fabricated weight.
    """
    labels_dir = Path(data_dir) / split / "labels"
    if not labels_dir.exists():
        raise FileNotFoundError(f"Labels directory not found: {labels_dir}")
    counts = [0] * NUM_CLASSES
    files = sorted(labels_dir.glob("*.txt"))
    if not files:
        raise FileNotFoundError(f"No label files found in {labels_dir}")
    for label_path in files:
        for box in read_yolo_labels(label_path):
            if not 0 <= box.class_id < NUM_CLASSES:
                raise ValueError(f"class_id {box.class_id} out of range in {label_path}")
            counts[box.class_id] += 1
    empty = [CLASS_NAMES[i] for i, n in enumerate(counts) if n == 0]
    if empty:
        raise ValueError(f"Cannot weight classes with zero samples: {empty}")
    raw = [(1.0 - beta) / (1.0 - beta**n) for n in counts]
    mean = sum(raw) / len(raw)
    weights = [round(w / mean, 4) for w in raw]
    logger.info("class_weights_computed", split=split, counts=dict(zip(CLASS_NAMES, counts, strict=True)), weights=weights)
    return weights


class ClassWeightsConfig(BaseModel):
    """Configuration for class-weight recomputation."""

    data_dir: str = Field(default="", description="Split root (defaults to SPLIT_DATASET)")
    split: str = Field(default="train", description="Split to count")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.constants import SPLIT_DATASET

    def _run(cfg: ClassWeightsConfig) -> None:
        weights = compute_class_weights(cfg.data_dir or SPLIT_DATASET, split=cfg.split)
        print(json.dumps({"CLASS_WEIGHTS_LIST": weights}, indent=2))

    standalone_main(
        config_model=ClassWeightsConfig,
        run_fn=_run,
        description="Recompute effective-number class weights from a split",
    )
