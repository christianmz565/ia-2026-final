"""Preprocess raw wood defect images: border cropping, downscaling, label filtering (parallelized).

Standalone usage:
    uv run python -m src.s1_prepare.preprocess [--input-dir PATH] [--output-dir PATH]
"""

from __future__ import annotations

import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import cv2
import numpy as np
import structlog
from tqdm import tqdm

from src.caching import run_cached_step
from src.config import PreprocessConfig
from src.constants import PROCESSED_DATASET, RAW_DATASET
from src.utils import BBox, find_image_label_pairs, read_yolo_labels, write_yolo_labels

logger = structlog.get_logger(__name__)


def crop_black_borders(img: np.ndarray, threshold: int = 10) -> tuple[np.ndarray, tuple[int, int, int, int]]:
    """Remove rightmost/leftmost/topmost/bottommost black borders around wood planks.

    Uses Otsu thresholding and morphological cleanup to isolate the valid wood plank region.

    Args:
        img: Input image array (H, W, 3) or (H, W).
        threshold: Fallback threshold parameter (retained for config compatibility).

    Returns:
        Tuple of (cropped_image, crop_box), where crop_box is (xmin, ymin, xmax, ymax)
        in original pixel coordinates.
    """
    h_orig, w_orig = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if img.ndim == 3 else img

    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    col_counts = np.sum(cleaned > 0, axis=0)
    col_indices = np.where(col_counts > h_orig * 0.05)[0]

    if len(col_indices) == 0:
        xmin, xmax = 0, w_orig
    else:
        xmin = int(col_indices[0])
        xmax = int(col_indices[-1]) + 1

    row_counts = np.sum(cleaned > 0, axis=1)
    row_indices = np.where(row_counts > w_orig * 0.05)[0]

    if len(row_indices) == 0:
        ymin, ymax = 0, h_orig
    else:
        ymin = int(row_indices[0])
        ymax = int(row_indices[-1]) + 1

    xmin, ymin = max(0, xmin), max(0, ymin)
    xmax, ymax = min(w_orig, xmax), min(h_orig, ymax)

    if xmax <= xmin or ymax <= ymin:
        return img, (0, 0, w_orig, h_orig)

    cropped_img = img[ymin:ymax, xmin:xmax]
    return cropped_img, (xmin, ymin, xmax, ymax)


def process_image_and_labels(
    img_path: Path,
    label_path: Path,
    config: PreprocessConfig,
) -> tuple[np.ndarray, list[BBox]] | tuple[None, list[BBox]]:
    """Crop black borders, downscale image by scale_factor, and filter labels < min_label_size_px.

    Args:
        img_path: Path to raw image file.
        label_path: Path to raw YOLO label file.
        config: Preprocessing parameters (scale_factor, min_label_size_px, black_threshold).

    Returns:
        Tuple of (processed_image, filtered_bboxes).
    """
    img = cv2.imread(str(img_path))
    if img is None:
        logger.warning("unreadable_image", path=str(img_path))
        return None, []

    h_orig, w_orig = img.shape[:2]
    cropped_img, (xmin, ymin, xmax, ymax) = crop_black_borders(img, threshold=config.black_threshold)

    w_crop = xmax - xmin
    h_crop = ymax - ymin

    w_final = max(1, int(round(w_crop * config.scale_factor)))
    h_final = max(1, int(round(h_crop * config.scale_factor)))

    downscaled_img = cv2.resize(cropped_img, (w_final, h_final), interpolation=cv2.INTER_AREA)

    bboxes_orig = read_yolo_labels(label_path)
    bboxes_final: list[BBox] = []

    for b in bboxes_orig:
        x1_orig = (b.cx - b.w / 2.0) * w_orig
        y1_orig = (b.cy - b.h / 2.0) * h_orig
        x2_orig = (b.cx + b.w / 2.0) * w_orig
        y2_orig = (b.cy + b.h / 2.0) * h_orig

        x1_crop = max(0.0, min(float(w_crop), x1_orig - xmin))
        y1_crop = max(0.0, min(float(h_crop), y1_orig - ymin))
        x2_crop = max(0.0, min(float(w_crop), x2_orig - xmin))
        y2_crop = max(0.0, min(float(h_crop), y2_orig - ymin))

        box_w_crop = x2_crop - x1_crop
        box_h_crop = y2_crop - y1_crop

        box_w_px = box_w_crop * config.scale_factor
        box_h_px = box_h_crop * config.scale_factor

        if box_w_px <= 0.0 or box_h_px <= 0.0:
            continue

        is_sub_minimum = (
            box_w_px < config.min_absolute_dim_px or box_h_px < config.min_absolute_dim_px
        )
        is_preserved = (
            (box_w_px * box_h_px >= config.min_label_area_px)
            or (max(box_w_px, box_h_px) >= config.min_elongated_dim_px)
        )
        if is_sub_minimum and not is_preserved:
            continue

        cx_norm = ((x1_crop + x2_crop) / 2.0) / w_crop
        cy_norm = ((y1_crop + y2_crop) / 2.0) / h_crop
        w_norm = box_w_crop / w_crop
        h_norm = box_h_crop / h_crop

        bboxes_final.append(
            BBox(
                class_id=b.class_id,
                cx=cx_norm,
                cy=cy_norm,
                w=w_norm,
                h=h_norm,
                confidence=b.confidence,
            )
        )

    return downscaled_img, bboxes_final


def _process_single_pair(
    task: tuple[Path, Path, PreprocessConfig, Path, Path],
) -> tuple[int, int]:
    """Worker function for parallel preprocessing of a single image-label pair."""
    img_path, label_path, config, out_images_dir, out_labels_dir = task
    processed_img, bboxes = process_image_and_labels(img_path, label_path, config)
    if processed_img is None:
        return 0, 0

    orig_boxes_count = len(read_yolo_labels(label_path)) if label_path.exists() else 0

    out_img_path = out_images_dir / img_path.name
    cv2.imwrite(str(out_img_path), processed_img)

    out_label_path = out_labels_dir / img_path.with_suffix(".txt").name
    write_yolo_labels(out_label_path, bboxes)

    return orig_boxes_count, len(bboxes)


def preprocess_dataset(
    config: PreprocessConfig | None = None,
    input_dir: Path | str | None = None,
    output_dir: Path | str | None = None,
    max_workers: int | None = None,
    force: bool = False,
) -> Path:
    """Execute preprocessing across all images and labels in input_dir in parallel.

    Args:
        config: Preprocessing configuration.
        input_dir: Input raw dataset path.
        output_dir: Output preprocessed dataset path.
        max_workers: Number of worker processes (defaults to CPU count).
        force: If True, bypass cache and re-process dataset.

    Returns:
        Path to output directory containing images/ and labels/ subdirectories.
    """
    config = config or PreprocessConfig()
    resolved_input = Path(input_dir or RAW_DATASET)
    resolved_output = Path(output_dir or PROCESSED_DATASET)

    def _preprocess() -> Path:
        out_images_dir = resolved_output / "images"
        out_labels_dir = resolved_output / "labels"
        out_images_dir.mkdir(parents=True, exist_ok=True)
        out_labels_dir.mkdir(parents=True, exist_ok=True)

        pairs = find_image_label_pairs(resolved_input)
        if not pairs:
            raise FileNotFoundError(f"No images found in {resolved_input}")

        workers = max_workers or os.cpu_count() or 4

        logger.info(
            "preprocessing_dataset_parallel",
            total_images=len(pairs),
            scale_factor=config.scale_factor,
            min_absolute_dim_px=config.min_absolute_dim_px,
            min_label_area_px=config.min_label_area_px,
            min_elongated_dim_px=config.min_elongated_dim_px,
            workers=workers,
        )

        tasks = [(img_path, label_path, config, out_images_dir, out_labels_dir) for img_path, label_path in pairs]

        total_orig_boxes = 0
        total_kept_boxes = 0

        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(_process_single_pair, task) for task in tasks]
            for future in tqdm(
                as_completed(futures),
                total=len(futures),
                desc="Preprocessing dataset (parallel)",
                unit="img",
            ):
                orig_c, kept_c = future.result()
                total_orig_boxes += orig_c
                total_kept_boxes += kept_c

        logger.info(
            "preprocessing_complete",
            total_images=len(pairs),
            orig_boxes=total_orig_boxes,
            kept_boxes=total_kept_boxes,
            removed_boxes=total_orig_boxes - total_kept_boxes,
            output_dir=str(resolved_output),
        )

        return resolved_output

    return run_cached_step(
        step_name="preprocess",
        target_path=resolved_output,
        fn=_preprocess,
        force=force,
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=PreprocessConfig,
        run_fn=lambda cfg: preprocess_dataset(cfg),
        description="Crop black borders, downscale 50%, filter <4px labels (parallel)",
    )
