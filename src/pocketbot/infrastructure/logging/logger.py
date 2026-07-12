"""
PocketBot Enterprise X

Infrastructure Logging Service.
"""

from __future__ import annotations

import logging
from pathlib import Path


class LoggerFactory:
    """
    Creates isolated application loggers.
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
        Creates an isolated configured logger.
        """

        logger = logging.getLogger(
            f"pocketbot.{name}",
        )

        logger.handlers.clear()

        logger.setLevel(
            logging.INFO,
        )

        logger.propagate = False

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

        return logger


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Returns an application logger.
    """

    factory = LoggerFactory()

    return factory.create(
        name,
    )
