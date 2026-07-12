from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)


class FakeStartup:
    def __init__(self) -> None:
        self.calls = 0

    def execute(self) -> None:
        self.calls += 1


class FakeShutdown:
    def __init__(self) -> None:
        self.calls = 0

    def execute(self) -> None:
        self.calls += 1


def test_lifecycle_manager_start_delegates_to_startup() -> None:
    startup = FakeStartup()
    shutdown = FakeShutdown()

    lifecycle = LifecycleManager(
        startup=startup,
        shutdown=shutdown,
    )

    lifecycle.start()

    assert startup.calls == 1
    assert shutdown.calls == 0


def test_lifecycle_manager_stop_delegates_to_shutdown() -> None:
    startup = FakeStartup()
    shutdown = FakeShutdown()

    lifecycle = LifecycleManager(
        startup=startup,
        shutdown=shutdown,
    )

    lifecycle.stop()

    assert startup.calls == 0
    assert shutdown.calls == 1
