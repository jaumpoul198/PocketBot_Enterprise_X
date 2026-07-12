from __future__ import annotations

from pocketbot.production.bootstrap.runtime import ProductionRuntime
from pocketbot.production.config.factory import load_production_settings


def create_production_runtime() -> ProductionRuntime:
    settings = load_production_settings()
    return ProductionRuntime(settings)


def run_production() -> bool:
    runtime = create_production_runtime()

    started = runtime.start()

    if not started:
        return False

    return runtime.shutdown()
