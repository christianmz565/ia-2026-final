"""Utility functions for PyTorch CUDA optimization, AMP, logging, COCO evaluation, and Early Stopping."""

import random
from pathlib import Path
from typing import Any

import numpy as np
import structlog
import torch
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

logger = structlog.get_logger(__name__)


def set_seed(seed: int = 42) -> None:
    """Set random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def configure_cuda_optimizations(benchmark: bool = True) -> torch.device:
    """Configure PyTorch CUDA flags for optimal performance on local NVIDIA GPU."""
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        torch.backends.cudnn.benchmark = benchmark
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
        device_name = torch.cuda.get_device_name(0)
        vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
        logger.info("CUDA Enabled", device=device_name, vram_gb=round(vram_gb, 2), benchmark=benchmark)
    else:
        device = torch.device("cpu")
        logger.warning("CUDA is NOT available. Running on CPU.")
    return device


def get_amp_scaler(enabled: bool = True) -> torch.amp.GradScaler:
    """Return PyTorch Automatic Mixed Precision (AMP FP16) GradScaler."""
    return torch.amp.GradScaler("cuda", enabled=enabled)


def setup_logger(output_dir: Path) -> structlog.stdlib.BoundLogger:
    """Configure logger instance for output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    return structlog.get_logger("CascadeRCNN")


class EarlyStopping:
    """Early stopping mechanism based on validation metric (e.g. mAP_50:95)."""

    def __init__(self, patience: int = 5, mode: str = "max", delta: float = 0.0001):
        self.patience = patience
        self.mode = mode
        self.delta = delta
        self.counter = 0
        self.best_score: float | None = None
        self.early_stop = False

    def __call__(self, current_score: float) -> bool:
        if self.best_score is None:
            self.best_score = current_score
            return True

        if self.mode == "max":
            improved = current_score > self.best_score + self.delta
        else:
            improved = current_score < self.best_score - self.delta

        if improved:
            self.best_score = current_score
            self.counter = 0
            return True
        else:
            self.counter += 1
            logger.info(
                "EarlyStopping counter update",
                counter=self.counter,
                patience=self.patience,
                best_score=self.best_score,
                current_score=current_score,
            )
            if self.counter >= self.patience:
                self.early_stop = True
            return False


@torch.no_grad()
def evaluate_coco_metrics(
    model: torch.nn.Module,
    val_loader: torch.utils.data.DataLoader,
    device: torch.device,
    val_coco_dict: dict[str, Any],
    amp_enabled: bool = True,
) -> dict[str, float]:
    """Evaluate object detection performance using COCO evaluation metrics (mAP_50, mAP_50:95)."""
    model.eval()

    tmp_coco_path = Path("/tmp/val_coco_eval_tmp.json")
    import json

    with open(tmp_coco_path, "w", encoding="utf-8") as f:
        json.dump(val_coco_dict, f)

    coco_gt = COCO(str(tmp_coco_path))

    categories = val_coco_dict.get("categories", [])
    label_to_cat_id = {i + 1: cat["id"] for i, cat in enumerate(categories)}

    coco_results = []

    for images, targets in val_loader:
        images = [img.to(device) for img in images]

        with torch.amp.autocast("cuda", enabled=amp_enabled and device.type == "cuda"):
            outputs = model(images)

        for target, output in zip(targets, outputs, strict=False):
            img_id = int(target["image_id"].item())
            boxes = output["boxes"].cpu().numpy()
            scores = output["scores"].cpu().numpy()
            labels = output["labels"].cpu().numpy()

            for box, score, label in zip(boxes, scores, labels, strict=False):
                xmin, ymin, xmax, ymax = box
                w = float(xmax - xmin)
                h = float(ymax - ymin)

                if w <= 0 or h <= 0:
                    continue

                cat_id = label_to_cat_id.get(int(label), int(label))
                coco_results.append(
                    {
                        "image_id": img_id,
                        "category_id": cat_id,
                        "bbox": [float(xmin), float(ymin), w, h],
                        "score": float(score),
                    }
                )

    if len(coco_results) == 0:
        logger.warning("No predictions produced by model during validation evaluation.")
        return {"mAP_50": 0.0, "mAP_50:95": 0.0}

    tmp_res_path = Path("/tmp/val_coco_results_tmp.json")
    with open(tmp_res_path, "w", encoding="utf-8") as f:
        json.dump(coco_results, f)

    coco_dt = coco_gt.loadRes(str(tmp_res_path))
    coco_eval = COCOeval(coco_gt, coco_dt, "bbox")
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    stats = coco_eval.stats
    mAP_50_95 = float(stats[0])
    mAP_50 = float(stats[1])

    return {"mAP_50": mAP_50, "mAP_50:95": mAP_50_95}
