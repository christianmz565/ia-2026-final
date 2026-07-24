"""Typed configuration models for the entire pipeline.

Every section gets its own Pydantic model. The global ``PipelineConfig`` nests
all section configs so that the CLI can override any leaf value via flags like
``--s1_prepare.download.force_redownload true``.
"""

from __future__ import annotations

import torch
from pydantic import BaseModel, Field

from src.constants import (
    DEFAULT_SEED,
    DEFAULT_SPLIT_RATIOS,
    KAGGLE_DATASET,
)
from src.s2_augments.augmentations import (
    AlbumentationsBalancedConfig,
    BoxAugLibcomConfig,
    BoxAugStandardConfig,
)


def _default_device() -> str:
    """Return default device depending on CUDA availability."""
    return "cuda:0" if torch.cuda.is_available() else "cpu"


class DownloadConfig(BaseModel):
    """Configuration for dataset download."""

    kaggle_dataset: str = Field(default=KAGGLE_DATASET, description="Kaggle dataset slug")
    force_redownload: bool = Field(default=False, description="Re-download even if exists")


class PreprocessConfig(BaseModel):
    """Configuration for image downscaling, cropping, and label filtering."""

    scale_factor: float = Field(default=0.5, description="Factor to resize image (e.g. 0.5 for 50%)")
    min_label_size_px: float = Field(
        default=4.0, description="Minimum width or height in pixels after downscale to keep label"
    )
    black_threshold: int = Field(default=10, description="Grayscale intensity threshold for non-black wood pixels")


class SplitConfig(BaseModel):
    """Configuration for train/val/test splitting."""

    ratios: dict[str, float] = Field(default_factory=lambda: dict(DEFAULT_SPLIT_RATIOS))
    seed: int = Field(default=DEFAULT_SEED, description="Random seed for reproducibility")
    stratify_by_class: bool = Field(default=True, description="Stratify splits by defect class")


class S1Config(BaseModel):
    """Configuration for the s1_prepare section."""

    download: DownloadConfig = Field(default_factory=DownloadConfig)
    preprocess: PreprocessConfig = Field(default_factory=PreprocessConfig)
    split: SplitConfig = Field(default_factory=SplitConfig)


class AugmentConfig(BaseModel):
    """Top-level augmentation configuration."""

    methods: list[str] = Field(
        default_factory=lambda: ["albumentations_balanced", "boxaug_standard", "boxaug_libcom"],
        description="List of augmentation method names to apply",
    )
    albumentations_balanced: AlbumentationsBalancedConfig = Field(default_factory=AlbumentationsBalancedConfig)
    boxaug_standard: BoxAugStandardConfig = Field(default_factory=BoxAugStandardConfig)
    boxaug_libcom: BoxAugLibcomConfig = Field(default_factory=BoxAugLibcomConfig)


class S2Config(BaseModel):
    """Configuration for the s2_augments section."""

    augment: AugmentConfig = Field(default_factory=AugmentConfig)


class YOLO26Config(BaseModel):
    """YOLO26 training hyper-parameters."""

    model_config = {"protected_namespaces": ()}

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    model_size: str = Field(default="yolo26n.pt", description="YOLO26 variant")
    epochs: int = Field(default=100)
    imgsz: int = Field(default=640)
    batch: int = Field(default=16)
    lr0: float = Field(default=0.01)
    device: str = Field(default_factory=_default_device)


class CascadeRCNNConfig(BaseModel):
    """Cascade R-CNN training hyper-parameters (MMDetection)."""

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    config_file: str = Field(default="cascade_rcnn_r50_fpn_1x_coco.py")
    epochs: int = Field(default=12)
    imgsz: int = Field(default=640)
    batch_size: int = Field(default=16)
    lr: float = Field(default=0.0001)
    device: str = Field(default_factory=_default_device)


class RFDETRConfig(BaseModel):
    """RF-DETR training hyper-parameters."""

    model_config = {"protected_namespaces": ()}

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    model_size: str = Field(default="rfdetr-m.pt", description="RF-DETR variant")
    epochs: int = Field(default=50)
    imgsz: int = Field(default=512)
    batch: int = Field(default=8)
    lr0: float = Field(default=0.001)
    device: str = Field(default_factory=_default_device)


class S3Config(BaseModel):
    """Configuration for the s3_train section."""

    models: list[str] = Field(
        default_factory=lambda: ["rf_detr", "cascade_rcnn", "yolo26"],
        description="Model paradigms to train",
    )
    augments: list[str] = Field(
        default_factory=lambda: ["baseline", "albumentations_balanced", "boxaug_standard", "boxaug_libcom"],
        description="Augmentation dataset splits to train models on",
    )
    rf_detr: RFDETRConfig = Field(default_factory=RFDETRConfig)
    cascade_rcnn: CascadeRCNNConfig = Field(default_factory=CascadeRCNNConfig)
    yolo26: YOLO26Config = Field(default_factory=YOLO26Config)


class EvalConfig(BaseModel):
    """Evaluation parameters."""

    model_config = {"protected_namespaces": ()}

    model_path: str = Field(default="", description="Path to trained model")
    data_dir: str = Field(default="", description="Path to test data directory")
    predictions: str = Field(default="", description="Path to predictions file")
    ground_truth: str = Field(default="", description="Path to ground truth annotations")
    output_path: str = Field(default="", description="Path to output results file")
    iou_threshold: float = Field(default=0.5, description="IoU threshold for mAP")
    device: str = Field(default_factory=_default_device)
    conf_threshold: float = Field(default=0.25)


class S4Config(BaseModel):
    """Configuration for the s4_evaluate section."""

    models: list[str] = Field(
        default_factory=lambda: ["rf_detr", "cascade_rcnn", "yolo26"],
        description="Model paradigms to evaluate",
    )
    augments: list[str] = Field(
        default_factory=lambda: ["baseline", "albumentations_balanced", "boxaug_standard", "boxaug_libcom"],
        description="Augmentation dataset splits to evaluate",
    )
    eval: EvalConfig = Field(default_factory=EvalConfig)


class AnalysisConfig(BaseModel):
    """Analysis and output preferences."""

    input: str = Field(default="", description="Path to aggregated results JSON")
    output_dir: str = Field(default="", description="Path to output directory")
    output_format: str = Field(default="latex", description="Table format: latex, markdown, csv")
    figure_dpi: int = Field(default=300)
    figure_backend: str = Field(default="Agg")


class S5Config(BaseModel):
    """Configuration for the s5_analysis section."""

    results_dir: str = Field(default="", description="Path to results directory")
    analysis: AnalysisConfig = Field(default_factory=AnalysisConfig)


class PipelineConfig(BaseModel):
    """Root configuration that nests every section."""

    s1_prepare: S1Config = Field(default_factory=S1Config)
    s2_augments: S2Config = Field(default_factory=S2Config)
    s3_train: S3Config = Field(default_factory=S3Config)
    s4_evaluate: S4Config = Field(default_factory=S4Config)
    s5_analysis: S5Config = Field(default_factory=S5Config)
    log_level: str = Field(default="INFO", description="Log level for structlog")
