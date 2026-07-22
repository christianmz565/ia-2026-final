"""Standardized structured logging configuration.

Every module should create its logger with::

    import structlog
    logger = structlog.get_logger(__name__)
"""

from __future__ import annotations

import logging
import sys

import structlog


def configure_logging(level: str = "INFO") -> None:
    """Configure structlog with consistent processors for the project.

    Args:
        level: Log level string (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            _pick_renderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, level.upper(), logging.INFO),
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(file=sys.stderr),
        cache_logger_on_first_use=True,
    )


def _pick_renderer() -> structlog.types.Processor:
    """Return a console renderer for TTYs, JSON otherwise."""
    if sys.stderr.isatty():
        return structlog.dev.ConsoleRenderer(colors=True)
    return structlog.processors.JSONRenderer()
