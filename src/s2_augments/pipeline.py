"""s2_augments pipeline — generates all configured augmented dataset splits.

Standalone usage:
    uv run python -m src.s2_augments.pipeline
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.config import S2Config
from src.constants import AUGMENTED_DIR, SPLIT_DATASET, TEST_SPLIT, TRAIN_SPLIT, VALID_SPLIT
from src.s1_prepare.convert_coco import convert_split
from src.s2_augments.base import get_augmentation, list_augmentations

logger = structlog.get_logger(__name__)

STEPS = ["albumentations_balanced", "boxaug_standard", "boxaug_libcom"]


def run_pipeline(config: S2Config | None = None) -> None:
    """Execute augmentation pipeline for all configured methods.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S2Config()
    methods = config.augment.methods
    train_split_dir = SPLIT_DATASET / "train"

    logger.info("s2_pipeline_start", methods=methods, available=list_augmentations())

    for method_name in methods:
        target_dir = AUGMENTED_DIR / method_name
        method_cfg = getattr(config.augment, method_name, None)

        def _run_method(name: str = method_name, out_dir: Path = target_dir, cfg: Any = method_cfg) -> Path:
            augmentor = get_augmentation(name)
            logger.info("generating_augmented_split", method=name, output_dir=str(out_dir))
            augmentor.generate_dataset(
                input_dir=train_split_dir,
                output_dir=out_dir,
                config=cfg,
            )
            convert_split(out_dir, TRAIN_SPLIT)
            for split_name in (VALID_SPLIT, TEST_SPLIT):
                src_split = SPLIT_DATASET / split_name
                dst_split = out_dir / split_name
                if src_split.exists() and not dst_split.exists():
                    shutil.copytree(src_split, dst_split)
            (out_dir / ".augmented").touch()
            logger.info("s2_step_complete", method=name, output_dir=str(out_dir))
            return out_dir

        run_cached_step(
            step_name=f"augment_{method_name}",
            target_path=target_dir,
            fn=_run_method,
        )

    logger.info("s2_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S2Config,
        run_fn=run_pipeline,
        description="s2_augments pipeline",
        skip_fields=["augment"],
    )
