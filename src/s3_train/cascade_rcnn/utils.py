"""Utility functions for PyTorch CUDA optimization, AMP, logging, and Early Stopping."""

import random

import numpy as np
import structlog
import torch

logger = structlog.get_logger(__name__)


def set_seed(seed: int = 42) -> None:
    """Set random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def configure_cuda_optimizations(benchmark: bool = True) -> torch.device:
    """Configure PyTorch CUDA flags for optimal performance on local NVIDIA GPU."""
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        torch.backends.cudnn.benchmark = benchmark
        torch.backends.cuda.matmul.allow_tf32 = True
        torch.backends.cudnn.allow_tf32 = True
        device_name = torch.cuda.get_device_name(0)
        vram_gb = torch.cuda.get_device_properties(0).total_memory / 1e9
        logger.info("CUDA Enabled", device=device_name, vram_gb=round(vram_gb, 2), benchmark=benchmark)
    else:
        device = torch.device("cpu")
        logger.warning("CUDA is NOT available. Running on CPU.")
    return device


def get_amp_scaler(enabled: bool = True) -> torch.amp.GradScaler:
    """Return PyTorch Automatic Mixed Precision (AMP FP16) GradScaler."""
    return torch.amp.GradScaler("cuda", enabled=enabled)


def setup_logger(output_dir) -> structlog.stdlib.BoundLogger:
    """Configure logger instance for output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    return structlog.get_logger("CascadeRCNN")


class EarlyStopping:
    """Early stopping mechanism based on validation metric (e.g. mAP_50:95)."""

    def __init__(self, patience: int = 5, mode: str = "max", delta: float = 0.0001):
        self.patience = patience
        self.mode = mode
        self.delta = delta
        self.counter = 0
        self.best_score: float | None = None
        self.early_stop = False

    def __call__(self, current_score: float) -> bool:
        if self.best_score is None:
            self.best_score = current_score
            return True

        if self.mode == "max":
            improved = current_score > self.best_score + self.delta
        else:
            improved = current_score < self.best_score - self.delta

        if improved:
            self.best_score = current_score
            self.counter = 0
            return True
        else:
            self.counter += 1
            logger.info(
                "EarlyStopping counter update",
                counter=self.counter,
                patience=self.patience,
                best_score=self.best_score,
                current_score=current_score,
            )
            if self.counter >= self.patience:
                self.early_stop = True
            return False
