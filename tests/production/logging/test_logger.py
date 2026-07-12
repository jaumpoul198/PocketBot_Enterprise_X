from pocketbot.production.logging.logger import create_production_logger


def test_create_production_logger() -> None:
    logger = create_production_logger()

    assert logger.name == "pocketbot"
    assert logger.level > 0


def test_create_named_logger() -> None:
    logger = create_production_logger("enterprise")

    assert logger.name == "enterprise"
