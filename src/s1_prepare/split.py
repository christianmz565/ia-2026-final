"""Split the dataset into train / val / test partitions.

Standalone usage:
    uv run python -m src.s1_prepare.split [--input-dir PATH] [--seed 42]
"""

from __future__ import annotations

import shutil
from pathlib import Path

import structlog
from sklearn.model_selection import train_test_split

from src.config import SplitConfig
from src.constants import RAW_DATASET, SPLIT_DATASET
from src.utils import find_image_label_pairs, resolve_labels_dir

logger = structlog.get_logger(__name__)


def split_dataset(
    config: SplitConfig | None = None,
    input_dir: Path | str | None = None,
    output_dir: Path | str | None = None,
) -> Path:
    """Split dataset images into train/val/test folders preserving YOLO labels.

    Args:
        config: Split configuration with ratios and seed.
        input_dir: Directory with images/ and labels/ sub-dirs.
        output_dir: Root output directory for splits.

    Returns:
        Path to the split output root.
    """
    config = config or SplitConfig()
    input_dir = Path(input_dir or RAW_DATASET)
    output_dir = Path(output_dir or SPLIT_DATASET)

    labels_dir = resolve_labels_dir(input_dir)
    pairs = find_image_label_pairs(input_dir)
    if not pairs:
        raise FileNotFoundError(f"No images found in {input_dir}")

    image_files = [p[0] for p in pairs]
    logger.info("splitting_dataset", total_images=len(image_files), seed=config.seed)

    train_ratio = config.ratios.get("train", 0.7)
    val_ratio = config.ratios.get("val", 0.15)
    test_ratio = config.ratios.get("test", 0.15)
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6, "Ratios must sum to 1.0"

    train_files, temp_files = train_test_split(
        image_files,
        train_size=train_ratio,
        random_state=config.seed,
    )

    relative_val = val_ratio / (val_ratio + test_ratio)
    val_files, test_files = train_test_split(
        temp_files,
        train_size=relative_val,
        random_state=config.seed,
    )

    splits = {"train": train_files, "val": val_files, "test": test_files}

    for split_name, files in splits.items():
        split_images = output_dir / split_name / "images"
        split_labels = output_dir / split_name / "labels"
        split_images.mkdir(parents=True, exist_ok=True)
        split_labels.mkdir(parents=True, exist_ok=True)

        for img_path in files:
            shutil.copy2(img_path, split_images / img_path.name)
            label_path = labels_dir / img_path.with_suffix(".txt").name
            if not label_path.exists():
                label_path = labels_dir / img_path.parent.name / img_path.with_suffix(".txt").name
            if label_path.exists():
                shutil.copy2(label_path, split_labels / label_path.with_suffix(".txt").name)

        logger.info("split_complete", split=split_name, count=len(files))

    return output_dir


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=SplitConfig,
        run_fn=lambda cfg: split_dataset(cfg),
        description="Split dataset into train/val/test",
        skip_fields=["stratify_by_class"],
    )
