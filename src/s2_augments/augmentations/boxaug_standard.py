"""Standard BoxAug implementation based on Lee et al. (2022)."""

from __future__ import annotations

import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

import cv2
import numpy as np
import structlog
from pydantic import BaseModel, Field

from src.constants import ID_TO_CLASS, SPLIT_DATASET
from src.s2_augments.base import (
    Augmentor,
    check_overlap,
    register_augmentation,
    sample_spatial_location,
)
from src.utils import BBox, find_image_label_pairs, read_image, read_yolo_labels, write_image, write_yolo_labels

logger = structlog.get_logger(__name__)


class BoxAugStandardConfig(BaseModel):
    """Configuration for BoxAug standard pipeline."""

    target_ratio: float = Field(default=1 / 3, description="Target minority-to-majority ratio")
    max_location_attempts: int = Field(default=50, description="Max spatial placement retries to prevent overlaps")
    max_num_transforms: int = Field(default=5, description="Max candidate transformations to apply per box")


def add_gaussian_noise(img: np.ndarray, std: float = 15.0) -> np.ndarray:
    """Add Gaussian noise to image crop."""
    noise = np.random.normal(0, std, img.shape).astype(np.float32)
    noisy = np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    return noisy


def add_poisson_noise(img: np.ndarray) -> np.ndarray:
    """Add Poisson noise to image crop."""
    vals = len(np.unique(img))
    vals = 2 ** np.ceil(np.log2(vals)) if vals > 0 else 1
    noisy = np.random.poisson(img.astype(np.float32) * vals) / float(vals)
    return np.clip(noisy, 0, 255).astype(np.uint8)


def add_salt_pepper_noise(img: np.ndarray, amount: float = 0.02) -> np.ndarray:
    """Add Salt & Pepper noise to image crop."""
    out = img.copy()
    num_salt = int(np.ceil(amount * img.size * 0.5))
    coords = [np.random.randint(0, i - 1, num_salt) for i in img.shape[:2]]
    out[tuple(coords)] = 255
    num_pepper = int(np.ceil(amount * img.size * 0.5))
    coords = [np.random.randint(0, i - 1, num_pepper) for i in img.shape[:2]]
    out[tuple(coords)] = 0
    return out


def add_speckle_noise(img: np.ndarray) -> np.ndarray:
    """Add Speckle noise to image crop."""
    gauss = np.random.randn(*img.shape) * 0.15
    noisy = img.astype(np.float32) + img.astype(np.float32) * gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)


def apply_random_noise(crop: np.ndarray) -> np.ndarray:
    """Randomly apply one of 4 noise types (Gaussian, Poisson, Salt & Pepper, Speckle)."""
    choice = int(np.random.randint(0, 4))
    if choice == 0:
        return add_gaussian_noise(crop)
    elif choice == 1:
        return add_poisson_noise(crop)
    elif choice == 2:
        return add_salt_pepper_noise(crop)
    else:
        return add_speckle_noise(crop)


def apply_morphological_mask(crop: np.ndarray) -> np.ndarray:
    """Generate morphological edge mask and blend with original crop."""
    if crop.shape[0] < 5 or crop.shape[1] < 5:
        return crop

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY) if crop.ndim == 3 else crop
    kernel_size = int(np.random.choice([15, 45]))
    kernel_size = min(kernel_size, min(crop.shape[:2]) // 2 * 2 + 1)
    if kernel_size < 3:
        kernel_size = 3

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    op = int(np.random.randint(0, 4))

    if op == 0:
        morph = cv2.dilate(gray, kernel)
    elif op == 1:
        morph = cv2.erode(gray, kernel)
    elif op == 2:
        morph = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    else:
        morph = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    morph_3ch = cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR) if crop.ndim == 3 else morph
    alpha = float(np.random.uniform(0.15, 0.40))
    blended = cv2.addWeighted(crop, 1.0 - alpha, morph_3ch, alpha, 0)
    return blended


def apply_random_crop(crop: np.ndarray) -> np.ndarray:
    """Randomly crop up to 10% from the upper-left of the crop."""
    h, w = crop.shape[:2]
    if h < 10 or w < 10:
        return crop

    crop_x = int(np.random.uniform(0, 0.10 * w))
    crop_y = int(np.random.uniform(0, 0.10 * h))

    cropped = crop[crop_y:h, crop_x:w]
    if cropped.shape[0] == 0 or cropped.shape[1] == 0:
        return crop
    return cropped


def transform_box_crop(crop: np.ndarray, max_transforms: int = 5) -> np.ndarray:
    """Apply BoxAug object-level transformations to cropped defect instance."""
    res = crop.copy()
    h, w = res.shape[:2]

    scale_factor = float(np.random.uniform(0.8, 1.2))
    new_w = max(4, int(round(w * scale_factor)))
    new_h = max(4, int(round(h * scale_factor)))
    res = cv2.resize(res, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    candidate_transforms = ["random_crop", "add_noise", "h_flip", "v_flip", "morphological_mask"]
    num_to_apply = int(np.random.randint(0, min(max_transforms, len(candidate_transforms)) + 1))

    if num_to_apply > 0:
        selected = np.random.choice(candidate_transforms, size=num_to_apply, replace=False)
        for name in selected:
            if name == "random_crop":
                res = apply_random_crop(res)
            elif name == "add_noise":
                res = apply_random_noise(res)
            elif name == "h_flip":
                res = cv2.flip(res, 1)
            elif name == "v_flip":
                res = cv2.flip(res, 0)
            elif name == "morphological_mask":
                res = apply_morphological_mask(res)

    return res


class BoxAugStandardAugmentor(Augmentor):
    """Full implementation of BoxAug paper data augmentation algorithm."""

    name: str = "boxaug_standard"

    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: Any = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply boxaug synthesis to a single image if instance crops are available."""
        return image, bboxes

    def generate_dataset(
        self,
        input_dir: Path | str | None = None,
        output_dir: Path | str | None = None,
        config: Any = None,
    ) -> Path:
        """Generate balanced dataset split via BoxAug paper algorithm."""
        if config is not None and not isinstance(config, BoxAugStandardConfig):
            raise TypeError(f"BoxAugStandardConfig expected, got {type(config).__name__}")
        cfg = config if isinstance(config, BoxAugStandardConfig) else BoxAugStandardConfig()

        src_dir = Path(input_dir or (SPLIT_DATASET / "train"))
        target_dir = Path(output_dir)

        out_img_dir = target_dir / "train" / "images"
        out_lbl_dir = target_dir / "train" / "labels"
        for stale_dir in (out_img_dir, out_lbl_dir):
            if stale_dir.exists():
                shutil.rmtree(stale_dir)
            stale_dir.mkdir(parents=True, exist_ok=True)

        pairs = find_image_label_pairs(src_dir)
        if not pairs:
            raise FileNotFoundError(f"No image/label pairs found in {src_dir}")

        logger.info("building_boxaug_instance_bank", source=str(src_dir))
        instance_bank: dict[int, list[tuple[np.ndarray, float, float]]] = defaultdict(list)
        class_counts: dict[int, int] = defaultdict(int)

        for img_p, lbl_p in pairs:
            shutil.copy2(img_p, out_img_dir / img_p.name)
            shutil.copy2(lbl_p, out_lbl_dir / lbl_p.name)

            img = read_image(img_p)
            img_h, img_w = img.shape[:2]
            bboxes = read_yolo_labels(lbl_p)

            for b in bboxes:
                class_counts[b.class_id] += 1
                x1, y1, x2, y2 = b.to_xyxy(img_w, img_h)
                crop = img[y1:y2, x1:x2].copy()
                if crop.shape[0] >= 4 and crop.shape[1] >= 4:
                    instance_bank[b.class_id].append((crop, b.w, b.h))

        majority_count = max(class_counts.values()) if class_counts else 0
        target_count = int(round(majority_count * cfg.target_ratio))

        logger.info(
            "boxaug_standard_targets",
            majority_count=majority_count,
            target_per_minority=target_count,
            bank_sizes={ID_TO_CLASS[cid]: len(crops) for cid, crops in instance_bank.items()},
        )

        aug_counter = 0

        for class_id in sorted(class_counts.keys()):
            if class_id not in ID_TO_CLASS:
                raise ValueError(f"Unknown class_id {class_id} in BoxAug instance bank")
            cls_name = ID_TO_CLASS[class_id]
            current = class_counts[class_id]

            if current >= target_count or not instance_bank[class_id]:
                continue

            needed = target_count - current
            logger.info("boxaug_augmenting_class", class_name=cls_name, current=current, needed=needed)

            working: dict[str, tuple[np.ndarray, list[BBox]]] = {}

            produced = 0
            pair_idx = 0
            pair_tries = 0
            max_pair_tries = max(needed * cfg.max_location_attempts, 1)
            while produced < needed:
                if pair_tries >= max_pair_tries:
                    raise RuntimeError(
                        f"BoxAug failed to place {needed - produced} remaining instances "
                        f"for class {cls_name} after {pair_tries} pair tries"
                    )
                img_p, lbl_p = pairs[pair_idx % len(pairs)]
                pair_idx += 1
                pair_tries += 1

                if img_p.name not in working:
                    working[img_p.name] = (read_image(img_p), read_yolo_labels(lbl_p))
                img, curr_bboxes = working[img_p.name]
                img_h, img_w = img.shape[:2]

                crops_list = instance_bank[class_id]
                crop_raw, orig_w_norm, orig_h_norm = crops_list[np.random.randint(0, len(crops_list))]

                transformed_crop = transform_box_crop(crop_raw, max_transforms=cfg.max_num_transforms)
                tc_h, tc_w = transformed_crop.shape[:2]

                box_w_norm = tc_w / img_w
                box_h_norm = tc_h / img_h

                placed = False
                for _ in range(cfg.max_location_attempts):
                    cx, cy = sample_spatial_location(cls_name, box_w_norm, box_h_norm)
                    candidate_box = BBox(class_id=class_id, cx=cx, cy=cy, w=box_w_norm, h=box_h_norm)

                    overlap = any(check_overlap(candidate_box, b) for b in curr_bboxes)
                    if not overlap:
                        x1, y1, x2, y2 = candidate_box.to_xyxy(img_w, img_h)
                        pw, ph = x2 - x1, y2 - y1
                        if pw > 0 and ph > 0:
                            resized_crop = cv2.resize(transformed_crop, (pw, ph))
                            img[y1:y2, x1:x2] = resized_crop
                            actual_box = BBox.from_xyxy(x1, y1, x2, y2, img_w, img_h, class_id=class_id)
                            curr_bboxes.append(actual_box)
                            placed = True
                            break

                if placed:
                    working[img_p.name] = (img, curr_bboxes)
                    class_counts[class_id] += 1
                    produced += 1
                    aug_counter += 1

            for key, (final_img, final_boxes) in working.items():
                write_image(out_img_dir / key, final_img)
                write_yolo_labels(out_lbl_dir / (Path(key).stem + ".txt"), final_boxes)

        logger.info(
            "boxaug_standard_complete",
            total_paste_operations=aug_counter,
            final_counts={ID_TO_CLASS[cid]: cnt for cid, cnt in class_counts.items()},
        )
        return target_dir


register_augmentation("boxaug_standard", BoxAugStandardAugmentor)
