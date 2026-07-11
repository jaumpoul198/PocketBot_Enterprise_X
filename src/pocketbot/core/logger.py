"""
PocketBot Enterprise X

Core Logger Compatibility Layer.
"""

from __future__ import annotations

from logging import Logger

from pocketbot.infrastructure.logging.logger import (
    get_logger as _get_logger,
)


def get_logger(
    name: str,
) -> Logger:
    """
    Returns application logger.

    Compatibility wrapper for existing imports.
    """

    return _get_logger(
        name,
    )
