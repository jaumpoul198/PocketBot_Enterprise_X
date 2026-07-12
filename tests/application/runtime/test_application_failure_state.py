from __future__ import annotations

import pytest

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.application.runtime.state import ApplicationState


class FailingLifecycle:
    def __init__(
        self,
        *,
        fail_start: bool = False,
        fail_stop: bool = False,
    ) -> None:
        self._fail_start = fail_start
        self._fail_stop = fail_stop

    def start(self) -> None:
        if self._fail_start:
            raise RuntimeError("startup failure")

    def stop(self) -> None:
        if self._fail_stop:
            raise RuntimeError("shutdown failure")


class StubSessionManager:
    pass


class RecordingPublisher:
    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, str]]] = []

    def publish(
        self,
        name: str,
        payload: dict[str, str],
    ) -> None:
        self.events.append((name, payload))


def test_runtime_enters_failed_state_when_startup_fails() -> None:
    publisher = RecordingPublisher()

    runtime = ApplicationRuntime(
        provider=object(),
        lifecycle=FailingLifecycle(fail_start=True),
        session_manager=StubSessionManager(),
        publisher=publisher,
    )

    with pytest.raises(RuntimeError, match="startup failure"):
        runtime.start()

    assert runtime.state is ApplicationState.FAILED
    assert (
        "application.startup.failed",
        {"error": "startup failure"},
    ) in publisher.events


def test_runtime_enters_failed_state_when_shutdown_fails() -> None:
    publisher = RecordingPublisher()

    runtime = ApplicationRuntime(
        provider=object(),
        lifecycle=FailingLifecycle(fail_stop=True),
        session_manager=StubSessionManager(),
        publisher=publisher,
    )

    runtime.start()

    with pytest.raises(RuntimeError, match="shutdown failure"):
        runtime.stop()

    assert runtime.state is ApplicationState.FAILED
    assert (
        "application.shutdown.failed",
        {"error": "shutdown failure"},
    ) in publisher.events
