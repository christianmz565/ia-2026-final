"""s3_train pipeline — trains all configured models on all augmented datasets.

Standalone usage:
    uv run python -m src.s3_train.pipeline [--models rf_detr,cascade_rcnn,yolo26] [--augments baseline,geometric,photometric]
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import structlog

from src.caching import run_cached_step
from src.config import S3Config
from src.constants import AUGMENTED_DIR, S3_OUTPUT, SPLIT_DATASET
from src.s3_train.base import get_trainer, list_trainers

logger = structlog.get_logger(__name__)


def run_pipeline(config: S3Config | None = None) -> None:
    """Train each configured model on each augmented dataset split.

    Args:
        config: Section configuration. Uses defaults when ``None``.
    """
    config = config or S3Config()
    models = config.models
    augments = config.augments

    logger.info("s3_pipeline_start", models=models, augments=augments, available=list_trainers())

    for model_name in models:
        for aug_name in augments:
            target_dir = S3_OUTPUT / model_name / aug_name
            data_dir = SPLIT_DATASET if aug_name == "baseline" else AUGMENTED_DIR / aug_name
            model_config = getattr(config, model_name, None)

            def _run_train(
                name: str = model_name,
                aug: str = aug_name,
                cfg: Any = model_config,
                d_dir: Path = data_dir,
                out_dir: Path = target_dir,
            ) -> Path:
                trainer = get_trainer(name)
                if cfg is not None and hasattr(cfg, "model_copy"):
                    exec_cfg = cfg.model_copy(deep=True)
                    exec_cfg.data_dir = str(d_dir)
                    exec_cfg.output_dir = str(out_dir)
                else:
                    exec_cfg = cfg
                return trainer.train(exec_cfg)

            run_cached_step(
                step_name=f"train_{model_name}_{aug_name}",
                target_path=target_dir,
                fn=_run_train,
            )

    logger.info("s3_pipeline_complete")


if __name__ == "__main__":
    from src.cli_helpers import standalone_main

    standalone_main(
        config_model=S3Config,
        run_fn=run_pipeline,
        description="s3_train pipeline",
        skip_fields=["yolo26", "cascade_rcnn", "rf_detr"],
    )
