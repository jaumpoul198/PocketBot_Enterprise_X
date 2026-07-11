"""
PocketBot Enterprise X

Trading flow integration tests.
"""

from __future__ import annotations

from datetime import UTC, datetime

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)
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


def create_candles() -> list[Candle]:
    timestamp = datetime.now(UTC)

    return [
        Candle(
            symbol="BTCUSDT",
            timeframe="60",
            open=Price(100.0 + index),
            high=Price(105.0 + index),
            low=Price(95.0 + index),
            close=Price(102.0 + index),
            volume=1000.0 + index,
            timestamp=timestamp,
        )
        for index in range(50)
    ]

def test_trading_application_flow_full_integration() -> None:

    provider = (
        ApplicationBuilder()
        .build()
    )

    repository = provider.get_service(
        MarketRepository,
    )

    snapshot = MarketSnapshot(
        asset="BTCUSDT",
        timeframe=60,
        candles=create_candles(),
        provider="integration-test",
        connected=True,
    )

    repository.save(
        snapshot,
    )

    flow = provider.get_service(
        TradingApplicationFlow,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "rsi",
            "ema",
            "macd",
        ],
    )

    result = flow.execute(
        request,
    )

    assert result is not None
    assert result.market is not None
    assert result.market.asset == "BTCUSDT"
    assert result.indicators is not None
    assert result.score is not None
    assert result.decision is not None
