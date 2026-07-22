"""Explore the downloaded dataset: class distribution, bbox statistics, sample images.

Standalone usage:
    uv run python -m src.s1_prepare.explore [--input-dir PATH]
"""

from __future__ import annotations

from pathlib import Path

import structlog

from src.constants import CLASS_NAMES, ID_TO_CLASS, RAW_DATASET
from src.utils import read_yolo_labels, resolve_labels_dir

logger = structlog.get_logger(__name__)


def explore_dataset(input_dir: Path | str | None = None) -> dict[str, object]:
    """Compute dataset statistics from YOLO label files.

    Args:
        input_dir: Directory with images/ and labels/ sub-dirs.
                   Defaults to ``RAW_DATASET``.

    Returns:
        Dict with keys: total_images, total_annotations, class_counts,
        avg_boxes_per_image, bbox_stats.
    """
    input_dir = Path(input_dir or RAW_DATASET)
    labels_dir = resolve_labels_dir(input_dir)

    label_files = list(labels_dir.rglob("*.txt"))
    logger.info("scanning_labels", directory=str(labels_dir), count=len(label_files))

    class_counts: dict[str, int] = dict.fromkeys(CLASS_NAMES, 0)
    total_annotations = 0
    widths, heights, aspects, areas = [], [], [], []

    for lf in label_files:
        bboxes = read_yolo_labels(lf)
        total_annotations += len(bboxes)
        for b in bboxes:
            name = ID_TO_CLASS.get(b.class_id, f"unknown_{b.class_id}")
            class_counts[name] = class_counts.get(name, 0) + 1
            widths.append(b.w)
            heights.append(b.h)
            aspects.append(b.aspect_ratio())
            areas.append(b.area())

    stats: dict[str, object] = {
        "total_images": len(label_files),
        "total_annotations": total_annotations,
        "class_counts": class_counts,
        "avg_boxes_per_image": total_annotations / max(len(label_files), 1),
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


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=type("ExploreConfig", (), {"input_dir": RAW_DATASET}),
        run_fn=lambda cfg: explore_dataset(cfg.input_dir),
        description="Explore wood-surface-defects dataset",
        skip_fields=[],
    )
