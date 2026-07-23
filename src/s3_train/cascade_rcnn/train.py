"""Main training script using MMDetection 3.x framework for Cascade R-CNN Baseline.

Executes complete MMDetection pipeline:
1. Data sanitization & report generation (discarding corrupt files and invalid bboxes).
2. MMDetection Config building (Cascade R-CNN + ConvNeXt + PAFPN).
3. CUDA & AMP optimization setup.
4. MMEngine Runner execution with Early Stopping and per-epoch evaluation.
5. Summary report generation (sanitization, execution metrics, mAP_50, mAP_50:95).
"""

import json
import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.s3_train.cascade_rcnn.config import PipelineConfig

from mmengine.runner import Runner

from src.s3_train.cascade_rcnn.config import parse_config
from src.s3_train.cascade_rcnn.dataset import DataSanitizer
from src.s3_train.cascade_rcnn.mmdet_config import build_mmdet_config
from src.s3_train.cascade_rcnn.utils import (
    configure_cuda_optimizations,
    set_seed,
    setup_logger,
)


def run_pipeline(config: "PipelineConfig | None" = None) -> dict[str, Any]:
    """Execute main MMDetection Cascade R-CNN baseline training pipeline.

    Args:
        config: Optional PipelineConfig. If None, parsed from CLI args.
    """
    if config is None:
        config = parse_config()
    output_dir = Path(config.dataset.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = setup_logger(output_dir)
    logger.info("==========================================================")
    logger.info("  MMDETECTION CASCADE R-CNN BASELINE PIPELINE STARTING    ")
    logger.info("==========================================================")

    set_seed(config.training.seed)
    _device = configure_cuda_optimizations(benchmark=config.training.cudnn_benchmark)

    config.save_json(output_dir / "pipeline_config.json")

    logger.info("--- PHASE 1: DATASET SANITIZATION & INSPECTION ---")
    sanitizer = DataSanitizer(data_dir=config.dataset.data_dir)

    train_coco, train_stats = sanitizer.sanitize_coco(config.dataset.train_json)
    val_coco, val_stats = sanitizer.sanitize_coco(config.dataset.val_json)

    sanitizer.save_report(
        stats={
            "train_set": train_stats,
            "val_set": val_stats,
        },
        output_json=output_dir / "sanitization_report.json",
        output_md=output_dir / "sanitization_report.md",
    )

    logger.info(
        f"Train set: {train_stats['valid_images_retained']} valid images ({train_stats['valid_annotations_retained']} annotations)"
    )
    logger.info(
        f"Val set: {val_stats['valid_images_retained']} valid images ({val_stats['valid_annotations_retained']} annotations)"
    )

    sanitized_train_json = output_dir / "sanitized_train.json"
    sanitized_val_json = output_dir / "sanitized_val.json"
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

    runner = Runner.from_cfg(mmdet_cfg)
    logger.info("Starting MMDetection training runner...")
    runner.train()

    total_pipeline_time_sec = time.time() - start_total_time

    metrics_file = output_dir / "vis_data" / "scalars.json"
    history = []
    best_mAP_50_95 = 0.0
    best_epoch = 0

    if metrics_file.exists():
        with open(metrics_file, encoding="utf-8") as f:
            for line in f:
                try:
                    record = json.loads(line.strip())
                    if "coco/bbox_mAP" in record:
                        mAP_50_95 = record["coco/bbox_mAP"]
                        mAP_50 = record.get("coco/bbox_mAP_50", 0.0)
                        epoch = record.get("step", len(history) + 1)
                        history.append(
                            {
                                "epoch": epoch,
                                "val_mAP_50": mAP_50,
                                "val_mAP_50:95": mAP_50_95,
                            }
                        )
                        if mAP_50_95 > best_mAP_50_95:
                            best_mAP_50_95 = mAP_50_95
                            best_epoch = epoch
                except Exception:
                    pass

    logger.info("--- PHASE 4: FINAL DELIVERABLES & SUMMARY REPORT ---")
    summary = {
        "pipeline_name": "MMDetection Cascade R-CNN Baseline (ConvNeXt + PAFPN)",
        "framework": "MMDetection 3.3.0",
        "total_elapsed_seconds": total_pipeline_time_sec,
        "total_elapsed_hours": total_pipeline_time_sec / 3600.0,
        "epochs_completed": len(history) if history else config.training.epochs,
        "target_epochs": config.training.epochs,
        "average_epoch_time_seconds": total_pipeline_time_sec / max(1, config.training.epochs),
        "best_epoch": best_epoch,
        "final_val_mAP_50": history[-1]["val_mAP_50"] if history else 0.0,
        "final_val_mAP_50_95": history[-1]["val_mAP_50:95"] if history else 0.0,
        "best_val_mAP_50_95": best_mAP_50_95,
        "best_checkpoint_path": str(output_dir / "best_coco_bbox_mAP_epoch_*.pth"),
        "training_history": history,
    }

    with open(output_dir / "summary_report.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    summary_md = f"""# MMDetection Cascade R-CNN Baseline Summary Report

## 1. Overview
- **Framework:** MMDetection 3.3.0 + MMEngine 0.10.7
- **Model Architecture:** Cascade R-CNN (3 Stages: IoU 0.5, 0.6, 0.7)
- **Backbone:** ConvNeXt ({config.model.backbone_variant}) via MMPretrain
- **Neck:** PAFPN (Path Aggregation Feature Pyramid Network)
- **Pretrained Transfer Learning:** Enabled (COCO)
- **Data Policy:** Native Image Resolution (No Resizing, No Augmentations)
- **Automatic Mixed Precision (AMP):** {config.training.amp_enabled}
- **CUDA Benchmark:** {config.training.cudnn_benchmark}

## 2. Execution & Timing Summary
- **Total Elapsed Time:** {total_pipeline_time_sec / 3600.0:.2f} hours ({total_pipeline_time_sec / 60.0:.2f} minutes)
- **Target Epochs:** {config.training.epochs}
- **Average Time per Epoch:** {total_pipeline_time_sec / max(1, config.training.epochs):.1f} seconds

## 3. Evaluation Metrics
- **Best Epoch:** {best_epoch}
- **Best Validation $mAP_{{50:95}}$:** {best_mAP_50_95:.4f}
- **Final Validation $mAP_{{50}}$:** {history[-1]["val_mAP_50"] if history else 0.0:.4f}
- **Final Validation $mAP_{{50:95}}$:** {history[-1]["val_mAP_50:95"] if history else 0.0:.4f}

## 4. Output Artifacts
- **Output Directory:** `{output_dir}`
- **Sanitization Report:** `{output_dir / "sanitization_report.md"}`
- **Pipeline Logs:** `{output_dir / "training_pipeline.log"}`
"""
    with open(output_dir / "summary_report.md", "w", encoding="utf-8") as f:
        f.write(summary_md)

    logger.info("==========================================================")
    logger.info(f" MMDETECTION PIPELINE COMPLETED IN {total_pipeline_time_sec / 3600.0:.2f} HOURS ")
    logger.info("==========================================================")

    return summary


if __name__ == "__main__":
    run_pipeline()
