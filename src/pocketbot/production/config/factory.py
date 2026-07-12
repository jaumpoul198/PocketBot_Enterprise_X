from __future__ import annotations

import os

from pocketbot.production.config.settings import ProductionSettings


def load_production_settings() -> ProductionSettings:
    return ProductionSettings(
        environment=os.getenv("POCKETBOT_ENV", "production"),
        debug=os.getenv("POCKETBOT_DEBUG", "false").lower() == "true",
        service_name=os.getenv("POCKETBOT_SERVICE_NAME", "pocketbot"),
    )
