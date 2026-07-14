"""
PocketBot Enterprise X

Market filter tests.
"""

from datetime import datetime

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.filters.default_market_filter import (
    DefaultMarketFilter,
)


def create_candle(volume: float) -> Candle:
    return Candle(
        symbol="BTCUSDT",
        timeframe="1m",
        open=Price(100),
        high=Price(110),
        low=Price(90),
        close=Price(105),
        volume=volume,
        timestamp=datetime.now(),
    )


def test_filter_removes_invalid_volume():

    service = DefaultMarketFilter()

    result = service.apply(
        [
            create_candle(100),
            create_candle(-1),
        ]
    )

    assert len(result) == 1


def test_filter_preserves_valid_candles():

    service = DefaultMarketFilter()

    candles = [
        create_candle(10),
        create_candle(20),
    ]

    result = service.apply(candles)

    assert result == candles
