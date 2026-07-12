from __future__ import annotations

from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


def create_production_runtime() -> ProductionRuntimeContext:
    return create_production_runtime_context()


def run_production() -> bool:
    runtime_context = create_production_runtime_context()

    return runtime_context.start()
