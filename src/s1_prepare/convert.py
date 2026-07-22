"""Convert YOLO-format annotations to COCO JSON for MMDetection compatibility.

Standalone usage:
    uv run python -m src.s1_prepare.convert [--input-dir PATH] [--output-dir PATH]
"""

from __future__ import annotations

import json
from pathlib import Path

import cv2
import structlog

from src.constants import CLASS_NAMES, COCO_DATASET, RAW_DATASET
from src.utils import read_yolo_labels, resolve_labels_dir

logger = structlog.get_logger(__name__)


def convert_yolo_to_coco(
    input_dir: Path | str | None = None,
    output_dir: Path | str | None = None,
) -> Path:
    """Convert YOLO .txt labels to COCO-format JSON.

    Args:
        input_dir: Directory with images/ and labels/ sub-dirs.
        output_dir: Where to write ``coco_annotations.json``.

    Returns:
        Path to the generated COCO JSON file.
    """
    input_dir = Path(input_dir or RAW_DATASET)
    output_dir = Path(output_dir or COCO_DATASET)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("converting_yolo_to_coco", input=str(input_dir), output=str(output_dir))

    images_dir = input_dir / "images"
    labels_dir = resolve_labels_dir(input_dir)

    coco: dict = {
        "images": [],
        "annotations": [],
        "categories": [{"id": idx, "name": name, "supercategory": "defect"} for idx, name in enumerate(CLASS_NAMES)],
    }

    ann_id = 0
    image_files = sorted(images_dir.rglob("*.jpg")) + sorted(images_dir.rglob("*.png"))

    for img_id, img_path in enumerate(image_files, start=1):
        label_path = labels_dir / img_path.with_suffix(".txt").name
        if not label_path.exists():
            label_path = labels_dir / img_path.parent.name / img_path.with_suffix(".txt").name

        img = cv2.imread(str(img_path))
        if img is None:
            logger.warning("unreadable_image", path=str(img_path))
            continue
        h, w = img.shape[:2]

        coco["images"].append(
            {
                "id": img_id,
                "file_name": str(img_path.relative_to(input_dir)),
                "width": w,
                "height": h,
            }
        )

        if not label_path.exists():
            continue

        for b in read_yolo_labels(label_path):
            x = (b.cx - b.w / 2) * w
            y = (b.cy - b.h / 2) * h
            abs_w = b.w * w
            abs_h = b.h * h

            coco["annotations"].append(
                {
                    "id": ann_id,
                    "image_id": img_id,
                    "category_id": b.class_id,
                    "bbox": [round(x, 2), round(y, 2), round(abs_w, 2), round(abs_h, 2)],
                    "area": round(abs_w * abs_h, 2),
                    "iscrowd": 0,
                }
            )
            ann_id += 1

    out_path = output_dir / "coco_annotations.json"
    with open(out_path, "w") as f:
        json.dump(coco, f, indent=2)

    logger.info(
        "conversion_complete",
        images=len(coco["images"]),
        annotations=len(coco["annotations"]),
        output=str(out_path),
    )
    return out_path


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=type("ConvertConfig", (), {"input_dir": RAW_DATASET, "output_dir": COCO_DATASET}),
        run_fn=lambda cfg: convert_yolo_to_coco(cfg.input_dir, cfg.output_dir),
        description="Convert YOLO to COCO format",
    )
