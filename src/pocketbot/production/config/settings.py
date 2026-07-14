from __future__ import annotations

from dataclasses import dataclass

from pocketbot.production.config.environments import (
    EnvironmentConfig,
    production_environment,
)


@dataclass(frozen=True)
class ProductionSettings:
    environment: str = "production"
    debug: bool = False
    service_name: str = "pocketbot"
    environment_config: EnvironmentConfig = production_environment
