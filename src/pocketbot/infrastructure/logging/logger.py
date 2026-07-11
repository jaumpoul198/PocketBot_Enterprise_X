"""
PocketBot Enterprise X

Infrastructure Logging Service.
"""

from __future__ import annotations

import logging
from pathlib import Path


class LoggerFactory:
    """
    Creates configured application loggers.
    """

    def __init__(
        self,
        log_directory: Path | None = None,
    ) -> None:
        self._log_directory = (
            log_directory
            or Path("logs")
        )

        self._log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def create(
        self,
        name: str,
    ) -> logging.Logger:
        """
        Creates or returns a configured logger.
        """

        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(
            logging.INFO,
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            formatter,
        )

        file_handler = logging.FileHandler(
            self._log_directory / "pocketbot.log",
            encoding="utf-8",
        )

        file_handler.setFormatter(
            formatter,
        )

        logger.addHandler(
            console_handler,
        )

        logger.addHandler(
            file_handler,
        )

        logger.propagate = False

        return logger


_default_factory = LoggerFactory()


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Returns application logger.
    """

    return _default_factory.create(
        name,
    )
