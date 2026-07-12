from pocketbot.production.bootstrap.context import (
    create_production_context,
)
from pocketbot.production.bootstrap.runtime import (
    ProductionRuntime,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.bootstrap.runtime_health import (
    ProductionRuntimeHealth,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)


def test_runtime_health() -> None:
    context = create_production_context()
    runtime = ProductionRuntime(
        ProductionSettings()
    )

    runtime_context = ProductionRuntimeContext(
        runtime,
        context,
    )

    health = ProductionRuntimeHealth(
        runtime_context,
    )

    status = health.check()

    assert status.healthy is True
