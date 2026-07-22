"""s3_train — Model training wrappers for each detection paradigm."""

from src.s3_train.faster_rcnn import FasterRCNNTrainer
from src.s3_train.rt_detr import RTDETRTrainer
from src.s3_train.yolov8 import YOLOv8Trainer

__all__ = [
    "FasterRCNNTrainer",
    "RTDETRTrainer",
    "YOLOv8Trainer",
]
