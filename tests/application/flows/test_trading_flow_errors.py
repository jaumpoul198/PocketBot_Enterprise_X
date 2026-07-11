"""
PocketBot Enterprise X

Trading application flow error tests.
"""

from __future__ import annotations

import pytest

from pocketbot.application.flows.trading_flow import (
    TradingApplicationFlow,
)
from pocketbot.application.pipeline.exceptions import (
    TradingPipelineError,
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

from datetime import UTC, datetime


def create_snapshot() -> MarketSnapshot:

    timestamp = datetime.now(UTC)

    candles = [
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

    return MarketSnapshot(
        asset="BTCUSDT",
        timeframe=60,
        candles=candles,
        provider="integration-test",
        connected=True,
    )


def test_trading_flow_raises_error_when_market_snapshot_missing() -> None:

    provider = (
        ApplicationBuilder()
        .build()
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

    with pytest.raises(
        TradingPipelineError,
        match="Market snapshot not found.",
    ):
        flow.execute(
            request,
        )


def test_trading_flow_rejects_unknown_indicator() -> None:

    provider = (
        ApplicationBuilder()
        .build()
    )

    repository = provider.get_service(
        MarketRepository,
    )

    repository.save(
        create_snapshot(),
    )

    flow = provider.get_service(
        TradingApplicationFlow,
    )

    request = TradingRequest(
        asset="BTCUSDT",
        timeframe=60,
        indicators=[
            "unknown_indicator",
        ],
    )

    with pytest.raises(
        Exception,
    ):
        flow.execute(
            request,
        )
