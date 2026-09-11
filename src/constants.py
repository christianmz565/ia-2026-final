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
    "Quartzity",
    "Live_Knot",
    "Marrow",
    "resin",
    "Dead_Knot",
    "knot_with_crack",
    "Knot_missing",
    "Crack",
]

NUM_CLASSES = len(CLASS_NAMES)

CLASS_TO_ID: dict[str, int] = {name: idx for idx, name in enumerate(CLASS_NAMES)}
ID_TO_CLASS: dict[int, str] = {idx: name for name, idx in CLASS_TO_ID.items()}

TRAIN_SPLIT = "train"
VALID_SPLIT = "valid"
TEST_SPLIT = "test"

SPLITS: list[str] = [TRAIN_SPLIT, VALID_SPLIT, TEST_SPLIT]

DEFAULT_SPLIT_RATIOS: dict[str, float] = {
    TRAIN_SPLIT: 0.80,
    TEST_SPLIT: 0.10,
    VALID_SPLIT: 0.10,
}

DEFAULT_SEED = 42

TARGET_IMG_WIDTH = 960
TARGET_IMG_HEIGHT = 384

# Effective-number class weights (Cui et al., beta=0.999, mean=1.0)
CLASS_WEIGHTS_LIST: list[float] = [1.7229, 0.2756, 1.4546, 0.5666, 0.2861, 0.6472, 2.3761, 0.6708]
CLASS_WEIGHTS: dict[str, float] = {CLASS_NAMES[i]: CLASS_WEIGHTS_LIST[i] for i in range(NUM_CLASSES)}

# Majority classes (Live_Knot and Dead_Knot, accounting for ~77% of labels)
MAJORITY_CLASS_IDS: set[int] = {1, 4}

# Label filtering parameters post-downscaling
MIN_ABSOLUTE_DIM_PX = 2.0
MIN_LABEL_AREA_PX = 12.0
MIN_ELONGATED_DIM_PX = 6.0

# Preprocessing & Split balancing
DEFAULT_MAJORITY_DOWNSAMPLE_RATIO = 0.35

# Training defaults
DEFAULT_CASCADE_EPOCHS = 24
DEFAULT_YOLO_EPOCHS = 100
DEFAULT_RFDETR_EPOCHS = 50
DEFAULT_PATIENCE = 15
DEFAULT_RFDETR_LR = 1e-4
DEFAULT_CASCADE_LR = 1e-4

# Inference & Evaluation
DEFAULT_CONF_THRESHOLD = 0.001
