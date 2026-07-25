"""BoxAug with libcom border blending and without noise/photometric modifications."""

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
from src.utils import (
    BBox,
    find_image_label_pairs,
    get_default_device,
    read_image,
    read_yolo_labels,
    write_image,
    write_yolo_labels,
)

logger = structlog.get_logger(__name__)


class BoxAugLibcomConfig(BaseModel):
    """Configuration for BoxAug with libcom border merging."""

    target_ratio: float = Field(default=1 / 3, description="Target minority-to-majority ratio")
    max_location_attempts: int = Field(default=50, description="Max spatial placement retries to prevent overlaps")
    blending_mode: str = Field(
        default="image_harmonization",
        description="libcom blending method: 'poisson', 'gaussian', 'color_transfer', 'painterly', 'image_harmonization', 'none'",
    )
    device: str = Field(
        default_factory=get_default_device,
        description="Target device for libcom models (e.g. 'cuda:0' or 'cpu')",
    )


def apply_geometric_only_transforms(crop: np.ndarray) -> np.ndarray:
    """Apply strictly geometric transforms (resize jitter and flips) without lighting/noise changes."""
    res = crop.copy()
    h, w = res.shape[:2]

    scale_factor = float(np.random.uniform(0.8, 1.2))
    new_w = max(4, int(round(w * scale_factor)))
    new_h = max(4, int(round(h * scale_factor)))
    res = cv2.resize(res, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    if np.random.rand() < 0.5:
        res = cv2.flip(res, 1)
    if np.random.rand() < 0.5:
        res = cv2.flip(res, 0)

    return res


class BoxAugLibcomAugmentor(Augmentor):
    """BoxAug implementation with libcom border merging and clean geometric transforms."""

    name: str = "boxaug_libcom"

    def __init__(self, device: str | None = None) -> None:
        self._painterly_model: Any = None
        self._harmonization_model: Any = None
        self._painterly_device: str | None = None
        self._harmonization_device: str | None = None
        self.device = device

    def _get_painterly_model(self, device: str = "cuda:0") -> Any:
        if self._painterly_model is None or self._painterly_device != device:
            try:
                from libcom import PainterlyHarmonizationModel

                logger.info("loading_libcom_painterly_model", device=device)
                self._painterly_model = PainterlyHarmonizationModel(device=device)
                self._painterly_device = device
            except Exception as err:
                logger.warning("painterly_model_load_failed", error=str(err))
                self._painterly_model = False
        return self._painterly_model

    def _get_harmonization_model(self, device: str = "cuda:0") -> Any:
        if self._harmonization_model is None or self._harmonization_device != device:
            try:
                from libcom import ImageHarmonizationModel

                logger.info("loading_libcom_harmonization_model", device=device)
                self._harmonization_model = ImageHarmonizationModel(device=device)
                self._harmonization_device = device
            except Exception as err:
                logger.warning("harmonization_model_load_failed", error=str(err))
                self._harmonization_model = False
        return self._harmonization_model


    def apply(
        self,
        image: np.ndarray,
        bboxes: list[BBox],
        config: Any = None,
    ) -> tuple[np.ndarray, list[BBox]]:
        """Apply augmentation to a single image if instance crops are available."""
        return image, bboxes

    def _blend_crop_into_background(
        self,
        bg_img: np.ndarray,
        fg_crop: np.ndarray,
        bbox_xyxy: tuple[int, int, int, int],
        blending_mode: str,
        device: str = "cuda:0",
    ) -> np.ndarray:
        """Use libcom or seamless cloning to merge foreground crop into background image."""
        import libcom

        x1, y1, x2, y2 = bbox_xyxy
        bw, bh = x2 - x1, y2 - y1

        if bw <= 0 or bh <= 0:
            return bg_img

        fg_resized = cv2.resize(fg_crop, (bw, bh))
        fg_mask = np.full((bh, bw), 255, dtype=np.uint8)
        bbox_list = [x1, y1, x2, y2]

        if blending_mode in ("poisson", "gaussian", "none"):
            comp_img, _ = libcom.get_composite_image(
                fg_resized,
                fg_mask,
                bg_img,
                bbox_list,
                option=blending_mode,
            )
            return comp_img

        elif blending_mode == "color_transfer":
            try:
                ct_crop = libcom.color_transfer(fg_resized, fg_mask, bg_img, bbox_list)
                comp_img, _ = libcom.get_composite_image(
                    ct_crop,
                    fg_mask,
                    bg_img,
                    bbox_list,
                    option="poisson",
                )
                return comp_img
            except Exception as err:
                logger.warning("color_transfer_failed_fallback_poisson", error=str(err))
                comp_img, _ = libcom.get_composite_image(
                    fg_resized,
                    fg_mask,
                    bg_img,
                    bbox_list,
                    option="poisson",
                )
                return comp_img

        elif blending_mode == "painterly":
            model = self._get_painterly_model(device=device)
            if model:
                try:
                    comp_img, _ = libcom.get_composite_image(fg_resized, fg_mask, bg_img, bbox_list, option="none")
                    comp_mask = np.zeros(bg_img.shape[:2], dtype=np.uint8)
                    comp_mask[y1:y2, x1:x2] = 255
                    harmonized = model(comp_img, comp_mask)
                    return harmonized
                except Exception as err:
                    logger.warning("painterly_harmonization_failed_fallback", error=str(err))

            comp_img, _ = libcom.get_composite_image(fg_resized, fg_mask, bg_img, bbox_list, option="poisson")
            return comp_img

        elif blending_mode == "image_harmonization":
            model = self._get_harmonization_model(device=device)
            if model:
                try:
                    comp_img, _ = libcom.get_composite_image(fg_resized, fg_mask, bg_img, bbox_list, option="none")
                    comp_mask = np.zeros(bg_img.shape[:2], dtype=np.uint8)
                    comp_mask[y1:y2, x1:x2] = 255
                    harmonized = model(comp_img, comp_mask)
                    return harmonized
                except Exception as err:
                    logger.warning("image_harmonization_failed_fallback", error=str(err))

            comp_img, _ = libcom.get_composite_image(fg_resized, fg_mask, bg_img, bbox_list, option="poisson")
            return comp_img

        else:
            comp_img, _ = libcom.get_composite_image(fg_resized, fg_mask, bg_img, bbox_list, option="poisson")
            return comp_img

    def generate_dataset(
        self,
        input_dir: Path | str | None = None,
        output_dir: Path | str | None = None,
        config: Any = None,
    ) -> Path:
        """Generate balanced dataset split via BoxAug with libcom border blending."""
        cfg = config if isinstance(config, BoxAugLibcomConfig) else BoxAugLibcomConfig()
        device = getattr(cfg, "device", self.device) or get_default_device()

        src_dir = Path(input_dir or (SPLIT_DATASET / "train"))
        target_dir = Path(output_dir)

        out_img_dir = target_dir / "train" / "images"
        out_lbl_dir = target_dir / "train" / "labels"
        out_img_dir.mkdir(parents=True, exist_ok=True)
        out_lbl_dir.mkdir(parents=True, exist_ok=True)

        pairs = find_image_label_pairs(src_dir)
        if not pairs:
            raise FileNotFoundError(f"No image/label pairs found in {src_dir}")

        logger.info(
            "building_boxaug_libcom_instance_bank",
            source=str(src_dir),
            mode=cfg.blending_mode,
            device=device,
        )
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
            "boxaug_libcom_targets",
            majority_count=majority_count,
            target_per_minority=target_count,
            blending_mode=cfg.blending_mode,
            device=device,
        )

        aug_counter = 0

        for class_id in sorted(class_counts.keys()):
            cls_name = ID_TO_CLASS.get(class_id, str(class_id))
            current = class_counts[class_id]

            if current >= target_count or not instance_bank[class_id]:
                continue

            needed = target_count - current
            logger.info("boxaug_libcom_augmenting_class", class_name=cls_name, current=current, needed=needed)

            produced = 0
            pair_idx = 0
            while produced < needed:
                img_p, lbl_p = pairs[pair_idx % len(pairs)]
                pair_idx += 1

                img = read_image(out_img_dir / img_p.name)
                img_h, img_w = img.shape[:2]
                curr_bboxes = read_yolo_labels(out_lbl_dir / img_p.with_suffix(".txt").name)

                crops_list = instance_bank[class_id]
                crop_raw, orig_w_norm, orig_h_norm = crops_list[np.random.randint(0, len(crops_list))]

                transformed_crop = apply_geometric_only_transforms(crop_raw)
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
                            blended_img = self._blend_crop_into_background(
                                img,
                                transformed_crop,
                                (x1, y1, x2, y2),
                                blending_mode=cfg.blending_mode,
                                device=device,
                            )
                            img = blended_img
                            curr_bboxes.append(candidate_box)
                            placed = True
                            break

                if placed:
                    write_image(out_img_dir / img_p.name, img)
                    write_yolo_labels(out_lbl_dir / img_p.with_suffix(".txt").name, curr_bboxes)
                    class_counts[class_id] += 1
                    produced += 1
                    aug_counter += 1

        logger.info(
            "boxaug_libcom_complete",
            total_paste_operations=aug_counter,
            final_counts={ID_TO_CLASS[cid]: cnt for cid, cnt in class_counts.items()},
        )
        return target_dir


register_augmentation("boxaug_libcom", BoxAugLibcomAugmentor)
