"""
PocketBot Enterprise X

Trading session manager tests.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.session.exceptions import (
    InvalidTradingSessionError,
)
from pocketbot.application.session.models import (
    TradingSessionStatus,
)
from pocketbot.application.session.trading_session_manager import (
    TradingSessionManager,
)


class FakeOrchestrator:
    """
    Fake trading orchestrator for tests.
    """

    def __init__(self) -> None:
        self.called = False

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:
        self.called = True

        return MagicMock(
            spec=TradingResult,
        )


def create_request() -> TradingRequest:
    """
    Creates a test trading request.
    """

    return TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "rsi",
        ],
    )


def test_create_session() -> None:
    orchestrator = FakeOrchestrator()

    manager = TradingSessionManager(
        orchestrator=orchestrator,  # type: ignore[arg-type]
    )

    session = manager.create_session(
        create_request(),
    )

    assert session.session_id
    assert session.status is TradingSessionStatus.CREATED
    assert session.result is None


def test_execute_session() -> None:
    orchestrator = FakeOrchestrator()

    manager = TradingSessionManager(
        orchestrator=orchestrator,  # type: ignore[arg-type]
    )

    session = manager.create_session(
        create_request(),
    )

    result = manager.execute(
        session,
    )

    assert result is not None
    assert orchestrator.called is True
    assert session.status is TradingSessionStatus.COMPLETED
    assert session.result is result


def test_execute_completed_session_fails() -> None:
    orchestrator = FakeOrchestrator()

    manager = TradingSessionManager(
        orchestrator=orchestrator,  # type: ignore[arg-type]
    )

    session = manager.create_session(
        create_request(),
    )

    manager.execute(
        session,
    )

    with pytest.raises(
        InvalidTradingSessionError,
    ):
        manager.execute(
            session,
        )
