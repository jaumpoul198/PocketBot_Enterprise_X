from pocketbot.production.config.factory import load_production_settings
from pocketbot.production.config.settings import ProductionSettings


def test_factory_returns_production_settings() -> None:
    settings = load_production_settings()

    assert isinstance(settings, ProductionSettings)


def test_factory_loads_production_environment() -> None:
    settings = load_production_settings()

    assert settings.environment == "production"


def test_factory_returns_consistent_configuration() -> None:
    first = load_production_settings()
    second = load_production_settings()

    assert first.environment == second.environment
    assert first.debug == second.debug
