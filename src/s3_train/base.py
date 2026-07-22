"""Base training protocol — common interface for all model trainers."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol, runtime_checkable

import structlog

logger = structlog.get_logger(__name__)


@runtime_checkable
class Trainer(Protocol):
    """Interface that every model training wrapper must implement."""

    name: str

    def train(
        self,
        data_dir: Path,
        output_dir: Path,
        config: Any,
    ) -> Path:
        """Train the model and return path to the best checkpoint.

        Args:
            data_dir: Directory with train/val splits (YOLO or COCO format).
            output_dir: Where to save checkpoints, logs, and config.
            config: Model-specific training config.

        Returns:
            Path to the best model checkpoint/weights.
        """
        ...

    def export(self, checkpoint: Path, output_dir: Path, format: str = "onnx") -> Path:
        """Export a trained model to a portable format.

        Args:
            checkpoint: Path to trained model weights.
            output_dir: Where to save the exported model.
            format: Export format (onnx, torchscript, etc.).

        Returns:
            Path to the exported model file.
        """
        ...


_TRAINER_REGISTRY: dict[str, type[Trainer]] = {}


def register_trainer(name: str, cls: type[Trainer]) -> None:
    """Register a trainer class by name."""
    _TRAINER_REGISTRY[name] = cls


def get_trainer(name: str) -> Trainer:
    """Instantiate and return a trainer by registered name."""
    if name not in _TRAINER_REGISTRY:
        available = ", ".join(sorted(_TRAINER_REGISTRY))
        raise KeyError(f"Unknown trainer '{name}'. Available: {available}")
    return _TRAINER_REGISTRY[name]()


def list_trainers() -> list[str]:
    """Return sorted list of registered trainer names."""
    return sorted(_TRAINER_REGISTRY)
