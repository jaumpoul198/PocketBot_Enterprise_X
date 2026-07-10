"""
PocketBot Enterprise X

Trading session execution flow integration tests.
"""

from __future__ import annotations

from datetime import datetime

from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.application.session.models import (
    TradingSessionStatus,
)
from pocketbot.application.session.trading_session_manager import (
    TradingSessionManager,
)
from pocketbot.bootstrap import build_application
from pocketbot.domain.candle import (
    Candle,
)
from pocketbot.domain.value_objects.price import (
    Price,
)
from pocketbot.market.interfaces.market_repository import (
    MarketRepository,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


def test_trading_session_executes_complete_flow() -> None:
    """
    Validates complete trading execution through session manager.
    """

    provider = build_application()

    repository = provider.get_service(
        MarketRepository,
    )

    repository.save(
        MarketSnapshot(
            asset="BTCUSDT",
            timeframe=60,
            candles=[
                Candle(
                    symbol="BTCUSDT",
                    timeframe="60",
                    open=Price(100.0),
                    high=Price(105.0),
                    low=Price(95.0),
                    close=Price(102.0),
                    volume=1000.0,
                    timestamp=datetime.now(),
                )
                for _ in range(100)
            ],
        )
    )

    manager = provider.get_service(
        TradingSessionManager,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
    )

    session = manager.create_session(
        request,
    )

    assert session.status is TradingSessionStatus.CREATED

    result = manager.execute(
        session,
    )

    assert result is not None

    assert session.status is TradingSessionStatus.COMPLETED

    assert session.result == result
