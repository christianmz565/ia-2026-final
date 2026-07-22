"""Typed configuration models for the entire pipeline.

Every section gets its own Pydantic model. The global ``PipelineConfig`` nests
all section configs so that the CLI can override any leaf value via flags like
``--s1_prepare.download.force_redownload true``.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from src.constants import (
    DEFAULT_SEED,
    DEFAULT_SPLIT_RATIOS,
    KAGGLE_DATASET,
)

# ── S1: Prepare ─────────────────────────────────────────────────────────────


class DownloadConfig(BaseModel):
    """Configuration for dataset download."""

    kaggle_dataset: str = Field(default=KAGGLE_DATASET, description="Kaggle dataset slug")
    force_redownload: bool = Field(default=False, description="Re-download even if exists")


class SplitConfig(BaseModel):
    """Configuration for train/val/test splitting."""

    ratios: dict[str, float] = Field(default_factory=lambda: dict(DEFAULT_SPLIT_RATIOS))
    seed: int = Field(default=DEFAULT_SEED, description="Random seed for reproducibility")
    stratify_by_class: bool = Field(default=True, description="Stratify splits by defect class")


class S1Config(BaseModel):
    """Configuration for the s1_prepare section."""

    download: DownloadConfig = Field(default_factory=DownloadConfig)
    split: SplitConfig = Field(default_factory=SplitConfig)


# ── S2: Augments ─────────────────────────────────────────────────────────────


class GeometricConfig(BaseModel):
    """Parameters for geometric augmentations."""

    horizontal_flip_prob: float = Field(default=0.5, ge=0.0, le=1.0)
    vertical_flip_prob: float = Field(default=0.0, ge=0.0, le=1.0)
    rotation_limit: int = Field(default=15, description="Max rotation in degrees")
    scale_limit: float = Field(default=0.2, description="Scale jitter range")
    crop_prob: float = Field(default=0.0, ge=0.0, le=1.0)
    crop_size: tuple[int, int] = Field(default=(640, 640))


class PhotometricConfig(BaseModel):
    """Parameters for photometric augmentations."""

    brightness_limit: float = Field(default=0.2)
    contrast_limit: float = Field(default=0.2)
    saturation_limit: float = Field(default=0.2)
    hue_shift_limit: int = Field(default=20)
    motion_blur_prob: float = Field(default=0.0, ge=0.0, le=1.0)
    gaussian_noise_prob: float = Field(default=0.0, ge=0.0, le=1.0)


class MosaicConfig(BaseModel):
    """Parameters for mosaic augmentation."""

    target_size: tuple[int, int] = Field(default=(640, 640))
    prob: float = Field(default=1.0, ge=0.0, le=1.0)


class MixupConfig(BaseModel):
    """Parameters for mixup augmentation."""

    mixup_prob: float = Field(default=0.5, ge=0.0, le=1.0)
    alpha: float = Field(default=1.5, description="Mixup alpha parameter")


class AugmentConfig(BaseModel):
    """Top-level augmentation configuration."""

    methods: list[str] = Field(
        default_factory=lambda: ["geometric", "photometric"],
        description="List of augmentation method names to apply",
    )
    geometric: GeometricConfig = Field(default_factory=GeometricConfig)
    photometric: PhotometricConfig = Field(default_factory=PhotometricConfig)
    mosaic: MosaicConfig = Field(default_factory=MosaicConfig)
    mixup: MixupConfig = Field(default_factory=MixupConfig)


class S2Config(BaseModel):
    """Configuration for the s2_augments section."""

    augment: AugmentConfig = Field(default_factory=AugmentConfig)


# ── S3: Train ────────────────────────────────────────────────────────────────


class YOLOv8Config(BaseModel):
    """YOLOv8 training hyper-parameters."""

    model_config = {"protected_namespaces": ()}

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    model_size: str = Field(default="yolov8n.pt", description="YOLOv8 variant")
    epochs: int = Field(default=100)
    imgsz: int = Field(default=640)
    batch: int = Field(default=16)
    lr0: float = Field(default=0.01)
    device: str = Field(default="cuda:0")


class FasterRCNNConfig(BaseModel):
    """Faster R-CNN training hyper-parameters (MMDetection)."""

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    config_file: str = Field(default="faster_rcnn_r50_fpn_1x_coco.py")
    epochs: int = Field(default=12)
    batch_size: int = Field(default=8)
    lr: float = Field(default=0.01)
    device: str = Field(default="cuda:0")


class RTDETRConfig(BaseModel):
    """RT-DETR training hyper-parameters."""

    model_config = {"protected_namespaces": ()}

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    model_size: str = Field(default="rtdetr-l.pt", description="RT-DETR variant")
    epochs: int = Field(default=100)
    imgsz: int = Field(default=640)
    batch: int = Field(default=8)
    lr0: float = Field(default=0.001)
    device: str = Field(default="cuda:0")


class S3Config(BaseModel):
    """Configuration for the s3_train section."""

    models: list[str] = Field(
        default_factory=lambda: ["yolov8", "faster_rcnn", "rt_detr"],
        description="Model paradigms to train",
    )
    yolov8: YOLOv8Config = Field(default_factory=YOLOv8Config)
    faster_rcnn: FasterRCNNConfig = Field(default_factory=FasterRCNNConfig)
    rt_detr: RTDETRConfig = Field(default_factory=RTDETRConfig)


# ── S4: Evaluate ─────────────────────────────────────────────────────────────


class EvalConfig(BaseModel):
    """Evaluation parameters."""

    model_config = {"protected_namespaces": ()}

    model_path: str = Field(default="", description="Path to trained model")
    data_dir: str = Field(default="", description="Path to test data directory")
    predictions: str = Field(default="", description="Path to predictions file")
    ground_truth: str = Field(default="", description="Path to ground truth annotations")
    output_path: str = Field(default="", description="Path to output results file")
    iou_threshold: float = Field(default=0.5, description="IoU threshold for mAP")
    device: str = Field(default="cuda:0")
    conf_threshold: float = Field(default=0.25)


class S4Config(BaseModel):
    """Configuration for the s4_evaluate section."""

    eval: EvalConfig = Field(default_factory=EvalConfig)


# ── S5: Analysis ─────────────────────────────────────────────────────────────


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


# ── Global pipeline config ───────────────────────────────────────────────────


class PipelineConfig(BaseModel):
    """Root configuration that nests every section."""

    s1_prepare: S1Config = Field(default_factory=S1Config)
    s2_augments: S2Config = Field(default_factory=S2Config)
    s3_train: S3Config = Field(default_factory=S3Config)
    s4_evaluate: S4Config = Field(default_factory=S4Config)
    s5_analysis: S5Config = Field(default_factory=S5Config)
    log_level: str = Field(default="INFO", description="Log level for structlog")
