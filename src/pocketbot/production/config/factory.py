from __future__ import annotations

import os

from pocketbot.production.config.environments import resolve_environment
from pocketbot.production.config.profiles import default_profile
from pocketbot.production.config.settings import ProductionSettings


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
        else default_profile.debug
    )

    return ProductionSettings(
        environment=environment.name,
        debug=debug,
        service_name=os.getenv(
            "POCKETBOT_SERVICE_NAME",
            default_profile.service_name,
        ),
        environment_config=environment,
    )
