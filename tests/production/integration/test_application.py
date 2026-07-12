from pocketbot.production.integration.application import (
    create_production_application,
    start_production_application,
)


def test_create_production_application() -> None:
    application = create_production_application()

    assert application.settings.environment == "production"


def test_start_production_application() -> None:
    assert start_production_application() is True
