from __future__ import annotations

from pocketbot.production.config.factory import (
    load_production_settings,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)


def test_factory_returns_validated_production_settings() -> None:
    settings = load_production_settings()

    assert isinstance(settings, ProductionSettings)
    assert settings.service_name.strip()


def test_factory_defaults_to_safe_production_configuration() -> None:
    settings = load_production_settings()

    assert settings.environment == "production"
    assert settings.debug is False


