"""
PocketBot Enterprise X

Application runtime state machine tests.
"""

from __future__ import annotations

import pytest

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.application.runtime.state import (
    ApplicationState,
)


class RecordingLifecycle:
    def __init__(self) -> None:
        self.starts = 0
        self.stops = 0

    def start(self) -> None:
        self.starts += 1

    def stop(self) -> None:
        self.stops += 1


class RecordingPublisher:
    def __init__(self) -> None:
        self.events: list[str] = []

    def publish(
        self,
        name: str,
        payload: dict[str, object],
    ) -> None:
        self.events.append(name)


class StubSessionManager:
    pass


def create_runtime() -> tuple[ApplicationRuntime, RecordingLifecycle]:
    lifecycle = RecordingLifecycle()

    runtime = ApplicationRuntime(
        lifecycle=lifecycle,
        session_manager=StubSessionManager(),
        publisher=RecordingPublisher(),
    )

    return runtime, lifecycle


def test_start_is_idempotent() -> None:
    runtime, lifecycle = create_runtime()

    runtime.start()
    runtime.start()

    assert lifecycle.starts == 1
    assert runtime.state is ApplicationState.RUNNING


def test_stop_is_idempotent() -> None:
    runtime, lifecycle = create_runtime()

    runtime.start()
    runtime.stop()
    runtime.stop()

    assert lifecycle.stops == 1
    assert runtime.state is ApplicationState.STOPPED


def test_start_after_stop_is_not_allowed() -> None:
    runtime, _ = create_runtime()

    runtime.start()
    runtime.stop()

    with pytest.raises(RuntimeError):
        runtime.start()


def test_stop_from_created_is_safe() -> None:
    runtime, lifecycle = create_runtime()

    runtime.stop()

    assert lifecycle.stops == 1
    assert runtime.state is ApplicationState.STOPPED
