import pytest

from pocketbot.production.bootstrap.factory import (
    create_production_runtime_context,
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
from pocketbot.production.config.settings import (
    ProductionSettings,
)


def test_runtime_context_start_failure_isolated() -> None:
    context = create_production_context()

    class BrokenRuntime(ProductionRuntime):
        def start(self) -> bool:
            raise RuntimeError("startup failure")

    runtime_context = ProductionRuntimeContext(
        BrokenRuntime(
            ProductionSettings()
        ),
        context,
    )

    with pytest.raises(RuntimeError):
        runtime_context.start()


def test_factory_creates_complete_runtime_context() -> None:
    runtime_context = create_production_runtime_context()

    assert runtime_context.runtime is not None
    assert runtime_context.context is not None


def test_runtime_shutdown_failure_isolated() -> None:
    context = create_production_context()

    class BrokenRuntime(ProductionRuntime):
        def shutdown(self) -> bool:
            raise RuntimeError("shutdown failure")

    runtime_context = ProductionRuntimeContext(
        BrokenRuntime(
            ProductionSettings()
        ),
        context,
    )

    with pytest.raises(RuntimeError):
        runtime_context.shutdown()
