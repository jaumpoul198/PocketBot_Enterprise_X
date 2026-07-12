from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
)
from pocketbot.production.entrypoint.lifecycle import (
    ProductionLifecycle,
)


def test_production_lifecycle() -> None:
    runtime_context = create_production_runtime_context()

    lifecycle = ProductionLifecycle(
        runtime_context,
    )

    assert lifecycle.start() is True
    assert (
        runtime_context.context.metrics.get("startup")
        == 1
    )

    assert lifecycle.shutdown() is True
    assert (
        runtime_context.context.metrics.get("shutdown")
        == 1
    )
