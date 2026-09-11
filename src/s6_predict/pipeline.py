"""s6_predict pipeline — single-image inference grid for all trained models.

Discovers all model checkpoints in partials/s3_train/, runs inference on a
single input image, and produces a grid visualization with bounding boxes drawn.

Standalone usage:
    uv run python -m src.s6_predict.pipeline --image-path /path/to/photo.jpg
    uv run python -m src.s6_predict.pipeline --image-path photo.jpg --conf-threshold 0.3
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import structlog
import torch

from src.constants import S3_OUTPUT, S6_OUTPUT
from src.s6_predict.draw import draw_detections

logger = structlog.get_logger(__name__)


def _discover_checkpoints() -> list[dict[str, Any]]:
    """Scan partials/s3_train/ and return all (model, augment, checkpoint) combos.

    Returns list of dicts with keys: model, augment, checkpoint (Path).
    """
    s3 = S3_OUTPUT
    if not s3.exists():
        return []

    combos: list[dict[str, Any]] = []

    for model_dir in sorted(s3.iterdir()):
        if not model_dir.is_dir():
            continue
        model_name = model_dir.name

        for aug_dir in sorted(model_dir.iterdir()):
            if not aug_dir.is_dir():
                continue
            augment_name = aug_dir.name

            # Collect all checkpoint files
            candidates: list[Path] = []

            # best.pt or best_model.pth at root (preferred)
            for name in ("best.pt", "best_model.pth"):
                p = aug_dir / name
                if p.exists():
                    candidates.append(p)

            # If no root checkpoint, check weights/ subdirectory
            if not candidates:
                weights_dir = aug_dir / "weights"
                if weights_dir.exists():
                    candidates.extend(sorted(weights_dir.glob("best.pt")))

            # epoch checkpoints at root level
            candidates.extend(sorted(aug_dir.glob("checkpoint*.pth")))
            candidates.extend(sorted(aug_dir.glob("epoch_*.pth")))
            candidates.extend(sorted(aug_dir.glob("epoch_*.pt")))
            candidates.extend(sorted(aug_dir.glob("best_*.pth")))

            # Deduplicate by file size + name to avoid root/weights duplicates
            seen_names: set[str] = set()
            for ckpt in candidates:
                # Use stem to catch root/best.pt vs weights/best.pt
                key = ckpt.stem
                if key in seen_names:
                    continue
                seen_names.add(key)
                combos.append({
                    "model": model_name,
                    "augment": augment_name,
                    "checkpoint": ckpt,
                })

    return combos


def _detect_model_type(model_path: Path, model_dir_name: str) -> str:
    """Identify model paradigm from path or parent directory name."""
    name = model_dir_name.lower()
    path_str = str(model_path).lower()

    if "cascade" in name or "cascade" in path_str:
        return "cascade_rcnn"
    if "yolo" in name or "yolo" in path_str:
        return "yolo26"
    if "rf" in name or "detr" in name or "rf" in path_str or "detr" in path_str:
        return "rf_detr"

    if model_path.is_file():
        if model_path.suffix == ".pt":
            return "yolo26"
        if model_path.suffix == ".pth":
            return "cascade_rcnn"

    return "yolo26"


def _load_and_infer(
    model_type: str,
    checkpoint: Path,
    image: np.ndarray,
    device: str,
    conf_threshold: float,
) -> list[dict]:
    """Load a model and run inference on a single image. Returns list of detection dicts."""
    h, w = image.shape[:2]
    detections: list[dict] = []

    if model_type == "yolo26":
        from ultralytics import YOLO

        yolo_model = YOLO(str(checkpoint))
        results = yolo_model.predict(
            image,
            conf=conf_threshold,
            device=device,
            verbose=False,
        )
        res = results[0]
        if res.boxes is not None and len(res.boxes) > 0:
            boxes = res.boxes.xyxy.cpu().numpy()
            scores = res.boxes.conf.cpu().numpy()
            clss = res.boxes.cls.cpu().numpy()
            for box, score, cls in zip(boxes, scores, clss, strict=False):
                x1, y1, x2, y2 = box
                bw, bh = x2 - x1, y2 - y1
                detections.append({
                    "category_id": int(cls),
                    "bbox": [round(float(x1), 2), round(float(y1), 2), round(float(bw), 2), round(float(bh), 2)],
                    "score": round(float(score), 4),
                })

    elif model_type == "cascade_rcnn":
        import mmcv

        if getattr(mmcv, "__version__", "") >= "2.2.0":
            mmcv.__version__ = "2.1.0"

        from mmdet.apis import inference_detector, init_detector
        from src.s3_train.cascade_rcnn import _get_cascade_rcnn_default_config

        cfg_file = _get_cascade_rcnn_default_config()
        try:
            mmdet_model = init_detector(str(cfg_file), str(checkpoint), device=device)
        except Exception:
            logger.warning("cascade_rcnn_checkpoint_invalid_using_pretrained", checkpoint=str(checkpoint))
            mmdet_model = init_detector(str(cfg_file), None, device=device)
        res = inference_detector(mmdet_model, image)
        pred_instances = res.pred_instances
        if hasattr(pred_instances, "bboxes") and len(pred_instances.bboxes) > 0:
            bboxes = pred_instances.bboxes.cpu().numpy()
            scores = pred_instances.scores.cpu().numpy()
            labels = pred_instances.labels.cpu().numpy()
            for box, score, label in zip(bboxes, scores, labels, strict=False):
                if float(score) < conf_threshold:
                    continue
                x1, y1, x2, y2 = box
                bw, bh = x2 - x1, y2 - y1
                detections.append({
                    "category_id": int(label),
                    "bbox": [round(float(x1), 2), round(float(y1), 2), round(float(bw), 2), round(float(bh), 2)],
                    "score": round(float(score), 4),
                })

    else:  # rf_detr
        from rfdetr.detr import RFDETRMedium

        rfdetr_model = RFDETRMedium(resolution=512)
        try:
            state_dict = torch.load(str(checkpoint), map_location=device, weights_only=False)
            if isinstance(state_dict, dict) and "model" in state_dict:
                rfdetr_model.model.load_state_dict(state_dict["model"])
            elif isinstance(state_dict, dict):
                rfdetr_model.model.load_state_dict(state_dict)
            rfdetr_model.model.eval()
        except Exception:
            logger.warning("rf_detr_checkpoint_invalid_using_pretrained", checkpoint=str(checkpoint))
            rfdetr_model = RFDETRMedium(resolution=512)

        detections_rf = rfdetr_model.predict(image, threshold=conf_threshold)
        if isinstance(detections_rf, list):
            detections_rf = detections_rf[0]
        if detections_rf.confidence is not None and detections_rf.class_id is not None:
            for i in range(len(detections_rf)):
                x1, y1, x2, y2 = detections_rf.xyxy[i]
                conf = float(detections_rf.confidence[i])
                cls = int(detections_rf.class_id[i])
                bw, bh = x2 - x1, y2 - y1
                detections.append({
                    "category_id": cls,
                    "bbox": [round(float(x1), 2), round(float(y1), 2), round(float(bw), 2), round(float(bh), 2)],
                    "score": round(float(conf), 4),
                })

    return detections


def _build_grid(
    results: list[dict[str, Any]],
    *,
    cell_size: tuple[int, int] = (400, 200),
    dpi: int = 100,
) -> matplotlib.figure.Figure:
    """Build a matplotlib grid figure from inference results.

    Args:
        results: List of dicts with keys: model, augment, checkpoint, image (np.ndarray).
        cell_size: (width, height) per cell in pixels.
        dpi: Resolution of the output figure.

    Returns:
        Matplotlib figure with the grid.
    """
    n = len(results)
    if n == 0:
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.text(0.5, 0.5, "No checkpoints found", ha="center", va="center", fontsize=14)
        ax.axis("off")
        return fig

    cols = min(n, 3)
    rows = (n + cols - 1) // cols

    fig_w = cols * cell_size[0] / dpi
    fig_h = rows * cell_size[1] / dpi
    fig, axes = plt.subplots(
        rows, cols,
        figsize=(fig_w, fig_h),
        dpi=dpi,
        gridspec_kw={"wspace": 0.05, "hspace": 0.15},
    )

    if rows == 1 and cols == 1:
        axes = [[axes]]
    elif rows == 1:
        axes = [axes]
    elif cols == 1:
        axes = [[ax] for ax in axes]

    for idx, res in enumerate(results):
        r, c = divmod(idx, cols)
        ax = axes[r][c]
        # Convert BGR to RGB for matplotlib
        img_rgb = cv2.cvtColor(res["image"], cv2.COLOR_BGR2RGB)
        ax.imshow(img_rgb)

        ckpt_name = res["checkpoint"].stem
        remove_parts = ["_best_model", "_best", "_last_model", "_last", "best_model", "best", "last_model", "last"]
        for part in remove_parts:
            if ckpt_name == part:
                ckpt_name = ""
                break
            if ckpt_name.endswith(part):
                ckpt_name = ckpt_name[: -len(part)]
                break
        label = f"{res['model']}/{res['augment']}"
        if ckpt_name:
            label += f"\n{ckpt_name}"
        ax.set_title(label, fontsize=8, pad=2)
        ax.axis("off")

    # Hide unused axes
    for idx in range(n, rows * cols):
        r, c = divmod(idx, cols)
        axes[r][c].axis("off")

    fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.01)
    return fig


def run_pipeline(
    image_path: str,
    output_dir: str | Path | None = None,
    conf_threshold: float = 0.25,
    device: str | None = None,
) -> Path:
    """Run single-image inference with all discovered checkpoints and produce grid.

    Args:
        image_path: Path to input image.
        output_dir: Where to save outputs. Defaults to partials/s6_predict/images/{image_stem}/.
        conf_threshold: Minimum detection confidence.
        device: Target device.

    Returns:
        Path to the output grid image.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {image_path}")

    image_stem = Path(image_path).stem
    base_output = Path(output_dir) if output_dir else S6_OUTPUT
    resolved_output = base_output / "images" / image_stem
    resolved_output.mkdir(parents=True, exist_ok=True)

    resolved_device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")

    logger.info("s6_predict_start", image=image_path, device=resolved_device, output_dir=str(resolved_output))

    combos = _discover_checkpoints()
    if not combos:
        logger.warning("s6_no_checkpoints_found")
        return resolved_output

    logger.info("s6_checkpoints_found", count=len(combos))

    results: list[dict[str, Any]] = []

    for combo in combos:
        model_name = combo["model"]
        aug_name = combo["augment"]
        ckpt = combo["checkpoint"]
        model_type = _detect_model_type(ckpt, model_name)

        logger.info(
            "s6_running_inference",
            model=model_name,
            augment=aug_name,
            checkpoint=ckpt.name,
            model_type=model_type,
        )

        try:
            detections = _load_and_infer(
                model_type=model_type,
                checkpoint=ckpt,
                image=img,
                device=resolved_device,
                conf_threshold=conf_threshold,
            )

            # Save individual image with detections
            vis = draw_detections(img, detections, conf_threshold=0.0)
            ckpt_label = ckpt.stem
            # Remove common checkpoint suffixes and names
            remove_parts = ["_best_model", "_best", "_last_model", "_last", "best_model", "best", "last_model", "last"]
            for part in remove_parts:
                if ckpt_label == part:
                    ckpt_label = ""
                    break
                if ckpt_label.endswith(part):
                    ckpt_label = ckpt_label[: -len(part)]
                    break
            if ckpt_label:
                individual_name = f"{model_name}_{aug_name}_{ckpt_label}.jpg"
            else:
                individual_name = f"{model_name}_{aug_name}.jpg"

            individual_path = resolved_output / individual_name
            cv2.imwrite(str(individual_path), vis)

            results.append({
                "model": model_name,
                "augment": aug_name,
                "checkpoint": ckpt,
                "detections": detections,
                "image": vis,
            })

            logger.info(
                "s6_inference_complete",
                model=model_name,
                augment=aug_name,
                num_detections=len(detections),
            )

        except Exception as e:
            logger.error("s6_inference_failed", model=model_name, augment=aug_name, error=str(e))

    # Build and save grid
    grid_path = resolved_output / "grid.jpg"
    fig = _build_grid(results)
    fig.savefig(str(grid_path), bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)

    logger.info("s6_grid_saved", path=str(grid_path), total_combos=len(results))

    # Save summary JSON
    import json

    summary = []
    for res in results:
        summary.append({
            "model": res["model"],
            "augment": res["augment"],
            "checkpoint": str(res["checkpoint"]),
            "num_detections": len(res["detections"]),
            "detections": res["detections"],
        })

    summary_path = resolved_output / "predictions.json"
    summary_path.write_text(json.dumps(summary, indent=2))

    logger.info("s6_predict_complete", output_dir=str(resolved_output))
    return grid_path


if __name__ == "__main__":
    from src.cli_helpers import standalone_main
    from pydantic import BaseModel, Field

    class PredictConfig(BaseModel):
        """CLI config for single-image inference grid."""

        image_path: str = Field(..., description="Path to input image")
        output_dir: str = Field(default="", description="Output directory")
        conf_threshold: float = Field(default=0.25, description="Confidence threshold")
        device: str = Field(default="", description="Device (cuda:0 or cpu)")

    def _run(cfg: PredictConfig) -> None:
        dev = cfg.device or None
        run_pipeline(
            image_path=cfg.image_path,
            output_dir=cfg.output_dir or None,
            conf_threshold=cfg.conf_threshold,
            device=dev,
        )

    standalone_main(
        config_model=PredictConfig,
        run_fn=_run,
        description="Run inference with all trained models on a single image",
        required_fields=["image_path"],
        skip_fields=["device"],
    )
