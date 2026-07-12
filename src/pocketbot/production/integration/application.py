from __future__ import annotations

from pocketbot.production.bootstrap.runtime import ProductionRuntime
from pocketbot.production.config.factory import load_production_settings


def create_production_application() -> ProductionRuntime:
    settings = load_production_settings()

    return ProductionRuntime(settings)


def start_production_application() -> bool:
    runtime = create_production_application()

    return runtime.start()
