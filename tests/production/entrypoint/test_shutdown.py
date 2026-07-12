from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)
from pocketbot.production.entrypoint.shutdown import (
    ProductionShutdown,
)


def test_production_shutdown() -> None:
    runtime_context = create_production_runtime_context()

    shutdown = ProductionShutdown(
        runtime_context,
    )

    assert shutdown.shutdown() is True

    assert (
        runtime_context.context.metrics.get("shutdown")
        == 1
    )
