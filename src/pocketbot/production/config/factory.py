from __future__ import annotations

import os

from pocketbot.production.config.environments import (
    resolve_environment,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)
from pocketbot.production.config.validator import (
    validate_production_settings,
)


def load_production_settings() -> ProductionSettings:
    environment = resolve_environment(
        os.getenv("POCKETBOT_ENV")
    )

    debug_override = os.getenv(
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
        service_name=os.getenv(
            "POCKETBOT_SERVICE_NAME",
            "pocketbot",
        ),
    )

    validate_production_settings(settings)

    return settings
