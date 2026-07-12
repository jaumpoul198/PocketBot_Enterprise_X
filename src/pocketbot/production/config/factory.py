from __future__ import annotations

from pocketbot.production.config.environments import (
    resolve_environment,
)
from pocketbot.production.config.secrets import (
    SecretProvider,
    load_secret_settings,
    resolve_secret_provider,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)
from pocketbot.production.config.validator import (
    validate_production_settings,
)


def load_production_settings(
    secret_provider: SecretProvider | None = None,
) -> ProductionSettings:
    if secret_provider is not None:
        provider = secret_provider
    else:
        secret_settings = load_secret_settings(
            None,
        )
        provider = resolve_secret_provider(
            secret_settings,
        )

    environment = resolve_environment(
        provider.get_secret("POCKETBOT_ENV")
    )

    debug_override = provider.get_secret(
        "POCKETBOT_DEBUG"
    )

    debug = (
        debug_override.lower() == "true"
        if debug_override is not None
        else environment.debug
    )

    settings = ProductionSettings(
        environment=environment.name,
        debug=debug,
        service_name=provider.get_secret(
            "POCKETBOT_SERVICE_NAME"
        )
        or "pocketbot",
    )

    validate_production_settings(settings)

    return settings
