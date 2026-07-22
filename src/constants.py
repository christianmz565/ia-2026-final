"""Centralized constants for paths, dataset metadata, and shared values."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PARTIALS_DIR = PROJECT_ROOT / "partials"

S1_OUTPUT = PARTIALS_DIR / "s1_prepare"
S2_OUTPUT = PARTIALS_DIR / "s2_augments"
S3_OUTPUT = PARTIALS_DIR / "s3_train"
S4_OUTPUT = PARTIALS_DIR / "s4_evaluate"
S5_OUTPUT = PARTIALS_DIR / "s5_analysis"

RAW_DATASET = S1_OUTPUT / "raw"
PROCESSED_DATASET = S1_OUTPUT / "processed"
SPLIT_DATASET = S1_OUTPUT / "split"

AUGMENTED_DIR = S2_OUTPUT / "augmented"


KAGGLE_DATASET = "nomihsa965/large-scale-image-dataset-of-wood-surface-defects"

CLASS_NAMES: list[str] = [
    "Live_Knot",
    "Dead_Knot",
    "resin",
    "knot_with_crack",
    "Crack",
    "Marrow",
    "Quartzity",
    "Knot_missing",
]

NUM_CLASSES = len(CLASS_NAMES)

CLASS_TO_ID: dict[str, int] = {name: idx for idx, name in enumerate(CLASS_NAMES)}
ID_TO_CLASS: dict[int, str] = {idx: name for name, idx in CLASS_TO_ID.items()}


DEFAULT_SPLIT_RATIOS: dict[str, float] = {
    "train": 0.80,
    "test": 0.10,
    "val": 0.10,
}

DEFAULT_SEED = 42
