"""Convert YOLO-format labels to COCO JSON for RF-DETR.

Reads .txt label files (class x_center y_center width height, normalized)
and generates _annotations.coco.json files in each split directory.

Standalone usage:
    uv run python -m src.s1_prepare.convert_coco
"""

from __future__ import annotations

import json
from pathlib import Path

import cv2
import structlog

from src.caching import run_cached_step
from src.constants import CLASS_NAMES, SPLIT_DATASET

logger = structlog.get_logger(__name__)

SPLITS = ["train", "val", "test"]


def yolo_to_coco_bbox(x_center: float, y_center: float, w: float, h: float, img_w: int, img_h: int) -> list[float]:
    """Convert normalized YOLO bbox to COCO [x_top_left, y_top_left, width, height] in pixels."""
    abs_w = w * img_w
    abs_h = h * img_h
    x_top_left = x_center * img_w - abs_w / 2
    y_top_left = y_center * img_h - abs_h / 2
    return [round(x_top_left, 2), round(y_top_left, 2), round(abs_w, 2), round(abs_h, 2)]


def convert_split(data_dir: Path, split: str) -> Path | None:
    """Convert one split (train/val/test) from YOLO to COCO JSON.

    Args:
        data_dir: Root dataset directory containing split subdirectories.
        split: Name of the split (e.g. ``train``, ``val``, ``test``).

    Returns:
        Path to the generated COCO JSON, or None if skipped.
    """
    images_dir = data_dir / split / "images"
    labels_dir = data_dir / split / "labels"

    if not images_dir.exists() or not labels_dir.exists():
        logger.warning("yolo_to_coco_skip", split=split, reason="missing images/ or labels/")
        return None

    out_path = labels_dir.parent / "_annotations.coco.json"

    def _convert() -> Path:
        images: list[dict] = []
        annotations: list[dict] = []
        categories: list[dict] = [{"id": i, "name": name} for i, name in enumerate(CLASS_NAMES)]

        ann_id = 0
        img_id = 0

        for img_path in sorted(images_dir.glob("*.jpg")):
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
                        "category_id": class_id,
                        "bbox": bbox,
                        "area": round(area, 2),
                        "iscrowd": 0,
                    }
                )
                ann_id += 1

        coco = {"images": images, "annotations": annotations, "categories": categories}
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
