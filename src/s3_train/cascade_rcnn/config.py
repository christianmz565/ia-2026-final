"""Configuration module for Cascade R-CNN Baseline object detection.

Provides dataclasses and parsing functionality for CLI arguments and YAML configuration files.
Defaults updated to point directly to `dataset/split/`.
"""

import json
from argparse import ArgumentParser
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from src.constants import CLASS_NAMES


@dataclass
class DatasetConfig:
    """Dataset and path configurations targeting dataset/split/."""

    data_dir: Path = Path("dataset/split")
    train_json: Path = Path("dataset/split/train/_annotations.coco.json")
    val_json: Path = Path("dataset/split/val/_annotations.coco.json")
    output_dir: Path = Path("outputs/casc_rcnn_baseline")
    num_classes: int = 8
    class_names: list[str] = field(default_factory=lambda: list(CLASS_NAMES))


@dataclass
class ModelConfig:
    """Architecture configuration."""

    backbone_variant: str = "convnext_tiny"
    pretrained: bool = True
    neck_type: str = "PAFPN"
    in_channels: list[int] = field(default_factory=lambda: [96, 192, 384, 768])
    out_channels: int = 256
    num_cascade_stages: int = 3
    cascade_iou_thresholds: list[float] = field(default_factory=lambda: [0.5, 0.6, 0.7])
    rpn_anchor_scales: list[int] = field(default_factory=lambda: [32, 64, 128, 256, 512])
    rpn_anchor_ratios: list[float] = field(default_factory=lambda: [0.5, 1.0, 2.0])


@dataclass
class TrainingConfig:
    """Training, optimization, and resource configurations."""

    epochs: int = 12
    batch_size: int = 2
    num_workers: int = 4
    lr: float = 0.0001
    weight_decay: float = 0.0001
    amp_enabled: bool = True
    cudnn_benchmark: bool = True
    pin_memory: bool = True
    early_stopping_patience: int = 5
    seed: int = 42


@dataclass
class PipelineConfig:
    """Full pipeline configuration wrapper."""

    dataset: DatasetConfig = field(default_factory=DatasetConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)

    @classmethod
    def from_yaml(cls, yaml_path: Path) -> "PipelineConfig":
        """Load configuration from a YAML file."""
        if not yaml_path.exists():
            raise FileNotFoundError(f"Config file not found: {yaml_path}")
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        dataset_data = data.get("dataset", {})
        model_data = data.get("model", {})
        training_data = data.get("training", {})

        dataset = DatasetConfig(
            data_dir=Path(dataset_data.get("data_dir", DatasetConfig.data_dir)),
            train_json=Path(dataset_data.get("train_json", DatasetConfig.train_json)),
            val_json=Path(dataset_data.get("val_json", DatasetConfig.val_json)),
            output_dir=Path(dataset_data.get("output_dir", DatasetConfig.output_dir)),
            num_classes=dataset_data.get("num_classes", DatasetConfig.num_classes),
            class_names=dataset_data.get("class_names", DatasetConfig().class_names),
        )

        model = ModelConfig(
            backbone_variant=model_data.get("backbone_variant", ModelConfig.backbone_variant),
            pretrained=model_data.get("pretrained", ModelConfig.pretrained),
            neck_type=model_data.get("neck_type", ModelConfig.neck_type),
            in_channels=model_data.get("in_channels", ModelConfig().in_channels),
            out_channels=model_data.get("out_channels", ModelConfig.out_channels),
            num_cascade_stages=model_data.get("num_cascade_stages", ModelConfig.num_cascade_stages),
            cascade_iou_thresholds=model_data.get("cascade_iou_thresholds", ModelConfig().cascade_iou_thresholds),
        )

        training = TrainingConfig(
            epochs=training_data.get("epochs", TrainingConfig.epochs),
            batch_size=training_data.get("batch_size", TrainingConfig.batch_size),
            num_workers=training_data.get("num_workers", TrainingConfig.num_workers),
            lr=training_data.get("lr", TrainingConfig.lr),
            weight_decay=training_data.get("weight_decay", TrainingConfig.weight_decay),
            amp_enabled=training_data.get("amp_enabled", TrainingConfig.amp_enabled),
            cudnn_benchmark=training_data.get("cudnn_benchmark", TrainingConfig.cudnn_benchmark),
            pin_memory=training_data.get("pin_memory", TrainingConfig.pin_memory),
            early_stopping_patience=training_data.get(
                "early_stopping_patience", TrainingConfig.early_stopping_patience
            ),
            seed=training_data.get("seed", TrainingConfig.seed),
        )

        return cls(dataset=dataset, model=model, training=training)

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "dataset": {
                "data_dir": str(self.dataset.data_dir),
                "train_json": str(self.dataset.train_json),
                "val_json": str(self.dataset.val_json),
                "output_dir": str(self.dataset.output_dir),
                "num_classes": self.dataset.num_classes,
                "class_names": self.dataset.class_names,
            },
            "model": {
                "backbone_variant": self.model.backbone_variant,
                "pretrained": self.model.pretrained,
                "neck_type": self.model.neck_type,
                "in_channels": self.model.in_channels,
                "out_channels": self.model.out_channels,
                "num_cascade_stages": self.model.num_cascade_stages,
                "cascade_iou_thresholds": self.model.cascade_iou_thresholds,
            },
            "training": {
                "epochs": self.training.epochs,
                "batch_size": self.training.batch_size,
                "num_workers": self.training.num_workers,
                "lr": self.training.lr,
                "weight_decay": self.training.weight_decay,
                "amp_enabled": self.training.amp_enabled,
                "cudnn_benchmark": self.training.cudnn_benchmark,
                "pin_memory": self.training.pin_memory,
                "early_stopping_patience": self.training.early_stopping_patience,
                "seed": self.training.seed,
            },
        }

    def save_json(self, json_path: Path) -> None:
        """Save configuration to JSON file."""
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)


def get_cli_parser() -> ArgumentParser:
    """Create CLI argument parser."""
    parser = ArgumentParser(description="Cascade R-CNN Baseline Object Detection Training Pipeline")
    parser.add_argument("--config", type=Path, default=None, help="Path to YAML configuration file")
    parser.add_argument("--data-dir", type=Path, default=None, help="Root directory for dataset images")
    parser.add_argument("--train-json", type=Path, default=None, help="COCO format training annotation JSON")
    parser.add_argument("--val-json", type=Path, default=None, help="COCO format validation annotation JSON")
    parser.add_argument("--output-dir", type=Path, default=None, help="Directory to save models and logs")
    parser.add_argument(
        "--backbone",
        type=str,
        choices=["convnext_tiny", "convnext_small"],
        default=None,
        help="ConvNeXt backbone variant",
    )
    parser.add_argument("--epochs", type=int, default=None, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=None, help="Batch size per GPU")
    parser.add_argument("--num-workers", type=int, default=None, help="Number of DataLoader workers")
    parser.add_argument("--lr", type=float, default=None, help="Initial learning rate")
    parser.add_argument("--no-amp", action="store_true", help="Disable Automatic Mixed Precision (AMP)")
    return parser


def parse_config() -> PipelineConfig:
    """Parse configuration from CLI and optional YAML file."""
    parser = get_cli_parser()
    args, _ = parser.parse_known_args()

    config = PipelineConfig.from_yaml(args.config) if args.config and args.config.exists() else PipelineConfig()

    if args.data_dir:
        config.dataset.data_dir = args.data_dir
    if args.train_json:
        config.dataset.train_json = args.train_json
    if args.val_json:
        config.dataset.val_json = args.val_json
    if args.output_dir:
        config.dataset.output_dir = args.output_dir
    if args.backbone:
        config.model.backbone_variant = args.backbone
    if args.epochs:
        config.training.epochs = args.epochs
    if args.batch_size:
        config.training.batch_size = args.batch_size
    if args.num_workers is not None:
        config.training.num_workers = args.num_workers
    if args.lr:
        config.training.lr = args.lr
    if args.no_amp:
        config.training.amp_enabled = False

    return config
