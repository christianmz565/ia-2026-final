"""Caching utilities for pipeline steps under partials.

Provides a unified, abstracted caching mechanism to check if step outputs exist in
the ``partials/`` directory and skip execution if cached.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any, TypeVar

import structlog

logger = structlog.get_logger(__name__)

T = TypeVar("T")


def is_cached(target_path: Path | str | list[Path | str]) -> bool:
    """Check if target path(s) exist under partials and contain data.

    Args:
        target_path: Single Path/str or list of Path/str objects to check.

    Returns:
        True if all target paths exist and are non-empty files or non-empty directories.
    """
    paths = [Path(p) for p in target_path] if isinstance(target_path, list) else [Path(target_path)]
    if not paths:
        return False

    for path in paths:
        if not path.exists():
            return False
        if path.is_file() and path.stat().st_size == 0:
            return False
        if path.is_dir() and not any(path.iterdir()):
            return False

    return True


def run_cached_step(
    step_name: str,
    target_path: Path | str | list[Path | str],
    fn: Callable[[], Any],
    *,
    force: bool = False,
    loader: Callable[[Path], Any] | None = None,
) -> Any:
    """Execute a pipeline step only if its target results do not exist in partials.

    Args:
        step_name: Descriptive name of the step (e.g. 'download', 'preprocess', 'yolo26').
        target_path: Expected file or directory output path(s) under partials.
        fn: Function to execute if step is not cached or force is True.
        force: If True, ignore existing cached files and re-run step.
        loader: Optional function to load and return cached result if target is a file.

    Returns:
        The step function return value, loaded cached result, or target path.
    """
    primary_path = Path(target_path[0]) if isinstance(target_path, list) else Path(target_path)

    if not force and is_cached(target_path):
        logger.info("step_cached", step=step_name, path=str(primary_path))
        if loader and primary_path.is_file():
            return loader(primary_path)
        return primary_path

    logger.info("step_start", step=step_name, path=str(primary_path))
    result = fn()
    logger.info("step_complete", step=step_name, path=str(primary_path))
    return result
