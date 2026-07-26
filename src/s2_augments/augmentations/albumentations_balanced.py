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
    keep_train_size: bool = Field(
        default=True, description="Keep total training dataset size approximately equal to input size"
    )
    max_decrement_ratio: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Max fraction of pure majority images to decrement"
    )


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
        """Generate balanced augmented dataset split by augmenting rare classes

        and decrementing largest classes to maintain constant dataset size.
        """
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

        total_input_images = len(pairs)

        class_counts: dict[int, int] = defaultdict(int)
        image_class_counts: dict[Path, dict[int, int]] = {}
        images_by_class: dict[int, list[tuple[Path, Path]]] = defaultdict(list)

        for img_p, lbl_p in pairs:
            bboxes = read_yolo_labels(lbl_p)
            counts: dict[int, int] = defaultdict(int)
            for b in bboxes:
                counts[b.class_id] += 1
                class_counts[b.class_id] += 1
                if (img_p, lbl_p) not in images_by_class[b.class_id]:
                    images_by_class[b.class_id].append((img_p, lbl_p))
            image_class_counts[img_p] = counts

        majority_count = max(class_counts.values()) if class_counts else 0
        target_count_per_class = int(round(majority_count * cfg.target_ratio))

        rare_class_ids = {cid for cid, count in class_counts.items() if count < target_count_per_class}
        majority_class_ids = {cid for cid, count in class_counts.items() if count >= target_count_per_class}

        logger.info(
            "albumentations_balance_targets",
            total_input_images=total_input_images,
            majority_count=majority_count,
            target_per_minority=target_count_per_class,
            rare_classes=[ID_TO_CLASS.get(c, str(c)) for c in sorted(rare_class_ids)],
            initial_counts={ID_TO_CLASS.get(cid, str(cid)): cnt for cid, cnt in class_counts.items()},
        )

        pure_majority_pairs: list[tuple[Path, Path]] = []
        kept_base_pairs: list[tuple[Path, Path]] = []

        for img_p, lbl_p in pairs:
            counts = image_class_counts[img_p]
            img_class_set = set(counts.keys())

            if img_class_set & rare_class_ids:
                kept_base_pairs.append((img_p, lbl_p))
            elif img_class_set & majority_class_ids and not (img_class_set & rare_class_ids):
                pure_majority_pairs.append((img_p, lbl_p))
            else:
                kept_base_pairs.append((img_p, lbl_p))

        needed_instances_by_class: dict[int, int] = {}
        needed_aug_images_by_class: dict[int, int] = {}
        total_needed_aug_images = 0

        for cid in sorted(rare_class_ids):
            needed = target_count_per_class - class_counts[cid]
            needed_instances_by_class[cid] = max(0, needed)
            c_pairs = images_by_class[cid]
            if c_pairs and needed > 0:
                avg_bboxes = sum(image_class_counts[p[0]][cid] for p in c_pairs) / len(c_pairs)
                est_imgs = int(np.ceil(needed / max(1.0, avg_bboxes)))
                needed_aug_images_by_class[cid] = est_imgs
                total_needed_aug_images += est_imgs
            else:
                needed_aug_images_by_class[cid] = 0

        if cfg.keep_train_size:
            max_decrements = int(len(pure_majority_pairs) * cfg.max_decrement_ratio)
            num_decrements = min(total_needed_aug_images, max_decrements)
            num_augments = num_decrements
        else:
            num_decrements = 0
            num_augments = total_needed_aug_images

        # Rank pure majority images by total majority class bboxes (descending) so dropping them reduces majority count most efficiently
        def _majority_bbox_score(pair: tuple[Path, Path]) -> int:
            return sum(image_class_counts[pair[0]].get(c, 0) for c in majority_class_ids)

        pure_majority_pairs.sort(key=_majority_bbox_score, reverse=True)
        dropped_pairs = pure_majority_pairs[:num_decrements]
        retained_majority_pairs = pure_majority_pairs[num_decrements:]
        kept_base_pairs.extend(retained_majority_pairs)

        logger.info(
            "albumentations_decrement_plan",
            total_pure_majority_candidates=len(pure_majority_pairs),
            num_decrements=num_decrements,
            num_augments_planned=num_augments,
            kept_base_count=len(kept_base_pairs),
            dropped_samples_preview=[p[0].name for p in dropped_pairs[:5]],
        )

        for img_p, lbl_p in kept_base_pairs:
            shutil.copy2(img_p, out_img_dir / img_p.name)
            shutil.copy2(lbl_p, out_lbl_dir / lbl_p.name)

        aug_counter = 0
        if num_augments > 0 and total_needed_aug_images > 0:
            image_aug_counts: dict[Path, int] = defaultdict(int)

            class_aug_targets: dict[int, int] = {}
            allocated = 0
            sorted_rare = sorted(rare_class_ids, key=lambda c: needed_aug_images_by_class[c], reverse=True)
            for idx, cid in enumerate(sorted_rare):
                if idx == len(sorted_rare) - 1:
                    class_aug_targets[cid] = num_augments - allocated
                else:
                    share = int(round(num_augments * (needed_aug_images_by_class[cid] / total_needed_aug_images)))
                    class_aug_targets[cid] = share
                    allocated += share

            for cid in sorted_rare:
                cls_name = ID_TO_CLASS.get(cid, str(cid))
                target_aug_for_cls = class_aug_targets.get(cid, 0)
                candidate_pairs = images_by_class[cid]

                if target_aug_for_cls <= 0 or not candidate_pairs:
                    continue

                produced = 0
                max_attempts = target_aug_for_cls * 5
                attempts = 0

                logger.info(
                    "augmenting_rare_class",
                    class_name=cls_name,
                    target_augments=target_aug_for_cls,
                    candidate_pool_size=len(candidate_pairs),
                )

                while produced < target_aug_for_cls and attempts < max_attempts:
                    attempts += 1
                    min_aug = min(image_aug_counts[p[0]] for p in candidate_pairs)
                    min_candidates = [p for p in candidate_pairs if image_aug_counts[p[0]] == min_aug]
                    selected_pair = min_candidates[np.random.randint(0, len(min_candidates))]
                    img_p, lbl_p = selected_pair

                    img = read_image(img_p)
                    bboxes = read_yolo_labels(lbl_p)
                    if not bboxes:
                        continue

                    aug_img, aug_bboxes = self.apply(img, bboxes)
                    if not aug_bboxes:
                        continue

                    image_aug_counts[img_p] += 1
                    produced += 1
                    aug_counter += 1

                    out_name = f"{img_p.stem}_augbal_{aug_counter}"
                    write_image(out_img_dir / f"{out_name}.jpg", aug_img)
                    write_yolo_labels(out_lbl_dir / f"{out_name}.txt", aug_bboxes)

                    for b in aug_bboxes:
                        class_counts[b.class_id] += 1

        final_dataset_size = len(list(out_img_dir.glob("*.jpg"))) + len(list(out_img_dir.glob("*.png")))

        logger.info(
            "albumentations_balanced_complete",
            total_input_images=total_input_images,
            decremented_majority_images=num_decrements,
            total_augmented_files=aug_counter,
            final_dataset_size=final_dataset_size,
            final_counts={ID_TO_CLASS.get(cid, str(cid)): cnt for cid, cnt in class_counts.items()},
        )
        return target_dir


register_augmentation("albumentations_balanced", AlbumentationsBalancedAugmentor)

