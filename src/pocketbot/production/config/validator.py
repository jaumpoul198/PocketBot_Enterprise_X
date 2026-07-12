from __future__ import annotations

from pocketbot.production.config.settings import ProductionSettings


def validate_production_settings(
    settings: ProductionSettings,
) -> None:
    if not settings.service_name.strip():
        raise ValueError(
            "service_name must not be empty"
        )

    if settings.environment == "production" and settings.debug:
        raise ValueError(
            "debug mode is not allowed in production"
        )
