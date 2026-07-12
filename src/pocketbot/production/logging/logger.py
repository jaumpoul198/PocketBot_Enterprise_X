from __future__ import annotations

import logging


def create_production_logger(name: str = "pocketbot") -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    return logger
