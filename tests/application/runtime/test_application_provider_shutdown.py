from __future__ import annotations

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.application.runtime.state import (
    ApplicationState,
)


class DisposableProvider:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


class StubLifecycle:
    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass


class StubSessionManager:
    pass


class StubPublisher:
    def publish(
        self,
        name: str,
        payload: dict[str, object],
    ) -> None:
        pass


def test_runtime_disposes_provider_on_shutdown() -> None:
    provider = DisposableProvider()

    runtime = ApplicationRuntime(
        provider=provider,
        lifecycle=StubLifecycle(),
        session_manager=StubSessionManager(),
        publisher=StubPublisher(),
    )

    runtime.start()

    runtime.stop()

    assert runtime.state is ApplicationState.STOPPED
    assert provider.dispose_calls == 1
