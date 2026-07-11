"""
PocketBot Enterprise X

Application Service trading pipeline integration tests.
"""

from __future__ import annotations

from datetime import datetime

from pocketbot.application.pipeline.models import (
    TradingRequest,
)
from pocketbot.application.services.application_service import (
    ApplicationService,
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
from pocketbot.market.interfaces import (
    MarketRepository,
)
from pocketbot.market.models.market_snapshot import (
    MarketSnapshot,
)


def test_application_service_executes_trading_pipeline() -> None:
    provider = (
        ApplicationBuilder()
        .build()
    )

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

    application_service = provider.get_service(
        ApplicationService,
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

    result = application_service.execute_pipeline(
        request,
    )

    assert result.market.asset == "BTCUSDT"
    assert result.indicators
    assert result.score is not None
    assert result.decision is not None
