"""
PocketBot Enterprise X

Application runtime failure scenarios tests.
"""

from __future__ import annotations

import pytest

from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)


class FailingLifecycle:
    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass


class FailingSessionManager:

    def create_session(
        self,
        request: TradingRequest,
    ):
        return "session"

    def execute(
        self,
        session,
    ):
        raise RuntimeError(
            "session execution failure"
        )


class RecordingPublisher:

    def __init__(self) -> None:
        self.events: list[str] = []

    def publish(
        self,
        name: str,
        payload: dict[str, object],
    ) -> None:
        self.events.append(name)


def test_runtime_run_propagates_session_execution_failure() -> None:

    publisher = RecordingPublisher()

    runtime = ApplicationRuntime(
        lifecycle=FailingLifecycle(),
        session_manager=FailingSessionManager(),
        publisher=publisher,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "rsi",
        ],
    )

    with pytest.raises(
        RuntimeError,
        match="session execution failure",
    ):
        runtime.run(
            request,
        )

    assert "application.started" in publisher.events


def test_runtime_start_failure_does_not_enter_running_state() -> None:

    class BrokenLifecycle:

        def start(self) -> None:
            raise RuntimeError(
                "runtime startup broken"
            )

        def stop(self) -> None:
            pass


    publisher = RecordingPublisher()

    runtime = ApplicationRuntime(
        lifecycle=BrokenLifecycle(),
        session_manager=FailingSessionManager(),
        publisher=publisher,
    )

    with pytest.raises(
        RuntimeError,
        match="runtime startup broken",
    ):
        runtime.start()

    assert runtime.is_running is False
