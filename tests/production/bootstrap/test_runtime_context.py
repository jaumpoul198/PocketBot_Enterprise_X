from pocketbot.production.bootstrap.context import (
    create_production_context,
)
from pocketbot.production.bootstrap.runtime import (
    ProductionRuntime,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)


def test_runtime_context_lifecycle() -> None:
    context = create_production_context()
    runtime = ProductionRuntime(
        ProductionSettings()
    )

    runtime_context = ProductionRuntimeContext(
        runtime,
        context,
    )

    assert runtime_context.start() is True
    assert context.metrics.get("startup") == 1

    assert runtime_context.shutdown() is True
    assert context.metrics.get("shutdown") == 1
