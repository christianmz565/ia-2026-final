"""Convert YOLO-format labels to COCO JSON.

Reads .txt label files (class x_center y_center width height, normalized)
and generates COCO JSON files in each split directory.

Standalone usage:
    uv run python -m src.s1_prepare.convert_coco
"""

from __future__ import annotations

import json
from pathlib import Path

import cv2
import structlog

from src.caching import run_cached_step
from src.coco_utils import SUPPORTED_IMAGE_SUFFIXES, build_categories, yolo_to_coco_bbox
from src.constants import SPLIT_DATASET

logger = structlog.get_logger(__name__)

SPLITS = ["train", "val", "test"]


def convert_split(
    data_dir: Path,
    split: str,
    output_path: Path | None = None,
) -> Path | None:
    """Convert one split (train/val/test) from YOLO to COCO JSON.

    Args:
        data_dir: Root dataset directory containing split subdirectories.
        split: Name of the split (e.g. ``train``, ``val``, ``test``).
        output_path: Where to write the COCO JSON. Defaults to
            ``{data_dir}/{split}/_annotations.coco.json``.

    Returns:
        Path to the generated COCO JSON, or None if skipped.
    """
    images_dir = data_dir / split / "images"
    labels_dir = data_dir / split / "labels"

    if not images_dir.exists() or not labels_dir.exists():
        logger.warning("yolo_to_coco_skip", split=split, reason="missing images/ or labels/")
        return None

    out_path = output_path or (labels_dir.parent / "_annotations.coco.json")

    def _convert() -> Path:
        images: list[dict] = []
        annotations: list[dict] = []
        categories = build_categories()

        ann_id = 1
        img_id = 0

        img_files = sorted(
            p for p in images_dir.iterdir() if p.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES
        )

        for img_path in img_files:
            img_id += 1
            img = cv2.imread(str(img_path))
            if img is None:
                logger.warning("yolo_to_coco_unreadable_image", path=str(img_path))
                continue
            h, w = img.shape[:2]

            images.append(
                {
                    "id": img_id,
                    "file_name": f"images/{img_path.name}",
                    "width": w,
                    "height": h,
                }
            )

            label_path = labels_dir / f"{img_path.stem}.txt"
            if not label_path.exists():
                continue

            for line in label_path.read_text().strip().splitlines():
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                class_id = int(parts[0])
                x_c, y_c, bw, bh = map(float, parts[1:5])

                bbox = yolo_to_coco_bbox(x_c, y_c, bw, bh, w, h)
                area = bbox[2] * bbox[3]

                annotations.append(
                    {
                        "id": ann_id,
                        "image_id": img_id,
                        "category_id": class_id + 1,
                        "bbox": bbox,
                        "area": round(area, 2),
                        "iscrowd": 0,
                    }
                )
                ann_id += 1

        coco = {
            "info": {"description": "Converted from YOLO format dataset"},
            "licenses": [],
            "categories": categories,
            "images": images,
            "annotations": annotations,
        }
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(coco, indent=2))
        logger.info(
            "yolo_to_coco_complete",
            split=split,
            images=len(images),
            annotations=len(annotations),
            output=str(out_path),
        )
        return out_path

    return run_cached_step(
        step_name=f"yolo_to_coco_{split}",
        target_path=out_path,
        fn=_convert,
        loader=lambda p: p,
    )


def convert_coco_dataset(data_dir: Path | None = None) -> None:
    """Convert all splits from YOLO to COCO JSON.

    Args:
        data_dir: Root dataset directory. Defaults to ``SPLIT_DATASET``.
    """
    root = data_dir or SPLIT_DATASET
    logger.info("yolo_to_coco_start", data_dir=str(root))
    for split in SPLITS:
        convert_split(root, split)
    logger.info("yolo_to_coco_all_complete")


if __name__ == "__main__":
    convert_coco_dataset()
