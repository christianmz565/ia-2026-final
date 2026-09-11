"""Explore the dataset: class distribution, bbox statistics, sample images.

Standalone usage:
    uv run python -m src.s1_prepare.explore [--input-dir PATH]
"""

from __future__ import annotations

import json
from pathlib import Path

import structlog
from pydantic import BaseModel, Field
from tqdm import tqdm

from src.caching import config_fingerprint, run_cached_step
from src.constants import CLASS_NAMES, ID_TO_CLASS, S1_OUTPUT
from src.utils import find_image_label_pairs, read_yolo_labels

logger = structlog.get_logger(__name__)


def explore_dataset(
    input_dir: Path | str | None = None,
    output_file: Path | str | None = None,
    force: bool = False,
) -> dict[str, object]:
    """Compute dataset statistics from YOLO label files.

    Args:
        input_dir: Directory with images/ and labels/ sub-dirs (required).
        output_file: Path to output JSON stats file. Defaults to ``S1_OUTPUT / "explore_stats.json"``.
        force: If True, bypass cache and re-compute statistics.

    Returns:
        Dict with keys: total_images, total_annotations, class_counts,
        avg_boxes_per_image, bbox_stats.
    """
    if input_dir is None:
        raise ValueError("explore_dataset requires an explicit input_dir")
    resolved_input = Path(input_dir)
    resolved_output = Path(output_file or S1_OUTPUT / "explore_stats.json")

    def _explore() -> dict[str, object]:
        pairs = find_image_label_pairs(resolved_input)
        if not pairs:
            raise FileNotFoundError(f"No images found in {resolved_input}")
        logger.info("scanning_dataset", directory=str(resolved_input), count=len(pairs))

        class_counts: dict[str, int] = dict.fromkeys(CLASS_NAMES, 0)
        total_annotations = 0
        widths, heights, aspects, areas = [], [], [], []

        for _, label_path in tqdm(pairs, desc="Exploring dataset", unit="img"):
            bboxes = read_yolo_labels(label_path)
            total_annotations += len(bboxes)
            for b in bboxes:
                if b.class_id not in ID_TO_CLASS:
                    raise ValueError(f"Unknown class_id {b.class_id} in {label_path}")
                name = ID_TO_CLASS[b.class_id]
                class_counts[name] = class_counts.get(name, 0) + 1
                widths.append(b.w)
                heights.append(b.h)
                aspects.append(b.aspect_ratio())
                areas.append(b.area())

        if total_annotations == 0:
            raise ValueError(f"No annotations found in {resolved_input}")
        stats: dict[str, object] = {
            "total_images": len(pairs),
            "total_annotations": total_annotations,
            "class_counts": class_counts,
            "avg_boxes_per_image": total_annotations / len(pairs),
            "bbox_stats": {
                "mean_width": sum(widths) / len(widths),
                "mean_height": sum(heights) / len(heights),
                "mean_aspect_ratio": sum(aspects) / len(aspects),
                "mean_area": sum(areas) / len(areas),
            },
        }

        logger.info("dataset_stats", **{k: v for k, v in stats.items() if k != "class_counts"})
        for cls, cnt in class_counts.items():
            logger.info("class_distribution", className=cls, count=cnt)

        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        resolved_output.write_text(json.dumps(stats, indent=2))

        return stats

    return run_cached_step(
        step_name="explore",
        target_path=resolved_output,
        fn=_explore,
        force=force,
        loader=lambda p: json.loads(p.read_text()),
        fingerprint=config_fingerprint({"input_dir": str(resolved_input)}),
    )


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
