"""Standard Albumentations pipeline with class balancing up to a 1:3 ratio across the dataset."""

from __future__ import annotations

import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

import albumentations as A
import cv2
import numpy as np
import structlog
from pydantic import BaseModel, Field

from src.constants import ID_TO_CLASS, SPLIT_DATASET
from src.s2_augments.base import AlbumentationsAugmentor, register_augmentation
from src.utils import find_image_label_pairs, read_image, read_yolo_labels, write_image, write_yolo_labels

logger = structlog.get_logger(__name__)


class AlbumentationsBalancedConfig(BaseModel):
    """Configuration for standard albumentations with class balancing."""

    horizontal_flip_prob: float = Field(default=0.5, ge=0.0, le=1.0)
    vertical_flip_prob: float = Field(default=0.5, ge=0.0, le=1.0)
    rotate_90_prob: float = Field(default=0.5, ge=0.0, le=1.0)
    shift_scale_rotate_prob: float = Field(default=0.5, ge=0.0, le=1.0)
    brightness_contrast_prob: float = Field(default=0.4, ge=0.0, le=1.0)
    color_jitter_prob: float = Field(default=0.3, ge=0.0, le=1.0)
    blur_prob: float = Field(default=0.2, ge=0.0, le=1.0)
    target_ratio: float = Field(default=1 / 3, description="Target ratio relative to majority class")


class AlbumentationsBalancedAugmentor(AlbumentationsAugmentor):
    """Albumentations pipeline combined with class balancing oversampling."""

    name: str = "albumentations_balanced"

    def _build_pipeline(self, config: BaseModel) -> A.Compose:
        cfg = config if isinstance(config, AlbumentationsBalancedConfig) else AlbumentationsBalancedConfig()
        transforms = [
            A.HorizontalFlip(p=cfg.horizontal_flip_prob),
            A.VerticalFlip(p=cfg.vertical_flip_prob),
            A.RandomRotate90(p=cfg.rotate_90_prob),
            A.ShiftScaleRotate(
                shift_limit=0.05,
                scale_limit=0.10,
                rotate_limit=15,
                border_mode=cv2.BORDER_CONSTANT,
                value=0,
                p=cfg.shift_scale_rotate_prob,
            ),
            A.RandomBrightnessContrast(
                brightness_limit=0.2,
                contrast_limit=0.2,
                p=cfg.brightness_contrast_prob,
            ),
            A.ColorJitter(
                brightness=0.1,
                contrast=0.1,
                saturation=0.1,
                hue=0.1,
                p=cfg.color_jitter_prob,
            ),
            A.GaussianBlur(blur_limit=(3, 5), p=cfg.blur_prob),
        ]
        bbox_params = A.BboxParams(
            format="yolo",
            label_fields=["class_labels"],
            min_visibility=0.3,
        )
        return A.Compose(transforms, bbox_params=bbox_params)

    def generate_dataset(
        self,
        input_dir: Path | str | None = None,
        output_dir: Path | str | None = None,
        config: Any = None,
    ) -> Path:
        """Generate balanced augmented dataset split."""
        cfg = config if isinstance(config, AlbumentationsBalancedConfig) else AlbumentationsBalancedConfig()
        self._pipeline = self._build_pipeline(cfg)

        src_dir = Path(input_dir or (SPLIT_DATASET / "train"))
        target_dir = Path(output_dir)

        out_img_dir = target_dir / "train" / "images"
        out_lbl_dir = target_dir / "train" / "labels"
        out_img_dir.mkdir(parents=True, exist_ok=True)
        out_lbl_dir.mkdir(parents=True, exist_ok=True)

        pairs = find_image_label_pairs(src_dir)
        if not pairs:
            raise FileNotFoundError(f"No image/label pairs found in {src_dir}")

        logger.info("copying_base_dataset", source=str(src_dir), target=str(target_dir))
        class_counts: dict[int, int] = defaultdict(int)
        images_by_class: dict[int, list[tuple[Path, Path]]] = defaultdict(list)

        for img_p, lbl_p in pairs:
            shutil.copy2(img_p, out_img_dir / img_p.name)
            shutil.copy2(lbl_p, out_lbl_dir / lbl_p.name)

            bboxes = read_yolo_labels(lbl_p)
            for b in bboxes:
                class_counts[b.class_id] += 1
                if (img_p, lbl_p) not in images_by_class[b.class_id]:
                    images_by_class[b.class_id].append((img_p, lbl_p))

        majority_count = max(class_counts.values()) if class_counts else 0
        target_count_per_class = int(round(majority_count * cfg.target_ratio))

        logger.info(
            "albumentations_balance_targets",
            majority_count=majority_count,
            target_per_minority=target_count_per_class,
            initial_counts={ID_TO_CLASS[cid]: cnt for cid, cnt in class_counts.items()},
        )

        aug_counter = 0
        for class_id in sorted(class_counts.keys()):
            cls_name = ID_TO_CLASS.get(class_id, str(class_id))
            current = class_counts[class_id]

            if current >= target_count_per_class or not images_by_class[class_id]:
                continue

            needed = target_count_per_class - current
            candidate_pairs = images_by_class[class_id]
            logger.info(
                "oversampling_minority_class", class_name=cls_name, current=current, target=target_count_per_class
            )

            produced = 0
            while produced < needed:
                idx = np.random.randint(0, len(candidate_pairs))
                img_p, lbl_p = candidate_pairs[idx]

                img = read_image(img_p)
                bboxes = read_yolo_labels(lbl_p)
                if not bboxes:
                    continue

                aug_img, aug_bboxes = self.apply(img, bboxes)
                if not aug_bboxes:
                    continue

                aug_counter += 1
                out_name = f"{img_p.stem}_augbal_{aug_counter}"
                write_image(out_img_dir / f"{out_name}.jpg", aug_img)
                write_yolo_labels(out_lbl_dir / f"{out_name}.txt", aug_bboxes)

                for b in aug_bboxes:
                    class_counts[b.class_id] += 1
                    if b.class_id == class_id:
                        produced += 1

        logger.info(
            "albumentations_balanced_complete",
            total_augmented_files=aug_counter,
            final_counts={ID_TO_CLASS[cid]: cnt for cid, cnt in class_counts.items()},
        )
        return target_dir


register_augmentation("albumentations_balanced", AlbumentationsBalancedAugmentor)
