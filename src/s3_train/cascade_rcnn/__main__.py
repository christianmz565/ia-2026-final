"""Standalone entry point for Cascade R-CNN training.

Usage:
    uv run python -m src.s3_train.cascade_rcnn [--data-dir PATH] [--epochs 12]
"""

from src.cli_helpers import standalone_main
from src.config import CascadeRCNNConfig
from src.s3_train.cascade_rcnn import CascadeRCNNTrainer

if __name__ == "__main__":
    standalone_main(
        config_model=CascadeRCNNConfig,
        run_fn=lambda cfg: CascadeRCNNTrainer(cfg).train(cfg),
        description="Train Cascade R-CNN",
        required_fields=["data_dir"],
    )
