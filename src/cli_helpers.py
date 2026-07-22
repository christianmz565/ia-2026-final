"""CLI helpers: bridge between pydantic config models and argparse for standalone execution.

Eliminates duplicated ``parse_args()`` functions and manual config-from-args
translation. Every pydantic field automatically becomes a ``--field-name`` CLI
flag with its pydantic default as the argparse default.

Usage in any standalone-runnable file::

    if __name__ == "__main__":
        from src.cli_helpers import standalone_main

        standalone_main(
            config_model=MyConfig,
            run_fn=lambda cfg: my_function(cfg),
        )
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from src.logging import configure_logging

# ── Field-type → argparse kwargs mapping ─────────────────────────────────────

_ARGPARSE_TYPE_MAP: dict[type, dict[str, Any]] = {
    str: {"type": str},
    int: {"type": int},
    float: {"type": float},
    bool: {"action": "store_true", "default": False},
    Path: {"type": Path},
}


def _field_name_to_flag(field_name: str) -> str:
    """Convert pydantic field name ``my_field`` to CLI flag ``--my-field``."""
    return f"--{field_name.replace('_', '-')}"


def _resolve_type(field_annotation: type) -> type | None:
    """Resolve annotation to a simple type argparse understands.

    Handles ``Optional[X]``, ``X | None``, ``list[X]``, ``dict[...]``, etc.
    Returns ``None`` for complex types that need special handling.
    """
    origin = getattr(field_annotation, "__origin__", None)

    # list[X] → str (comma-separated)
    if origin is list:
        return str

    # dict[...] → str (JSON)
    if origin is dict:
        return str

    # Path
    if field_annotation is Path or (origin is Path):
        return Path

    # Simple builtins
    if field_annotation in _ARGPARSE_TYPE_MAP:
        return field_annotation

    return None


def add_model_args(
    parser: argparse.ArgumentParser,
    model: type[BaseModel],
    *,
    required_fields: list[str] | None = None,
    skip_fields: list[str] | None = None,
    prefix: str = "",
) -> None:
    """Auto-generate argparse flags from a pydantic model's fields.

    Each field becomes a ``--field-name`` flag. The default value is taken
    from the pydantic model (single source of truth). ``bool`` fields become
    ``store_true`` flags. ``list`` and ``dict`` fields accept comma-separated
    and JSON strings respectively.

    Args:
        parser: Argument parser to add flags to.
        model: Pydantic BaseModel class.
        required_fields: If set, only these fields get ``--required`` flags.
        skip_fields: Fields to skip entirely.
        prefix: Optional prefix for flag names (e.g. ``"download."``).
    """
    required_fields = set(required_fields or [])
    skip_fields = set(skip_fields or [])

    for field_name, field_info in model.model_fields.items():
        if field_name in skip_fields:
            continue

        flag = _field_name_to_flag(f"{prefix}{field_name}" if prefix else field_name)
        annotation = field_info.annotation

        resolved = _resolve_type(annotation)

        if resolved is bool:
            parser.add_argument(flag, action="store_true", default=None)
            continue

        if resolved is str and field_info.metadata:
            # Check for enum-like choices
            for meta in field_info.metadata:
                if hasattr(meta, "get") and "choices" in meta:
                    parser.add_argument(flag, choices=meta["choices"], default=None)
                    break
            else:
                parser.add_argument(flag, type=str, default=None)
            continue

        if resolved is not None:
            kwargs = dict(_ARGPARSE_TYPE_MAP.get(resolved, {"type": str}))
            kwargs["default"] = None
            if field_name in required_fields:
                kwargs["required"] = True
            parser.add_argument(flag, **kwargs)
            continue

        # Fallback: accept as string, we'll parse it later
        parser.add_argument(flag, type=str, default=None)


def model_from_args[T: BaseModel](
    model: type[T],
    args: argparse.Namespace,
    *,
    prefix: str = "",
) -> T:
    """Construct a pydantic model instance from argparse namespace.

    Only non-``None`` values from args are used (so pydantic defaults
    apply for anything not passed on the CLI).

    Args:
        model: Pydantic model class to instantiate.
        args: Parsed argparse namespace.
        prefix: Prefix that was used in ``add_model_args()``.

    Returns:
        Instantiated pydantic model.
    """
    kwargs: dict[str, Any] = {}
    for field_name in model.model_fields:
        flag_name = f"{prefix}{field_name}" if prefix else field_name
        # argparse converts hyphens to underscores in dest, but our flag
        # is already using underscores internally
        attr_name = flag_name.replace("-", "_")
        value = getattr(args, attr_name, None)
        if value is not None:
            # Handle list[str] from comma-separated string
            annotation = model.model_fields[field_name].annotation
            origin = getattr(annotation, "__origin__", None)
            if origin is list and isinstance(value, str):
                value = [v.strip() for v in value.split(",") if v.strip()]
            kwargs[field_name] = value

    return model(**kwargs)


def standalone_main[T: BaseModel](
    config_model: type[T],
    run_fn: Callable[[T], Any],
    *,
    description: str | None = None,
    required_fields: list[str] | None = None,
    skip_fields: list[str] | None = None,
    log_level_default: str = "INFO",
) -> None:
    """One-call entry point for any standalone-runnable module.

    Handles: argument parsing, logging setup, config construction, and
    function invocation. Replaces the duplicated ``parse_args()`` +
    ``if __name__`` pattern.

    Args:
        config_model: Pydantic config model class.
        run_fn: Callable that accepts the config and does the work.
        description: Help text for the argument parser.
        required_fields: Fields that become required CLI flags.
        skip_fields: Config fields to skip in argparse.
        log_level_default: Default log level.
    """
    model_name = config_model.__name__
    parser = argparse.ArgumentParser(
        description=description or f"Run {model_name}",
    )
    parser.add_argument(
        "--log_level",
        default=log_level_default,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )

    add_model_args(
        parser,
        config_model,
        required_fields=required_fields,
        skip_fields=skip_fields,
    )

    args = parser.parse_args()
    configure_logging(args.log_level)

    cfg = model_from_args(config_model, args)
    run_fn(cfg)
