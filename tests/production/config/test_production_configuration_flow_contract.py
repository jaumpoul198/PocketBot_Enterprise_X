from __future__ import annotations

from pocketbot.production.config.factory import (
    load_production_settings,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)


def test_full_production_configuration_flow_returns_settings() -> None:
    settings = load_production_settings()

    assert isinstance(settings, ProductionSettings)


def test_full_production_configuration_flow_resolves_environment() -> None:
    settings = load_production_settings()

    assert settings.environment == "production"


def test_full_production_configuration_flow_has_service_identity() -> None:
    settings = load_production_settings()

    assert settings.service_name
    assert settings.service_name.strip()


def test_full_production_configuration_flow_keeps_debug_disabled() -> None:
    settings = load_production_settings()

    assert settings.debug is False
