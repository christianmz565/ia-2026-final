"""Explore the dataset: class distribution, bbox statistics, sample images.

Standalone usage:
    uv run python -m src.s1_prepare.explore [--input-dir PATH]
"""

from __future__ import annotations

from pathlib import Path

import structlog
from pydantic import BaseModel, Field
from tqdm import tqdm

from src.constants import CLASS_NAMES, ID_TO_CLASS, PROCESSED_DATASET, RAW_DATASET
from src.utils import find_image_label_pairs, read_yolo_labels

logger = structlog.get_logger(__name__)


def explore_dataset(input_dir: Path | str | None = None) -> dict[str, object]:
    """Compute dataset statistics from YOLO label files.

    Args:
        input_dir: Directory with images/ and labels/ sub-dirs.
                   Defaults to ``PROCESSED_DATASET`` if exists, else ``RAW_DATASET``.

    Returns:
        Dict with keys: total_images, total_annotations, class_counts,
        avg_boxes_per_image, bbox_stats.
    """
    resolved_input = Path(input_dir) if input_dir else PROCESSED_DATASET if PROCESSED_DATASET.exists() else RAW_DATASET

    pairs = find_image_label_pairs(resolved_input)
    logger.info("scanning_dataset", directory=str(resolved_input), count=len(pairs))

    class_counts: dict[str, int] = dict.fromkeys(CLASS_NAMES, 0)
    total_annotations = 0
    widths, heights, aspects, areas = [], [], [], []

    for _, label_path in tqdm(pairs, desc="Exploring dataset", unit="img"):
        bboxes = read_yolo_labels(label_path)
        total_annotations += len(bboxes)
        for b in bboxes:
            name = ID_TO_CLASS.get(b.class_id, f"unknown_{b.class_id}")
            class_counts[name] = class_counts.get(name, 0) + 1
            widths.append(b.w)
            heights.append(b.h)
            aspects.append(b.aspect_ratio())
            areas.append(b.area())

    stats: dict[str, object] = {
        "total_images": len(pairs),
        "total_annotations": total_annotations,
        "class_counts": class_counts,
        "avg_boxes_per_image": total_annotations / max(len(pairs), 1),
        "bbox_stats": {
            "mean_width": sum(widths) / max(len(widths), 1),
            "mean_height": sum(heights) / max(len(heights), 1),
            "mean_aspect_ratio": sum(aspects) / max(len(aspects), 1),
            "mean_area": sum(areas) / max(len(areas), 1),
        },
    }

    logger.info("dataset_stats", **{k: v for k, v in stats.items() if k != "class_counts"})
    for cls, cnt in class_counts.items():
        logger.info("class_distribution", className=cls, count=cnt)

    return stats


class ExploreConfig(BaseModel):
    """Configuration for explore step."""

    input_dir: str = Field(default="", description="Input dataset directory")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=ExploreConfig,
        run_fn=lambda cfg: explore_dataset(cfg.input_dir or None),
        description="Explore wood-surface-defects dataset",
        skip_fields=[],
    )
