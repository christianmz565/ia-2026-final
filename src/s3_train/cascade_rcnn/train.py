"""Main training script using MMDetection 3.x framework for Cascade R-CNN Baseline.

Executes complete MMDetection pipeline:
1. Data sanitization & report generation (discarding corrupt files and invalid bboxes).
2. MMDetection Config building (Cascade R-CNN + ConvNeXt + PAFPN).
3. CUDA & AMP optimization setup.
4. MMEngine Runner execution with Early Stopping and per-epoch evaluation.
5. Summary report generation and standardized artifact exporting (tqdm, history.json, epoch timing, per-class mAP, best.pt).
"""

from __future__ import annotations

import json
import shutil
import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

import mmdet.models  # noqa: F401 — registers CascadeRCNN in mmengine registry
from mmengine.runner import Runner

from src.constants import CLASS_NAMES, TRAIN_SPLIT, VALID_SPLIT
from src.s3_train.cascade_rcnn.config import parse_config
from src.s3_train.cascade_rcnn.dataset import DataSanitizer
from src.s3_train.cascade_rcnn.mmdet_config import build_mmdet_config
from src.s3_train.cascade_rcnn.utils import (
    configure_cuda_optimizations,
    set_seed,
    setup_logger,
)
from src.s3_train.common import (
    create_epoch_pbar,
    format_per_class_map,
    save_epoch_history,
    save_summary_reports,
    setup_training_output_dir,
)

if TYPE_CHECKING:
    from src.s3_train.cascade_rcnn.config import PipelineConfig


def run_pipeline(config: PipelineConfig | None = None) -> dict[str, Any]:
    """Execute main MMDetection Cascade R-CNN baseline training pipeline.

    Args:
        config: Optional PipelineConfig. If None, parsed from CLI args.

    Returns:
        Summary metrics dictionary.
    """
    if config is None:
        config = parse_config()

    output_dir = Path(config.dataset.output_dir)
    out_dir, checkpoints_dir = setup_training_output_dir(output_dir)

    logger = setup_logger(out_dir)
    logger.info("==========================================================")
    logger.info("  MMDETECTION CASCADE R-CNN BASELINE PIPELINE STARTING    ")
    logger.info("==========================================================")

    set_seed(config.training.seed)
    _device = configure_cuda_optimizations(benchmark=config.training.cudnn_benchmark)

    config.save_json(out_dir / "pipeline_config.json")

    logger.info("--- PHASE 1: DATASET SANITIZATION & INSPECTION ---")
    train_data_dir = config.dataset.data_dir / TRAIN_SPLIT
    val_data_dir = config.dataset.data_dir / VALID_SPLIT
    train_sanitizer = DataSanitizer(data_dir=train_data_dir)
    val_sanitizer = DataSanitizer(data_dir=val_data_dir)

    train_coco, train_stats = train_sanitizer.sanitize_coco(config.dataset.train_json)
    val_coco, val_stats = val_sanitizer.sanitize_coco(config.dataset.val_json)

    train_sanitizer.save_report(
        stats={
            "train_set": train_stats,
            "val_set": val_stats,
        },
        output_json=out_dir / "sanitization_report.json",
        output_md=out_dir / "sanitization_report.md",
    )

    logger.info(
        f"Train set: {train_stats['valid_images_retained']} valid images ({train_stats['valid_annotations_retained']} annotations)"
    )
    logger.info(
        f"Val set: {val_stats['valid_images_retained']} valid images ({val_stats['valid_annotations_retained']} annotations)"
    )

    sanitized_train_json = out_dir / "sanitized_train.json"
    sanitized_val_json = out_dir / "sanitized_val.json"
    with open(sanitized_train_json, "w", encoding="utf-8") as f:
        json.dump(train_coco, f)
    with open(sanitized_val_json, "w", encoding="utf-8") as f:
        json.dump(val_coco, f)

    config.dataset.train_json = sanitized_train_json
    config.dataset.val_json = sanitized_val_json

    logger.info("--- PHASE 2: BUILDING MMDETECTION CONFIG (Cascade R-CNN + ConvNeXt + PAFPN) ---")
    mmdet_cfg = build_mmdet_config(config)

    logger.info("--- PHASE 3: EXECUTING MMDETECTION RUNNER ---")
    start_total_time = time.time()

    pbar = create_epoch_pbar(config.training.epochs, "Cascade R-CNN")
    runner = Runner.from_cfg(mmdet_cfg)
    logger.info("Starting MMDetection training runner with AMP enabled...")

    try:
        runner.train()
    finally:
        pbar.update(config.training.epochs)
        pbar.close()

    total_pipeline_time_sec = time.time() - start_total_time

    metrics_file = out_dir / "vis_data" / "scalars.json"
    history: list[dict[str, Any]] = []

    if metrics_file.exists():
        with open(metrics_file, encoding="utf-8") as f:
            for line in f:
                try:
                    record = json.loads(line.strip())
                    if "coco/bbox_mAP" in record:
                        mAP_50_95 = record["coco/bbox_mAP"]
                        mAP_50 = record.get("coco/bbox_mAP_50", 0.0)
                        epoch = record.get("step", len(history) + 1)
                        epoch_duration = round(
                            float(record.get("time", total_pipeline_time_sec / max(1, config.training.epochs))), 2
                        )

                        raw_per_class: dict[str, float] = {}
                        for name in CLASS_NAMES:
                            for k, v in record.items():
                                if name.lower() in k.lower() and isinstance(v, (int, float)):
                                    raw_per_class[name] = float(v)
                                    break

                        val_per_class = format_per_class_map(raw_per_class)

                        history.append(
                            {
                                "epoch": epoch,
                                "epoch_time_sec": epoch_duration,
                                "train_loss": round(float(record.get("loss", 0.0)), 4),
                                "val_loss": 0.0,
                                "val_mAP_50": round(float(mAP_50), 4),
                                "val_mAP_50_95": round(float(mAP_50_95), 4),
                                "val_per_class_mAP": val_per_class,
                            }
                        )
                except Exception:
                    pass

    save_epoch_history(out_dir, history)

    best_ckpts = list(out_dir.glob("best_coco_bbox_mAP_epoch_*.pth"))
    if not best_ckpts:
        best_ckpts = list(out_dir.glob("epoch_*.pth"))
    best_checkpoint = best_ckpts[0] if best_ckpts else out_dir / "best.pt"

    for epoch_ckpt in out_dir.glob("epoch_*.pth"):
        shutil.copy2(epoch_ckpt, checkpoints_dir / epoch_ckpt.name)

    logger.info("--- PHASE 4: FINAL DELIVERABLES & SUMMARY REPORT ---")
    summary = save_summary_reports(
        output_dir=out_dir,
        pipeline_name="MMDetection Cascade R-CNN Baseline (ConvNeXt + PAFPN)",
        total_time_sec=total_pipeline_time_sec,
        target_epochs=config.training.epochs,
        history=history,
        best_checkpoint=best_checkpoint,
    )

    logger.info("==========================================================")
    logger.info(f" MMDETECTION PIPELINE COMPLETED IN {total_pipeline_time_sec / 3600.0:.2f} HOURS ")
    logger.info("==========================================================")

    return summary


if __name__ == "__main__":
    run_pipeline()
