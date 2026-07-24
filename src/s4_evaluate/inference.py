"""Run model inference (YOLO26, Cascade R-CNN, RF-DETR) on test set with timing measurements.

Loads a trained checkpoint, runs inference on all test images, and produces
a COCO-format predictions JSON for downstream metric computation.

Standalone usage:
    uv run python -m src.s4_evaluate.inference [--model-path PATH] [--data-dir PATH]
"""

from __future__ import annotations

import json
import ssl
import time
from pathlib import Path
from typing import Any

import cv2
import structlog
import torch

# Fix SSL certificate verification if needed
ssl._create_default_https_context = ssl._create_unverified_context

# Monkeypatch mmcv version check for mmdet compatibility with mmcv 2.2.0
import mmcv  # noqa: E402

if getattr(mmcv, "__version__", "") >= "2.2.0":
    mmcv.__version__ = "2.1.0"

from src.caching import run_cached_step  # noqa: E402
from src.coco_utils import SUPPORTED_IMAGE_SUFFIXES  # noqa: E402
from src.constants import S4_OUTPUT  # noqa: E402

logger = structlog.get_logger(__name__)


def _find_checkpoint(model_path: Path) -> Path:
    """Resolve the best checkpoint from a directory or file path."""
    if model_path.is_file():
        return model_path
    best = model_path / "best.pt"
    if best.exists():
        return best
    best_pth = model_path / "best_model.pth"
    if best_pth.exists():
        return best_pth
    checkpoints = list(model_path.glob("*.pt")) + list(model_path.glob("*.pth"))
    if not checkpoints:
        raise FileNotFoundError(f"No checkpoint weights found in {model_path}")
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


def _detect_model_type(model_path: Path) -> str:
    """Identify model paradigm from path name or file extension."""
    path_str = str(model_path).lower()
    if "cascade" in path_str:
        return "cascade_rcnn"
    if "yolo" in path_str:
        return "yolo26"
    if "rf" in path_str or "detr" in path_str:
        return "rf_detr"

    if model_path.is_file():
        if model_path.suffix == ".pt":
            return "yolo26"
        if model_path.suffix == ".pth":
            return "cascade_rcnn"

    return "yolo26"


def run_inference(
    model_path: Path | str,
    data_dir: Path | str,
    output_path: Path | str | None = None,
    device: str | None = None,
    conf_threshold: float = 0.25,
    force: bool = False,
    resolution: int = 512,
) -> dict[str, object]:
    """Run model inference and produce COCO-format predictions.

    Supports YOLO26, Cascade R-CNN, and RF-DETR models.

    Args:
        model_path: Path to trained checkpoint or run output directory.
        data_dir: Directory with test split (expects ``images/`` and ``_annotations.coco.json``).
        output_path: Where to save prediction results JSON.
        device: Target device (e.g. 'cuda:0' or 'cpu').
        conf_threshold: Confidence threshold for detections.
        force: If True, bypass cache and re-run inference.

    Returns:
        Dict with keys: predictions_path, total_time_ms, avg_time_ms,
        num_images, num_detections.
    """
    model_path = Path(model_path)
    data_dir = Path(data_dir)
    resolved_output = Path(output_path or S4_OUTPUT / "predictions.json")

    resolved_device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")

    def _do_inference() -> dict[str, object]:
        checkpoint = _find_checkpoint(model_path)
        model_type = _detect_model_type(model_path)
        logger.info("inference_start", model_type=model_type, checkpoint=str(checkpoint), device=resolved_device)

        ann_path = data_dir / "_annotations.coco.json"
        if not ann_path.exists():
            from src.s1_prepare.convert_coco import convert_split

            convert_split(data_dir.parent if data_dir.name in ("train", "valid", "test") else data_dir, data_dir.name)

        if not ann_path.exists():
            raise FileNotFoundError(f"COCO annotations file not found: {ann_path}")

        coco_gt = json.loads(ann_path.read_text())
        img_id_map: dict[str, int] = {img["file_name"]: img["id"] for img in coco_gt["images"]}
        images_dir = data_dir / "images"

        image_detections: dict[int, list[dict]] = {}
        num_images = 0
        total_detections = 0

        inf_start = time.perf_counter()

        if model_type == "yolo26":
            from ultralytics import YOLO

            yolo_model = YOLO(str(checkpoint))
            for img_path in sorted(images_dir.iterdir()):
                if img_path.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
                    continue
                file_name = f"images/{img_path.name}"
                if file_name not in img_id_map:
                    continue
                img_id = img_id_map[file_name]
                num_images += 1

                results = yolo_model.predict(
                    str(img_path),
                    conf=conf_threshold,
                    device=resolved_device,
                    verbose=False,
                )
                res = results[0]
                dets: list[dict] = []
                if res.boxes is not None and len(res.boxes) > 0:
                    boxes = res.boxes.xyxy.cpu().numpy()
                    scores = res.boxes.conf.cpu().numpy()
                    clss = res.boxes.cls.cpu().numpy()
                    for box, score, cls in zip(boxes, scores, clss, strict=False):
                        x1, y1, x2, y2 = box
                        w, h = x2 - x1, y2 - y1
                        dets.append(
                            {
                                "category_id": int(cls) + 1,
                                "bbox": [
                                    round(float(x1), 2),
                                    round(float(y1), 2),
                                    round(float(w), 2),
                                    round(float(h), 2),
                                ],
                                "area": round(float(w * h), 2),
                                "score": round(float(score), 4),
                            }
                        )
                        total_detections += 1
                image_detections[img_id] = dets

        elif model_type == "cascade_rcnn":
            from mmdet.apis import inference_detector, init_detector

            from src.s3_train.cascade_rcnn import _get_cascade_rcnn_default_config

            cfg_file = _get_cascade_rcnn_default_config()
            mmdet_model = init_detector(str(cfg_file), str(checkpoint), device=resolved_device)

            for img_path in sorted(images_dir.iterdir()):
                if img_path.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
                    continue
                file_name = f"images/{img_path.name}"
                if file_name not in img_id_map:
                    continue
                img_id = img_id_map[file_name]
                num_images += 1

                res = inference_detector(mmdet_model, str(img_path))
                pred_instances = res.pred_instances
                dets: list[dict] = []
                if hasattr(pred_instances, "bboxes") and len(pred_instances.bboxes) > 0:
                    bboxes = pred_instances.bboxes.cpu().numpy()
                    scores = pred_instances.scores.cpu().numpy()
                    labels = pred_instances.labels.cpu().numpy()
                    for box, score, label in zip(bboxes, scores, labels, strict=False):
                        if float(score) < conf_threshold:
                            continue
                        x1, y1, x2, y2 = box
                        w, h = x2 - x1, y2 - y1
                        dets.append(
                            {
                                "category_id": int(label) + 1,
                                "bbox": [
                                    round(float(x1), 2),
                                    round(float(y1), 2),
                                    round(float(w), 2),
                                    round(float(h), 2),
                                ],
                                "area": round(float(w * h), 2),
                                "score": round(float(score), 4),
                            }
                        )
                        total_detections += 1
                image_detections[img_id] = dets

        else:  # rf_detr
            from rfdetr.detr import RFDETRMedium

            rfdetr_model = RFDETRMedium(resolution=resolution)
            rfdetr_model.model = torch.load(str(checkpoint), map_location=resolved_device, weights_only=False)
            rfdetr_model.model.eval()

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
                            "bbox": [
                                round(float(x1), 2),
                                round(float(y1), 2),
                                round(float(w), 2),
                                round(float(h), 2),
                            ],
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

        result: dict[str, Any] = {
            "predictions_path": str(resolved_output),
            "total_time_ms": round(total_time_ms, 2),
            "avg_time_ms": round(total_time_ms / max(num_images, 1), 2),
            "num_images": num_images,
            "num_detections": total_detections,
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
        description="Run detection inference",
        required_fields=["model_path", "data_dir"],
    )
