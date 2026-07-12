from __future__ import annotations

from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)
from pocketbot.production.bootstrap.readiness import (
    ProductionReadiness,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


def create_production_runtime() -> ProductionRuntimeContext:
    return create_production_runtime_context()


def run_production() -> bool:
    runtime_context = create_production_runtime()

    readiness = ProductionReadiness(
        runtime_context,
    )

    if not readiness.check().ready:
        return False

    return runtime_context.start()
