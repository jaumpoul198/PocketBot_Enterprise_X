from pocketbot.production.logging.logger import (
    create_production_logger,
)


def test_logger_contract_does_not_duplicate_handlers() -> None:
    first = create_production_logger(
        "isolated-service",
    )

    handler_count = len(first.handlers)

    second = create_production_logger(
        "isolated-service",
    )

    assert first is second
    assert len(second.handlers) == handler_count


def test_logger_contract_isolates_different_names() -> None:
    first = create_production_logger(
        "service-a",
    )

    second = create_production_logger(
        "service-b",
    )

    assert first.name == "service-a"
    assert second.name == "service-b"
    assert first is not second


def test_logger_contract_has_production_level() -> None:
    logger = create_production_logger()

    assert logger.level == 20
