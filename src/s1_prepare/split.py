"""Split dataset into train / test / val partitions using Greedy Iterative Stratified Sampling.

Standalone usage:
    uv run python -m src.s1_prepare.split [--input-dir PATH] [--seed 42]
"""

from __future__ import annotations

import random
import shutil
from pathlib import Path

import numpy as np
import structlog
from tqdm import tqdm

from src.config import SplitConfig
from src.constants import CLASS_NAMES, PROCESSED_DATASET, RAW_DATASET, SPLIT_DATASET
from src.utils import find_image_label_pairs, read_yolo_labels

logger = structlog.get_logger(__name__)


def greedy_iterative_stratified_split(
    pairs: list[tuple[Path, Path]],
    ratios: dict[str, float],
    seed: int = 42,
) -> dict[str, list[tuple[Path, Path]]]:
    """Partition image-label pairs into splits using Greedy Iterative Stratified Sampling.

    Ensures small/rare classes are preserved proportionally in every split.

    Args:
        pairs: List of (image_path, label_path) tuples.
        ratios: Dict of split names to target proportions (e.g. {'train': 0.8, 'test': 0.1, 'val': 0.1}).
        seed: Random seed for deterministic tie-breaking.

    Returns:
        Dict mapping split names to lists of (image_path, label_path) tuples.
    """
    rng = random.Random(seed)
    n_samples = len(pairs)
    n_classes = len(CLASS_NAMES)

    # Construct label matrix Y (n_samples x n_classes)
    Y = np.zeros((n_samples, n_classes), dtype=int)
    for idx, (_, label_path) in enumerate(pairs):
        boxes = read_yolo_labels(label_path)
        for b in boxes:
            if 0 <= b.class_id < n_classes:
                Y[idx, b.class_id] += 1

    split_names = list(ratios.keys())
    split_ratios = np.array([ratios[s] for s in split_names], dtype=float)

    class_totals = Y.sum(axis=0)
    target_class_counts = np.outer(split_ratios, class_totals)
    target_sample_counts = split_ratios * n_samples

    current_class_counts = np.zeros((len(split_names), n_classes), dtype=float)
    current_sample_counts = np.zeros(len(split_names), dtype=int)
    assignments: dict[int, str] = {}

    unassigned = set(range(n_samples))

    # Process samples containing bounding boxes
    while True:
        labeled_unassigned = [i for i in unassigned if Y[i].sum() > 0]
        if not labeled_unassigned:
            break

        rem_Y = Y[labeled_unassigned]
        rem_class_totals = rem_Y.sum(axis=0)
        pos_classes = np.where(rem_class_totals > 0)[0]
        if len(pos_classes) == 0:
            break

        # Pick rarest class among remaining labeled samples
        rarest_class = int(pos_classes[np.argmin(rem_class_totals[pos_classes])])

        candidate_indices = [i for i in labeled_unassigned if Y[i, rarest_class] > 0]
        # Sort candidates deterministically (highest rarest class count, total count, index)
        candidate_indices.sort(key=lambda i: (-Y[i, rarest_class], -Y[i].sum(), i))

        for i in candidate_indices:
            if i not in unassigned:
                continue

            sample_labels = Y[i]
            present_classes = np.where(sample_labels > 0)[0]

            best_split_idx = -1
            best_tuple = (-float("inf"), -float("inf"), -float("inf"))

            split_indices = list(range(len(split_names)))
            rng.shuffle(split_indices)

            for s_idx in split_indices:
                # 1. Deficit ratio for rarest class
                c_target = target_class_counts[s_idx, rarest_class]
                c_curr = current_class_counts[s_idx, rarest_class]
                rarest_deficit_ratio = (c_target - c_curr) / max(c_target, 1.0)

                # 2. Mean deficit ratio for all present classes in sample
                deficits = [
                    (target_class_counts[s_idx, c] - current_class_counts[s_idx, c])
                    / max(target_class_counts[s_idx, c], 1.0)
                    for c in present_classes
                ]
                mean_deficit_ratio = float(np.mean(deficits))

                # 3. Sample count deficit ratio
                samp_target = target_sample_counts[s_idx]
                samp_curr = current_sample_counts[s_idx]
                samp_deficit_ratio = (samp_target - samp_curr) / max(samp_target, 1.0)

                tup = (rarest_deficit_ratio, mean_deficit_ratio, samp_deficit_ratio)
                if tup > best_tuple:
                    best_tuple = tup
                    best_split_idx = s_idx

            assignments[i] = split_names[best_split_idx]
            current_class_counts[best_split_idx] += sample_labels
            current_sample_counts[best_split_idx] += 1
            unassigned.remove(i)

    # Process remaining unlabeled samples
    remaining = list(unassigned)
    rng.shuffle(remaining)
    for i in remaining:
        split_indices = list(range(len(split_names)))
        split_indices.sort(
            key=lambda s_idx: (
                (target_sample_counts[s_idx] - current_sample_counts[s_idx]) / max(target_sample_counts[s_idx], 1.0)
            ),
            reverse=True,
        )
        best_split_idx = split_indices[0]
        assignments[i] = split_names[best_split_idx]
        current_sample_counts[best_split_idx] += 1

    # Map indices back to pairs
    result: dict[str, list[tuple[Path, Path]]] = {s: [] for s in split_names}
    for idx, pair in enumerate(pairs):
        split_name = assignments[idx]
        result[split_name].append(pair)

    return result


def split_dataset(
    config: SplitConfig | None = None,
    input_dir: Path | str | None = None,
    output_dir: Path | str | None = None,
) -> Path:
    """Split preprocessed dataset into train/test/val folders with greedy iterative stratification.

    Args:
        config: Split configuration with ratios and seed.
        input_dir: Directory with preprocessed images/ and labels/ sub-dirs.
        output_dir: Root output directory for splits.

    Returns:
        Path to the split output root.
    """
    config = config or SplitConfig()
    resolved_input = Path(input_dir) if input_dir else PROCESSED_DATASET if PROCESSED_DATASET.exists() else RAW_DATASET

    output_dir = Path(output_dir or SPLIT_DATASET)

    pairs = find_image_label_pairs(resolved_input)
    if not pairs:
        raise FileNotFoundError(f"No images found in {resolved_input}")

    logger.info(
        "splitting_dataset",
        total_images=len(pairs),
        ratios=config.ratios,
        seed=config.seed,
        input_dir=str(resolved_input),
    )

    ratio_sum = sum(config.ratios.values())
    assert abs(ratio_sum - 1.0) < 1e-6, f"Ratios must sum to 1.0, got {ratio_sum}"

    split_pairs = greedy_iterative_stratified_split(
        pairs=pairs,
        ratios=config.ratios,
        seed=config.seed,
    )

    for split_name, s_pairs in split_pairs.items():
        split_images = output_dir / split_name / "images"
        split_labels = output_dir / split_name / "labels"
        split_images.mkdir(parents=True, exist_ok=True)
        split_labels.mkdir(parents=True, exist_ok=True)

        for img_path, label_path in tqdm(s_pairs, desc=f"Writing {split_name} split", unit="img"):
            shutil.copy2(img_path, split_images / img_path.name)
            if label_path.exists():
                shutil.copy2(label_path, split_labels / img_path.with_suffix(".txt").name)
            else:
                # Ensure empty label file exists if no defect
                (split_labels / img_path.with_suffix(".txt").name).touch()

        logger.info("split_complete", split=split_name, count=len(s_pairs))

    return output_dir


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=SplitConfig,
        run_fn=lambda cfg: split_dataset(cfg),
        description="Split dataset into train/test/val using greedy iterative stratification",
        skip_fields=["stratify_by_class"],
    )
