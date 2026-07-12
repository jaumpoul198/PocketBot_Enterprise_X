from pocketbot.production.bootstrap.context import (
    create_production_context,
)
from pocketbot.production.bootstrap.readiness import (
    ProductionReadiness,
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


def test_production_readiness() -> None:
    context = create_production_context()

    runtime = ProductionRuntime(
        ProductionSettings()
    )

    runtime_context = ProductionRuntimeContext(
        runtime,
        context,
    )

    readiness = ProductionReadiness(
        runtime_context,
    )

    status = readiness.check()

    assert status.ready is True
