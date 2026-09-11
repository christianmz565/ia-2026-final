"""Global pipeline CLI with per-section flag passthrough.

Usage:
    uv run python -m src
    uv run python -m src --only s1_prepare s2_augments
    uv run python -m src --s1_prepare.download.force_redownload true
    uv run python -m src --log_level DEBUG
"""

from __future__ import annotations

import argparse
from typing import Any

import structlog

from src.config import PipelineConfig
from src.logging import configure_logging

logger = structlog.get_logger(__name__)

ALL_SECTIONS = [
    "s1_prepare",
    "s2_augments",
    "s3_train",
    "s4_evaluate",
    "s5_analysis",
]

PIPELINE_MODULES = {
    "s1_prepare": "src.s1_prepare.pipeline",
    "s2_augments": "src.s2_augments.pipeline",
    "s3_train": "src.s3_train.pipeline",
    "s4_evaluate": "src.s4_evaluate.pipeline",
    "s5_analysis": "src.s5_analysis.pipeline",
}


def _build_parser() -> argparse.ArgumentParser:
    """Build the argument parser with per-section nested flags."""
    parser = argparse.ArgumentParser(
        prog="src",
        description="Wood Surface Defect Detection — Data Augmentation Benchmark Pipeline",
    )

    parser.add_argument(
        "--only",
        nargs="+",
        choices=ALL_SECTIONS,
        default=None,
        help="Run only the specified section(s).",
    )
    parser.add_argument(
        "--log_level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Log level for structlog.",
    )

    for section in ALL_SECTIONS:
        parser.add_argument(
            f"--{section}",
            nargs="*",
            help=f"Flags for the {section} section (key=value pairs).",
        )

    return parser


def _parse_section_flags(section: str, raw_flags: list[str] | None) -> dict[str, Any]:
    """Parse ``key=value`` pairs from a section's REMAINDER args into a dict.

    Converts ``--s1_prepare download.force_redownload=true split.seed=100``
    into ``{"download": {"force_redownload": True}, "split": {"seed": 100}}``.
    """
    if not raw_flags:
        return {}

    overrides: dict[str, Any] = {}
    for token in raw_flags:
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        parts = key.split(".")

        coerced: Any = value
        if value.lower() in ("true", "yes"):
            coerced = True
        elif value.lower() in ("false", "no"):
            coerced = False
        else:
            try:
                coerced = int(value)
            except ValueError:
                try:
                    coerced = float(value)
                except ValueError:
                    coerced = [v.strip() for v in value.split(",")] if "," in value else value

        d = overrides
        for part in parts[:-1]:
            d = d.setdefault(part, {})
        d[parts[-1]] = coerced

    return overrides


def _apply_overrides(config: PipelineConfig, section: str, overrides: dict[str, Any]) -> None:
    """Deep-merge overrides into a section of the config."""
    section_model = getattr(config, section)
    for key, value in overrides.items():
        if isinstance(value, dict) and hasattr(getattr(section_model, key), "model_dump"):
            nested = getattr(section_model, key)
            for k, v in value.items():
                target_val = getattr(nested, k, None)
                if isinstance(target_val, list) and isinstance(v, str):
                    v = [item.strip() for item in v.split(",")]
                setattr(nested, k, v)
        else:
            target_val = getattr(section_model, key, None)
            if isinstance(target_val, list) and isinstance(value, str):
                value = [item.strip() for item in value.split(",")]
            setattr(section_model, key, value)


def _run_section(section: str, config: PipelineConfig) -> None:
    """Import and run a single section's pipeline."""
    import importlib

    module_path = PIPELINE_MODULES[section]
    logger.info("pipeline_section_start", section=section, module=module_path)

    mod = importlib.import_module(module_path)
    section_config = getattr(config, section)

    from src.utils import seed_all

    seed_all()

    mod.run_pipeline(section_config)

    logger.info("pipeline_section_complete", section=section)


def main() -> None:
    """Entry point for the global pipeline."""
    parser = _build_parser()
    args = parser.parse_args()

    configure_logging(args.log_level)

    config = PipelineConfig(log_level=args.log_level)

    for section in ALL_SECTIONS:
        raw = getattr(args, section, None)
        if raw:
            overrides = _parse_section_flags(section, raw)
            if overrides:
                _apply_overrides(config, section, overrides)
                logger.debug("section_overrides", section=section, overrides=overrides)

    sections_to_run = args.only or ALL_SECTIONS

    logger.info(
        "pipeline_start",
        sections=sections_to_run,
        log_level=args.log_level,
    )

    for section in sections_to_run:
        _run_section(section, config)

    logger.info("pipeline_complete")


if __name__ == "__main__":
    main()
