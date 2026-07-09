from datetime import UTC, datetime

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.analytics.indicators.rsi_indicator import (
    RSIIndicator,
)


def create_candle(price: float) -> Candle:
    return Candle(
        symbol="BTCUSDT",
        timeframe="60",
        open=Price(price),
        high=Price(price),
        low=Price(price),
        close=Price(price),
        volume=100,
        timestamp=datetime.now(UTC),
    )


def test_rsi_calculates_value():

    candles = [
        create_candle(100),
        create_candle(102),
        create_candle(104),
        create_candle(106),
    ]

    indicator = RSIIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result == 100


def test_rsi_returns_none_when_not_enough_candles():

    candles = [
        create_candle(100),
    ]

    indicator = RSIIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result is None


def test_rsi_requires_positive_period():

    try:
        RSIIndicator(period=0)
        assert False
    except ValueError:
        assert True
