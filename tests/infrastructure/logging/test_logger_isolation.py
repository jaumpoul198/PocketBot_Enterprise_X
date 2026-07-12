from pathlib import Path

from pocketbot.infrastructure.logging.logger import (
    LoggerFactory,
)


def test_logger_instances_are_isolated() -> None:
    factory = LoggerFactory(
        Path("test_logs"),
    )

    first = factory.create(
        "runtime",
    )

    second = factory.create(
        "audit",
    )

    assert first.name != second.name

    assert len(first.handlers) == 2
    assert len(second.handlers) == 2


def test_logger_recreation_does_not_duplicate_handlers() -> None:
    factory = LoggerFactory(
        Path("test_logs"),
    )

    logger = factory.create(
        "runtime",
    )

    factory.create(
        "runtime",
    )

    assert len(logger.handlers) == 2
