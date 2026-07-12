from __future__ import annotations

import pytest

from pocketbot.production.config.settings import ProductionSettings
from pocketbot.production.config.validator import (
    validate_production_settings,
)


def test_validator_rejects_empty_service_name() -> None:
    settings = ProductionSettings(
        environment="production",
        debug=False,
        service_name="   ",
    )

    with pytest.raises(ValueError):
        validate_production_settings(settings)


def test_validator_rejects_production_debug_mode() -> None:
    settings = ProductionSettings(
        environment="production",
        debug=True,
        service_name="pocketbot",
    )

    with pytest.raises(ValueError):
        validate_production_settings(settings)


def test_validator_accepts_valid_production_settings() -> None:
    settings = ProductionSettings(
        environment="production",
        debug=False,
        service_name="pocketbot",
    )

    validate_production_settings(settings)
