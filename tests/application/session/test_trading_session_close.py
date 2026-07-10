"""
PocketBot Enterprise X

Trading session close lifecycle tests.
"""

from __future__ import annotations

import pytest

from pocketbot.application.pipeline.models import (
    TradingRequest,
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
from pocketbot.bootstrap import build_application


def test_close_completed_session() -> None:
    """
    Validates closing a completed trading session.
    """

    provider = build_application()

    manager = provider.get_service(
        TradingSessionManager,
    )

    session = manager.create_session(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=60,
        )
    )

    session.status = TradingSessionStatus.COMPLETED

    manager.close(
        session,
    )

    assert session.status is TradingSessionStatus.CLOSED


def test_close_running_session_fails() -> None:
    """
    Validates that running sessions cannot be closed.
    """

    provider = build_application()

    manager = provider.get_service(
        TradingSessionManager,
    )

    session = manager.create_session(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=60,
        )
    )

    session.status = TradingSessionStatus.RUNNING

    with pytest.raises(
        InvalidTradingSessionError,
    ):
        manager.close(
            session,
        )


def test_close_already_closed_session_fails() -> None:
    """
    Validates duplicate close protection.
    """

    provider = build_application()

    manager = provider.get_service(
        TradingSessionManager,
    )

    session = manager.create_session(
        TradingRequest(
            asset="BTCUSDT",
            timeframe=60,
        )
    )

    session.status = TradingSessionStatus.CLOSED

    with pytest.raises(
        InvalidTradingSessionError,
    ):
        manager.close(
            session,
        )
