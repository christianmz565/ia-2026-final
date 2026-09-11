"""Typed configuration models for the entire pipeline.

Every section gets its own Pydantic model. The global ``PipelineConfig`` nests
all section configs so that the CLI can override any leaf value via flags like
``--s1_prepare.download.force_redownload true``.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from src.constants import (
    DEFAULT_CASCADE_EPOCHS,
    DEFAULT_CASCADE_LR,
    DEFAULT_CONF_THRESHOLD,
    DEFAULT_MAJORITY_DOWNSAMPLE_RATIO,
    DEFAULT_PATIENCE,
    DEFAULT_RFDETR_EPOCHS,
    DEFAULT_RFDETR_LR,
    DEFAULT_SEED,
    DEFAULT_SPLIT_RATIOS,
    DEFAULT_YOLO_EPOCHS,
    KAGGLE_DATASET,
    MIN_ABSOLUTE_DIM_PX,
    MIN_ELONGATED_DIM_PX,
    MIN_LABEL_AREA_PX,
    TARGET_IMG_HEIGHT,
    TARGET_IMG_WIDTH,
)
from src.s2_augments.augmentations import (
    AlbumentationsBalancedConfig,
    BoxAugLibcomConfig,
    BoxAugStandardConfig,
)
from src.utils import get_default_device

_default_device = get_default_device


class DownloadConfig(BaseModel):
    """Configuration for dataset download."""

    kaggle_dataset: str = Field(default=KAGGLE_DATASET, description="Kaggle dataset slug")
    force_redownload: bool = Field(default=False, description="Re-download even if exists")


class PreprocessConfig(BaseModel):
    """Configuration for image downscaling, cropping, and label filtering."""

    scale_factor: float = Field(default=0.5, description="Factor to resize image (e.g. 0.5 for 50%)")
    min_absolute_dim_px: float = Field(
        default=MIN_ABSOLUTE_DIM_PX, description="Minimum absolute width and height in pixels after downscale"
    )
    min_label_area_px: float = Field(
        default=MIN_LABEL_AREA_PX, description="Minimum bounding box area in pixels after downscale"
    )
    min_elongated_dim_px: float = Field(
        default=MIN_ELONGATED_DIM_PX, description="Minimum major dimension for elongated labels"
    )
    black_threshold: int = Field(default=10, description="Grayscale intensity threshold for non-black wood pixels")


class SplitConfig(BaseModel):
    """Configuration for train/val/test splitting."""

    ratios: dict[str, float] = Field(default_factory=lambda: dict(DEFAULT_SPLIT_RATIOS))
    seed: int = Field(default=DEFAULT_SEED, description="Random seed for reproducibility")
    stratify_by_class: bool = Field(default=True, description="Stratify splits by defect class")
    majority_downsample_ratio: float = Field(
        default=DEFAULT_MAJORITY_DOWNSAMPLE_RATIO,
        description="Fraction of pure majority planks (classes 1 and 4) to drop from train split",
    )


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
    device: str = Field(
        default_factory=get_default_device,
        description="Target device for GPU-accelerated augmentations (e.g. 'cuda:0' or 'cpu')",
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
    model_size: str = Field(default="yolo26m.pt", description="YOLO26 variant")
    epochs: int = Field(default=DEFAULT_YOLO_EPOCHS)
    target_width: int = Field(default=TARGET_IMG_WIDTH, description="Target width for rectangular training")
    target_height: int = Field(default=TARGET_IMG_HEIGHT, description="Target height for rectangular training")
    rect: bool = Field(default=True, description="Enable rectangular training preserving aspect ratio")
    batch: int = Field(default=16)
    lr0: float = Field(default=0.01)
    patience: int = Field(default=DEFAULT_PATIENCE, description="Early stopping patience")
    device: str = Field(default_factory=_default_device)
    freeze_layer_count: int | None = Field(
        default=None, description="Number of initial backbone layers to freeze during training"
    )


class CascadeRCNNConfig(BaseModel):
    """Cascade R-CNN training hyper-parameters (MMDetection)."""

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    config_file: str = Field(default="cascade_rcnn_r50_fpn_1x_coco.py")
    epochs: int = Field(default=DEFAULT_CASCADE_EPOCHS)
    target_width: int = Field(default=TARGET_IMG_WIDTH, description="Target scale width")
    target_height: int = Field(default=TARGET_IMG_HEIGHT, description="Target scale height")
    batch_size: int = Field(default=8)
    lr: float = Field(default=DEFAULT_CASCADE_LR)
    patience: int = Field(default=DEFAULT_PATIENCE, description="Early stopping patience")
    device: str = Field(default_factory=_default_device)


class RFDETRConfig(BaseModel):
    """RF-DETR training hyper-parameters."""

    model_config = {"protected_namespaces": ()}

    data_dir: str = Field(default="", description="Path to training data directory")
    output_dir: str = Field(default="", description="Path to output directory")
    model_size: str = Field(default="rfdetr-m.pt", description="RF-DETR variant")
    epochs: int = Field(default=DEFAULT_RFDETR_EPOCHS)
    imgsz: int = Field(default=512)
    batch: int = Field(default=8)
    lr0: float = Field(default=DEFAULT_RFDETR_LR)
    patience: int = Field(default=DEFAULT_PATIENCE, description="Early stopping patience")
    square_resize: bool = Field(default=False, description="Whether to force square resize or preserve aspect ratio")
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
    conf_threshold: float = Field(default=DEFAULT_CONF_THRESHOLD)
    max_images: int | None = Field(default=None, description="Max test images for sampled inference")



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
