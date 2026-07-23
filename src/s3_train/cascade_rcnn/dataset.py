"""Dataset loading, automatic YOLO-to-COCO conversion, sanitization, and PyTorch Dataset module.

Features:
- Auto-detects and converts YOLO format txt annotations (in dataset/split/train, dataset/split/val) to COCO JSON format if JSON file is missing.
- Light sanitization / filtering phase:
  * Discards corrupt or unreadable image files.
  * Discards invalid bounding boxes (area <= 0, xmax <= xmin, ymax <= ymin, out of bounds).
  * Discards images without valid annotations.
- Restrictive image treatment (BASELINE):
  * STRICTLY NO resizing, NO cropping, NO data augmentations.
  * Native resolution preserved for all valid images.
- Generates Data Sanitization Report (JSON & Markdown).
"""

import json
from pathlib import Path
from typing import Any

import cv2
import structlog
import torch
from PIL import Image
from torch.utils.data import Dataset

logger = structlog.get_logger(__name__)

DEFAULT_CLASSES = [
    "Quartzity",
    "Live_Knot",
    "Marrow",
    "resin",
    "Dead_Knot",
    "knot_with_crack",
    "Knot_missing",
    "Crack",
]


class DataSanitizer:
    """Sanitizes object detection datasets by filtering invalid images and annotations.

    Automatically handles YOLO txt annotation files if COCO JSON file does not exist.
    """

    def __init__(self, data_dir: Path, class_names: list[str] | None = None):
        self.data_dir = Path(data_dir)
        self.class_names = class_names or DEFAULT_CLASSES

    def convert_yolo_to_coco(self, split_name: str, output_json: Path) -> dict[str, Any]:
        """Convert YOLO format dataset (split_name/images and split_name/labels) to COCO format dict."""
        split_dir = self.data_dir / split_name
        if not split_dir.exists():
            split_dir = self.data_dir

        images_dir = split_dir / "images"
        labels_dir = split_dir / "labels"

        if not images_dir.exists():
            raise FileNotFoundError(f"Images directory not found: {images_dir}")

        categories = [
            {"id": i + 1, "name": name, "supercategory": "wood_defect"} for i, name in enumerate(self.class_names)
        ]

        images = []
        annotations = []
        ann_id = 1

        img_files = sorted([f for f in images_dir.glob("*") if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".bmp")])
        logger.info(f"Converting YOLO dataset split '{split_name}': found {len(img_files)} images...")

        for img_id, img_path in enumerate(img_files, start=1):
            try:
                with Image.open(img_path) as img:
                    w, h = img.size
            except Exception as e:
                logger.warning(f"Failed to read image dimensions for {img_path}: {e}")
                continue

            rel_file_name = f"{split_name}/images/{img_path.name}"
            images.append(
                {
                    "id": img_id,
                    "file_name": rel_file_name,
                    "width": w,
                    "height": h,
                    "resolved_path": str(img_path),
                }
            )

            txt_path = labels_dir / f"{img_path.stem}.txt"
            if not txt_path.exists():
                continue

            try:
                content = txt_path.read_text().strip()
            except Exception:
                continue

            if not content:
                continue

            for line in content.split("\n"):
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                try:
                    cls_id = int(parts[0])
                    cx, cy, nw, nh = map(float, parts[1:5])
                except ValueError:
                    continue

                bw = nw * w
                bh = nh * h
                xmin = (cx - nw / 2.0) * w
                ymin = (cy - nh / 2.0) * h

                annotations.append(
                    {
                        "id": ann_id,
                        "image_id": img_id,
                        "category_id": cls_id + 1,
                        "bbox": [xmin, ymin, bw, bh],
                        "area": bw * bh,
                        "iscrowd": 0,
                    }
                )
                ann_id += 1

        coco_dict = {
            "info": {"description": "Converted from YOLO format dataset"},
            "licenses": [],
            "categories": categories,
            "images": images,
            "annotations": annotations,
        }

        output_json.parent.mkdir(parents=True, exist_ok=True)
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(coco_dict, f, indent=2)

        logger.info(
            f"Successfully saved converted COCO JSON to {output_json} ({len(images)} images, {len(annotations)} annotations)"
        )
        return coco_dict

    def sanitize_coco(self, json_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
        """Validate and filter COCO annotation dict or auto-convert YOLO if JSON missing.

        Returns:
            tuple of (sanitized_coco_dict, sanitization_stats)
        """
        json_path = Path(json_path)

        if not json_path.exists():
            stem = json_path.stem.lower()
            if "train" in stem:
                split_name = "train"
            elif "val" in stem:
                split_name = "val"
            elif "test" in stem:
                split_name = "test"
            else:
                split_name = "train"

            logger.info(f"JSON file {json_path} not found. Auto-converting YOLO txt dataset from '{split_name}'...")
            raw_coco = self.convert_yolo_to_coco(split_name, json_path)
        else:
            with open(json_path, encoding="utf-8") as f:
                raw_coco = json.load(f)

        stats = {
            "total_images_inspected": len(raw_coco.get("images", [])),
            "valid_images_retained": 0,
            "corrupt_images_discarded": 0,
            "images_no_valid_annotations": 0,
            "total_annotations_inspected": len(raw_coco.get("annotations", [])),
            "valid_annotations_retained": 0,
            "invalid_annotations_discarded": 0,
            "discard_reasons": {
                "zero_or_negative_area": 0,
                "invalid_coordinates": 0,
                "out_of_bounds": 0,
                "missing_file": 0,
                "corrupt_file": 0,
            },
        }

        images_by_id = {img["id"]: img for img in raw_coco.get("images", [])}
        annotations_by_img_id: dict[int, list[dict[str, Any]]] = {}

        for ann in raw_coco.get("annotations", []):
            img_id = ann["image_id"]
            annotations_by_img_id.setdefault(img_id, []).append(ann)

        sanitized_images = []
        sanitized_annotations = []
        valid_img_ids = set()

        for img_id, img_info in images_by_id.items():
            file_name = img_info["file_name"]
            img_path = self.data_dir / file_name

            resolved_path = img_info.get("resolved_path")
            if resolved_path and Path(resolved_path).exists():
                img_path = Path(resolved_path)
            elif not img_path.exists():
                alt_path = self.data_dir / Path(file_name).name
                if alt_path.exists():
                    img_path = alt_path
                else:
                    stats["corrupt_images_discarded"] += 1
                    stats["discard_reasons"]["missing_file"] += 1
                    logger.warning(f"Image file missing: {img_path}")
                    continue

            try:
                with Image.open(img_path) as img:
                    img.verify()
                with Image.open(img_path) as img:
                    width, height = img.size
            except Exception as e:
                stats["corrupt_images_discarded"] += 1
                stats["discard_reasons"]["corrupt_file"] += 1
                logger.warning(f"Corrupt image file discarded: {img_path} ({e})")
                continue

            img_anns = annotations_by_img_id.get(img_id, [])
            valid_img_anns = []

            for ann in img_anns:
                bbox = ann.get("bbox", [])
                if len(bbox) != 4:
                    stats["invalid_annotations_discarded"] += 1
                    stats["discard_reasons"]["invalid_coordinates"] += 1
                    continue

                x, y, w, h = bbox
                xmin, ymin, xmax, ymax = x, y, x + w, y + h

                area = ann.get("area", w * h)
                if area <= 0 or w <= 0 or h <= 0:
                    stats["invalid_annotations_discarded"] += 1
                    stats["discard_reasons"]["zero_or_negative_area"] += 1
                    continue

                if xmax <= xmin or ymax <= ymin:
                    stats["invalid_annotations_discarded"] += 1
                    stats["discard_reasons"]["invalid_coordinates"] += 1
                    continue

                if xmin < -1 or ymin < -1 or xmax > width + 1 or ymax > height + 1:
                    stats["invalid_annotations_discarded"] += 1
                    stats["discard_reasons"]["out_of_bounds"] += 1
                    continue

                xmin_c = max(0.0, float(xmin))
                ymin_c = max(0.0, float(ymin))
                xmax_c = min(float(width), float(xmax))
                ymax_c = min(float(height), float(ymax))
                w_c = xmax_c - xmin_c
                h_c = ymax_c - ymin_c

                if w_c <= 0 or h_c <= 0:
                    stats["invalid_annotations_discarded"] += 1
                    stats["discard_reasons"]["zero_or_negative_area"] += 1
                    continue

                ann_clean = dict(ann)
                ann_clean["bbox"] = [xmin_c, ymin_c, w_c, h_c]
                ann_clean["area"] = w_c * h_c
                valid_img_anns.append(ann_clean)

            if not valid_img_anns:
                stats["images_no_valid_annotations"] += 1
                continue

            img_info_clean = dict(img_info)
            img_info_clean["width"] = width
            img_info_clean["height"] = height
            img_info_clean["resolved_path"] = str(img_path)

            sanitized_images.append(img_info_clean)
            sanitized_annotations.extend(valid_img_anns)
            valid_img_ids.add(img_id)

        stats["valid_images_retained"] = len(sanitized_images)
        stats["valid_annotations_retained"] = len(sanitized_annotations)

        sanitized_coco = {
            "info": raw_coco.get("info", {}),
            "licenses": raw_coco.get("licenses", []),
            "categories": raw_coco.get("categories", []),
            "images": sanitized_images,
            "annotations": sanitized_annotations,
        }

        return sanitized_coco, stats

    def save_report(self, stats: dict[str, Any], output_json: Path, output_md: Path) -> None:
        """Save Data Sanitization Report to JSON and Markdown format."""
        output_json.parent.mkdir(parents=True, exist_ok=True)
        output_md.parent.mkdir(parents=True, exist_ok=True)

        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)

        md_content = f"""# Data Sanitization & Validation Report

## Executive Summary
- **Total Images Inspected:** {stats.get("train_set", {}).get("total_images_inspected", 0) + stats.get("val_set", {}).get("total_images_inspected", 0)}
- **Train Valid Images Retained:** {stats.get("train_set", {}).get("valid_images_retained", 0)}
- **Val Valid Images Retained:** {stats.get("val_set", {}).get("valid_images_retained", 0)}
- **Corrupt/Missing Images Discarded:** {stats.get("train_set", {}).get("corrupt_images_discarded", 0) + stats.get("val_set", {}).get("corrupt_images_discarded", 0)}

## Annotation Breakdown
- **Train Valid Annotations:** {stats.get("train_set", {}).get("valid_annotations_retained", 0)}
- **Val Valid Annotations:** {stats.get("val_set", {}).get("valid_annotations_retained", 0)}
- **Invalid Annotations Discarded:** {stats.get("train_set", {}).get("invalid_annotations_discarded", 0) + stats.get("val_set", {}).get("invalid_annotations_discarded", 0)}

## Baseline Policy Compliance
- **Image Resizing:** Disabled (Native resolution preserved).
- **Data Augmentation:** Disabled (Strict baseline protocol).
"""
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(md_content)

        logger.info(f"Data Sanitization Report written to {output_json} and {output_md}")


class WoodDataset(Dataset):
    """PyTorch Dataset for Wood Surface Defect Detection.

    Strictly preserves native image resolution (No resizing / cropping / augmentations).
    """

    def __init__(
        self,
        coco_dict: dict[str, Any],
        data_dir: Path,
    ):
        self.data_dir = Path(data_dir)
        self.categories = coco_dict.get("categories", [])
        self.cat_id_to_label = {cat["id"]: i + 1 for i, cat in enumerate(self.categories)}
        self.label_to_cat_name = {i + 1: cat["name"] for i, cat in enumerate(self.categories)}

        self.images = coco_dict.get("images", [])
        self.annotations = coco_dict.get("annotations", [])

        self.img_id_to_anns: dict[int, list[dict[str, Any]]] = {}
        for ann in self.annotations:
            self.img_id_to_anns.setdefault(ann["image_id"], []).append(ann)

        self.mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)

    def __len__(self) -> int:
        return len(self.images)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        img_info = self.images[idx]
        img_id = img_info["id"]

        resolved_path = img_info.get("resolved_path")
        if resolved_path and Path(resolved_path).exists():
            img_path = Path(resolved_path)
        else:
            img_path = self.data_dir / img_info["file_name"]

        img_bgr = cv2.imread(str(img_path))
        if img_bgr is None:
            raise RuntimeError(f"Failed to load image at index {idx}: {img_path}")

        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        h, w, c = img_rgb.shape

        img_tensor = torch.from_numpy(img_rgb).permute(2, 0, 1).float() / 255.0
        img_tensor = (img_tensor - self.mean) / self.std

        anns = self.img_id_to_anns.get(img_id, [])

        boxes = []
        labels = []
        areas = []
        iscrowd = []

        for ann in anns:
            x, y, bw, bh = ann["bbox"]
            xmin = max(0.0, float(x))
            ymin = max(0.0, float(y))
            xmax = min(float(w), float(x + bw))
            ymax = min(float(h), float(y + bh))

            if xmax > xmin and ymax > ymin:
                boxes.append([xmin, ymin, xmax, ymax])
                cat_id = ann["category_id"]
                label = self.cat_id_to_label.get(cat_id, cat_id)
                labels.append(label)
                areas.append((xmax - xmin) * (ymax - ymin))
                iscrowd.append(ann.get("iscrowd", 0))

        if len(boxes) == 0:
            boxes_tensor = torch.zeros((0, 4), dtype=torch.float32)
            labels_tensor = torch.zeros((0,), dtype=torch.int64)
            areas_tensor = torch.zeros((0,), dtype=torch.float32)
            iscrowd_tensor = torch.zeros((0,), dtype=torch.int64)
        else:
            boxes_tensor = torch.tensor(boxes, dtype=torch.float32)
            labels_tensor = torch.tensor(labels, dtype=torch.int64)
            areas_tensor = torch.tensor(areas, dtype=torch.float32)
            iscrowd_tensor = torch.tensor(iscrowd, dtype=torch.int64)

        target = {
            "boxes": boxes_tensor,
            "labels": labels_tensor,
            "image_id": torch.tensor([img_id], dtype=torch.int64),
            "area": areas_tensor,
            "iscrowd": iscrowd_tensor,
            "orig_size": torch.tensor([h, w], dtype=torch.int64),
        }

        return img_tensor, target


def collate_fn(batch: list[tuple[torch.Tensor, dict[str, torch.Tensor]]]):
    """Collate function for native resolution image batches."""
    images = [item[0] for item in batch]
    targets = [item[1] for item in batch]
    return images, targets
