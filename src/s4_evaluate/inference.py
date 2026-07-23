"""Run RF-DETR inference on test set with timing measurements.

Loads a trained checkpoint, runs inference on all test images, and produces
a COCO-format predictions JSON for downstream metric computation.

Standalone usage:
    uv run python -m src.s4_evaluate.inference [--model-path PATH] [--data-dir PATH]
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import TYPE_CHECKING

import cv2
import numpy as np
import structlog
import torch

from src.caching import run_cached_step
from src.coco_utils import SUPPORTED_IMAGE_SUFFIXES
from src.constants import S4_OUTPUT

if TYPE_CHECKING:
    from rfdetr.detr import RFDETRLarge

logger = structlog.get_logger(__name__)


def _find_checkpoint(model_path: Path) -> Path:
    """Resolve the best checkpoint from a directory or file path."""
    if model_path.is_file():
        return model_path
    best = model_path / "best_model.pth"
    if best.exists():
        return best
    checkpoints = list(model_path.glob("*.pth"))
    if not checkpoints:
        raise FileNotFoundError(f"No .pth checkpoints found in {model_path}")
    return max(checkpoints, key=lambda p: p.stat().st_mtime)


def _build_coco_predictions(coco_gt: dict, image_detections: dict[int, list[dict]]) -> dict:
    """Build a COCO-format predictions dict from per-image detections.

    Args:
        coco_gt: Ground truth COCO dict with ``images``, ``categories``.
        image_detections: Mapping from image_id to list of detection dicts
            with keys ``category_id``, ``bbox``, ``score``.

    Returns:
        COCO-format predictions dict.
    """
    anns: list[dict] = []
    ann_id = 0
    for img_id, dets in image_detections.items():
        for det in dets:
            anns.append(
                {
                    "id": ann_id,
                    "image_id": img_id,
                    "category_id": det["category_id"],
                    "bbox": det["bbox"],
                    "area": det["area"],
                    "score": det["score"],
                }
            )
            ann_id += 1
    return {
        "images": coco_gt["images"],
        "annotations": anns,
        "categories": coco_gt["categories"],
    }


def _measure_latency(
    model: RFDETRLarge, image_paths: list[Path], num_warmup: int = 5, num_runs: int = 50
) -> dict[str, float]:
    """Measure inference latency in milliseconds."""
    for p in image_paths[:num_warmup]:
        img = cv2.imread(str(p))
        if img is not None:
            model.predict(img, threshold=0.3)

    latencies: list[float] = []
    for p in image_paths[num_warmup : num_warmup + num_runs]:
        img = cv2.imread(str(p))
        if img is None:
            continue
        start = time.perf_counter()
        model.predict(img, threshold=0.3)
        elapsed_ms = (time.perf_counter() - start) * 1000
        latencies.append(elapsed_ms)

    if not latencies:
        return {"latency_ms_mean": 0.0, "latency_ms_std": 0.0}
    arr = np.array(latencies)
    return {
        "latency_ms_mean": round(float(arr.mean()), 2),
        "latency_ms_std": round(float(arr.std()), 2),
    }


def run_inference(
    model_path: Path | str,
    data_dir: Path | str,
    output_path: Path | str | None = None,
    device: str = "cuda:0",
    conf_threshold: float = 0.25,
    force: bool = False,
) -> dict[str, object]:
    """Run RF-DETR inference and produce COCO-format predictions.

    Args:
        model_path: Path to trained checkpoint (.pth) or directory containing one.
        data_dir: Directory with test split (expects ``images/`` and ``_annotations.coco.json``).
        output_path: Where to save prediction results JSON.
        device: Device string for inference.
        conf_threshold: Confidence threshold for detections.
        force: If True, bypass cache and re-run inference.

    Returns:
        Dict with keys: predictions_path, total_time_ms, avg_time_ms,
        num_images, num_detections, latency_ms_mean, latency_ms_std.
    """
    data_dir = Path(data_dir)
    resolved_output = Path(output_path or S4_OUTPUT / "predictions.json")

    def _do_inference() -> dict[str, object]:
        from rfdetr.detr import RFDETRLarge

        checkpoint = _find_checkpoint(Path(model_path))
        logger.info("inference_load_checkpoint", path=str(checkpoint), device=device)

        rfdetr_model = RFDETRLarge()
        rfdetr_model.model = torch.load(str(checkpoint), map_location=device, weights_only=False)
        rfdetr_model.model.eval()

        ann_path = data_dir / "_annotations.coco.json"
        if not ann_path.exists():
            raise FileNotFoundError(f"COCO annotations not found: {ann_path}. Run yolo_to_coco first.")

        coco_gt = json.loads(ann_path.read_text())
        img_id_map: dict[str, int] = {img["file_name"]: img["id"] for img in coco_gt["images"]}

        images_dir = data_dir / "images"
        image_detections: dict[int, list[dict]] = {}
        num_images = 0
        total_detections = 0

        inf_start = time.perf_counter()
        for img_path in sorted(images_dir.iterdir()):
            if img_path.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
                continue
            file_name = f"images/{img_path.name}"
            if file_name not in img_id_map:
                continue
            img_id = img_id_map[file_name]
            num_images += 1

            img = cv2.imread(str(img_path))
            if img is None:
                continue

            detections = rfdetr_model.predict(img, threshold=conf_threshold)
            if isinstance(detections, list):
                detections = detections[0]
            if detections.confidence is None or detections.class_id is None:
                continue
            dets: list[dict] = []
            for i in range(len(detections)):
                x1, y1, x2, y2 = detections.xyxy[i]
                conf = float(detections.confidence[i])
                cls = int(detections.class_id[i])
                w = x2 - x1
                h = y2 - y1
                dets.append(
                    {
                        "category_id": cls + 1,
                        "bbox": [round(float(x1), 2), round(float(y1), 2), round(float(w), 2), round(float(h), 2)],
                        "area": round(float(w * h), 2),
                        "score": conf,
                    }
                )
                total_detections += 1
            image_detections[img_id] = dets
        total_time_ms = (time.perf_counter() - inf_start) * 1000

        predictions_dict = _build_coco_predictions(coco_gt, image_detections)
        resolved_output.parent.mkdir(parents=True, exist_ok=True)
        resolved_output.write_text(json.dumps(predictions_dict, indent=2))

        test_images = sorted(images_dir.glob("*.jpg"))
        latency = _measure_latency(rfdetr_model, test_images)

        result: dict[str, object] = {
            "predictions_path": str(resolved_output),
            "total_time_ms": round(total_time_ms, 2),
            "avg_time_ms": round(total_time_ms / max(num_images, 1), 2),
            "num_images": num_images,
            "num_detections": total_detections,
            **latency,
        }
        logger.info("inference_complete", **result)
        return result

    return run_cached_step(
        step_name="inference",
        target_path=resolved_output,
        fn=_do_inference,
        force=force,
        loader=lambda p: json.loads(p.read_text()),
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import EvalConfig

    standalone_main(
        config_model=EvalConfig,
        run_fn=lambda cfg: logger.info(
            "inference_result",
            **run_inference(cfg.model_path, cfg.data_dir, cfg.output_path or None, cfg.device, cfg.conf_threshold),
        ),
        description="Run RF-DETR inference",
        required_fields=["model_path", "data_dir"],
    )
