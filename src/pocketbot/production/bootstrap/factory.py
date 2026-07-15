from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)
from pocketbot.production.bootstrap.context import (
    create_production_context,
)
from pocketbot.production.bootstrap.health_runtime import (
    ProductionHealthRuntime,
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

    runtime_context = ProductionRuntimeContext(
        runtime=runtime,
        context=context,
        lifecycle=lifecycle,
    )

    health_runtime = ProductionHealthRuntime(
        runtime_context,
        settings.health_port,
    )

    runtime_context.attach_health_runtime(
        health_runtime,
    )

    return runtime_context
