from __future__ import annotations

from pocketbot.production.bootstrap.context import (
    create_production_context,
)
from pocketbot.production.bootstrap.runtime import (
    ProductionRuntime,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.config.factory import (
    load_production_settings,
)


def create_production_runtime_context() -> ProductionRuntimeContext:
    settings = load_production_settings()
    context = create_production_context()
    runtime = ProductionRuntime(settings)

    return ProductionRuntimeContext(
        runtime,
        context,
    )
