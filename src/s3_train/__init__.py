"""s3_train — Model training wrappers for each detection paradigm."""

from src.s3_train.cascade_rcnn import CascadeRCNNTrainer
from src.s3_train.rf_detr import RFDETRTrainer
from src.s3_train.yolo26 import YOLO26Trainer

__all__ = [
    "CascadeRCNNTrainer",
    "RFDETRTrainer",
    "YOLO26Trainer",
]
