"""Run model inference (YOLO26, Cascade R-CNN, RF-DETR) on test set with timing measurements.

Loads a trained checkpoint, runs inference on all test images, and produces
a COCO-format predictions JSON for downstream metric computation.

Standalone usage:
    uv run python -m src.s4_evaluate.inference [--model-path PATH] [--data-dir PATH]
"""

from __future__ import annotations

import json
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import cv2
import numpy as np
import structlog
import torch

from src.caching import config_fingerprint, run_cached_step
from src.coco_utils import SUPPORTED_IMAGE_SUFFIXES
from src.constants import (
    DEFAULT_CONF_THRESHOLD,
    DEFAULT_SEED,
    S4_OUTPUT,
    TARGET_IMG_HEIGHT,
    TARGET_IMG_WIDTH,
)
from src.utils import configure_torch_backend

logger = structlog.get_logger(__name__)



@contextmanager
def _weights_only_false_load():
    """Temporarily allow full-pickle ``torch.load`` for trusted local checkpoints."""
    orig_load = torch.load

    def _patched_load(*args, **kwargs):
        kwargs.setdefault("weights_only", False)
        return orig_load(*args, **kwargs)

    torch.load = _patched_load
    try:
        yield
    finally:
        torch.load = orig_load


_CHECKPOINT_PRIORITY = (
    "best_*.pt",
    "best_*.pth",
    "last_*.pt",
    "last_*.pth",
    "epoch_*.pt",
    "epoch_*.pth",
    "checkpoint*.pt",
    "checkpoint*.pth",
)


def _find_checkpoint(model_path: Path, explicit: Path | str | None = None) -> Path:
    """Resolve the best checkpoint from an explicit file or a directory."""
    if explicit:
        candidate = Path(explicit)
        if candidate.is_file() and candidate.stat().st_size > 0:
            return candidate
        raise FileNotFoundError(f"Explicit checkpoint not found or empty: {candidate}")
    if model_path.is_file():
        if model_path.stat().st_size > 0:
            return model_path
        raise FileNotFoundError(f"Checkpoint file is empty: {model_path}")
    for pattern in _CHECKPOINT_PRIORITY:
        matches = sorted(
            p for p in model_path.rglob(pattern) if p.is_file() and p.stat().st_size > 0
        )
        if len(matches) > 1:
            raise FileNotFoundError(
                f"Ambiguous checkpoints for {pattern!r} in {model_path}: {[str(p) for p in matches]}"
            )
        if matches:
            logger.info("checkpoint_selected", pattern=pattern, checkpoint=str(matches[0]))
            return matches[0]
    raise FileNotFoundError(f"No checkpoint weights found in {model_path}")



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

    raise ValueError(f"Cannot identify model paradigm from path: {model_path}")


def run_inference(
    model_path: Path | str,
    data_dir: Path | str,
    output_path: Path | str | None = None,
    device: str | None = None,
    conf_threshold: float = DEFAULT_CONF_THRESHOLD,
    max_images: int | None = None,
    force: bool = False,
    resolution: int = 512,
    checkpoint: Path | str | None = None,
    sample_seed: int | None = None,
    yolo_imgsz: list[int] | None = None,
) -> dict[str, object]:
    """Run model inference and produce COCO-format predictions.

    Supports YOLO26, Cascade R-CNN, and RF-DETR models.

    Args:
        model_path: Path to trained checkpoint or run output directory.
        data_dir: Directory with test split (expects ``images/`` and ``_annotations.coco.json``).
        output_path: Where to save prediction results JSON.
        device: Target device (e.g. 'cuda:0' or 'cpu').
        conf_threshold: Confidence threshold for detections.
        max_images: Optional maximum number of images to evaluate (seeded sample).
        force: If True, bypass cache and re-run inference.
        resolution: Input resolution for RF-DETR.
        checkpoint: Explicit checkpoint file; empty resolves by priority, ambiguity raises.
        sample_seed: Seed for ``max_images`` sampling (defaults to ``DEFAULT_SEED``).
        yolo_imgsz: ``[height, width]`` eval size for YOLO (defaults to training size).

    Returns:
        Dict with keys: predictions_path, total_inference_ms, avg_inference_ms,
        num_inferred_images, num_detections.
    """
    model_path = Path(model_path)
    data_dir = Path(data_dir)
    resolved_output = Path(output_path or S4_OUTPUT / "predictions.json")

    configure_torch_backend()
    resolved_device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")


    meta_output = resolved_output.parent / "inference_meta.json"

    def _do_inference() -> dict[str, object]:
        resolved_checkpoint = _find_checkpoint(model_path, explicit=checkpoint)
        model_type = _detect_model_type(model_path)
        resolved_yolo_imgsz = yolo_imgsz or [TARGET_IMG_HEIGHT, TARGET_IMG_WIDTH]
        logger.info(
            "inference_start",
            model_type=model_type,
            checkpoint=str(resolved_checkpoint),
            device=resolved_device,
            yolo_imgsz=resolved_yolo_imgsz,
            resolution=resolution,
        )

        ann_path = data_dir / "_annotations.coco.json"
        if not ann_path.exists():
            from src.s1_prepare.convert_coco import convert_split

            convert_split(data_dir.parent if data_dir.name in ("train", "valid", "test") else data_dir, data_dir.name)

        if not ann_path.exists():
            raise FileNotFoundError(f"COCO annotations file not found: {ann_path}")

        coco_gt = json.loads(ann_path.read_text())
        img_id_map: dict[str, int] = {img["file_name"]: img["id"] for img in coco_gt["images"]}
        images_dir = data_dir / "images"

        target_images = [
            p for p in sorted(images_dir.iterdir())
            if p.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES and f"images/{p.name}" in img_id_map
        ]
        if max_images and max_images > 0:
            seed = sample_seed if sample_seed is not None else DEFAULT_SEED
            order = np.random.default_rng([seed, 7]).permutation(len(target_images))
            target_images = [target_images[i] for i in sorted(order[:max_images])]
            logger.info("inference_sampled", count=len(target_images), seed=seed)

        image_detections: dict[int, list[dict]] = {}
        num_images = 0
        total_detections = 0

        inf_start = time.perf_counter()

        if model_type == "yolo26":
            from ultralytics import YOLO

            yolo_model = YOLO(str(resolved_checkpoint))
            for img_path in target_images:
                file_name = f"images/{img_path.name}"
                img_id = img_id_map[file_name]
                num_images += 1

                # Same input size as training ([target_height, target_width]); YOLO
                # is NMS-free by design, so conf_threshold is the operating control.
                results = yolo_model.predict(
                    str(img_path),
                    conf=conf_threshold,
                    device=resolved_device,
                    imgsz=resolved_yolo_imgsz,
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
                                "category_id": int(cls),
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
            import mmcv

            if getattr(mmcv, "__version__", "") >= "2.2.0":
                mmcv.__version__ = "2.1.0"

            from mmdet.apis import inference_detector, init_detector
            from mmengine.config import Config

            from src.constants import CLASS_NAMES
            from src.s3_train.cascade_rcnn import _get_cascade_rcnn_default_config

            cfg_file = _get_cascade_rcnn_default_config()
            cfg = Config.fromfile(str(cfg_file))
            num_classes = len(CLASS_NAMES)
            if hasattr(cfg.model, "roi_head") and hasattr(cfg.model.roi_head, "bbox_head"):
                bbox_heads = cfg.model.roi_head.bbox_head
                if isinstance(bbox_heads, list):
                    for head in bbox_heads:
                        head.num_classes = num_classes
                else:
                    bbox_heads.num_classes = num_classes

            # Same input size as training ((target_width, target_height), keep
            # ratio); Cascade has no NMS knob in this repo, so conf_threshold
            # is the operating control.
            target_scale = (TARGET_IMG_WIDTH, TARGET_IMG_HEIGHT)
            if hasattr(cfg, "test_pipeline"):
                for step in cfg.test_pipeline:
                    if isinstance(step, dict) and step.get("type") == "Resize":
                        step["scale"] = target_scale
                        step["keep_ratio"] = True

            with _weights_only_false_load():
                mmdet_model = init_detector(cfg, str(resolved_checkpoint), device=resolved_device)

            for img_path in target_images:
                file_name = f"images/{img_path.name}"
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
                                "category_id": int(label),
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

        else:
            from rfdetr.detr import RFDETRMedium

            from src.constants import CLASS_NAMES

            with _weights_only_false_load():
                rfdetr_model = RFDETRMedium(resolution=resolution)
                rfdetr_model.model.reinitialize_detection_head(num_classes=len(CLASS_NAMES))
                ckpt = torch.load(str(resolved_checkpoint), map_location=resolved_device, weights_only=False)
                state_dict = ckpt["model"] if isinstance(ckpt, dict) and "model" in ckpt else ckpt
                rfdetr_model.model.model.load_state_dict(state_dict)
                rfdetr_model.model.model.eval()

            for img_path in target_images:
                file_name = f"images/{img_path.name}"
                img_id = img_id_map[file_name]
                num_images += 1

                img = cv2.imread(str(img_path))
                if img is None:
                    continue
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                detections = rfdetr_model.predict(img_rgb, threshold=conf_threshold)
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
                            "category_id": cls,
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
            "total_inference_ms": round(total_time_ms, 2),
            "avg_inference_ms": round(total_time_ms / max(num_images, 1), 2),
            "num_inferred_images": num_images,
            "num_detections": total_detections,
        }
        meta_output.write_text(json.dumps(result, indent=2))
        logger.info("inference_complete", **result)
        return result

    def _load_cached() -> dict[str, object]:
        base = json.loads(resolved_output.read_text())
        if meta_output.exists():
            meta = json.loads(meta_output.read_text())
            base.update(meta)
        elif resolved_output.parent.exists():
            results_path = resolved_output.parent / "results.json"
            if results_path.exists():
                prev = json.loads(results_path.read_text())
                base["avg_inference_ms"] = prev["avg_inference_ms"]
                base["total_inference_ms"] = prev["total_inference_ms"]
                base["num_inferred_images"] = prev["num_inferred_images"]
        return base

    return run_cached_step(
        step_name="inference",
        target_path=resolved_output,
        fn=_do_inference,
        force=force,
        loader=lambda p: _load_cached(),
        fingerprint=config_fingerprint(
            {
                "model_path": str(model_path),
                "data_dir": str(data_dir),
                "conf_threshold": conf_threshold,
                "max_images": max_images,
                "resolution": resolution,
                "checkpoint": str(checkpoint) if checkpoint else "",
                "sample_seed": sample_seed,
                "yolo_imgsz": yolo_imgsz,
            }
        ),
    )


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from src.config import EvalConfig

    standalone_main(
        config_model=EvalConfig,
        run_fn=lambda cfg: logger.info(
            "inference_result",
            **run_inference(
                cfg.model_path,
                cfg.data_dir,
                cfg.output_path or None,
                cfg.device,
                cfg.conf_threshold,
                checkpoint=cfg.checkpoint or None,
                sample_seed=cfg.sample_seed,
            ),
        ),
        description="Run detection inference",
        required_fields=["model_path", "data_dir"],
    )
