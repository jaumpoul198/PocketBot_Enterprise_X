from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.application.lifecycle.shutdown import (
    Shutdown,
)
from pocketbot.application.lifecycle.startup import (
    Startup,
)


class FailingStartup:
    def execute(self) -> None:
        raise RuntimeError("startup failed")


class FailingShutdown:
    def execute(self) -> None:
        raise RuntimeError("shutdown failed")


class StubHostedServices:
    def __init__(self) -> None:
        self.calls = []

    def stop(self) -> None:
        self.calls.append("stop")


class StubProvider:
    def __init__(self, calls: list[str]) -> None:
        self.calls = calls

    def dispose(self) -> None:
        self.calls.append("dispose")


def test_lifecycle_start_propagates_startup_failure() -> None:
    lifecycle = LifecycleManager(
        startup=FailingStartup(),
        shutdown=FailingShutdown(),
    )

    try:
        lifecycle.start()
        assert False
    except RuntimeError as exc:
        assert str(exc) == "startup failed"


def test_lifecycle_stop_propagates_shutdown_failure() -> None:
    lifecycle = LifecycleManager(
        startup=FailingStartup(),
        shutdown=FailingShutdown(),
    )

    try:
        lifecycle.stop()
        assert False
    except RuntimeError as exc:
        assert str(exc) == "shutdown failed"


def test_shutdown_preserves_stop_before_dispose_order() -> None:
    calls: list[str] = []

    shutdown = Shutdown(
        hosted_services=StubHostedServices(),
        provider=StubProvider(calls),
    )

    shutdown.execute()

    assert calls == ["dispose"]
