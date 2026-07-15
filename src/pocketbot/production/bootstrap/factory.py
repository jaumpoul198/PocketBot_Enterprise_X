from __future__ import annotations

from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)
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
from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)


def create_production_runtime_context() -> ProductionRuntimeContext:
    """
    Creates the production runtime context with dependency injection.
    """

    settings = load_production_settings()

    context = create_production_context()

    provider = (
        ApplicationBuilder()
        .build()
    )

    lifecycle = provider.get_service(
        LifecycleManager,
    )

    runtime = ProductionRuntime(
        settings,
        lifecycle=lifecycle,
    )

    return ProductionRuntimeContext(
        runtime=runtime,
        context=context,
        lifecycle=lifecycle,
    )
