from datetime import UTC, datetime

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.analytics.indicators.macd_indicator import (
    MACDIndicator,
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


def test_macd_calculates_difference_between_averages():

    candles = [
        create_candle(100),
        create_candle(102),
        create_candle(104),
        create_candle(106),
        create_candle(108),
    ]

    indicator = MACDIndicator(
        fast_period=3,
        slow_period=5,
    )

    result = indicator.calculate(
        candles
    )

    assert result == 2


def test_macd_returns_none_without_enough_candles():

    candles = [
        create_candle(100),
        create_candle(102),
    ]

    indicator = MACDIndicator(
        fast_period=3,
        slow_period=5,
    )

    result = indicator.calculate(
        candles
    )

    assert result is None


def test_macd_requires_valid_periods():

    try:
        MACDIndicator(
            fast_period=0,
            slow_period=5,
        )

        assert False

    except ValueError:
        assert True

def test_macd_rejects_invalid_slow_period() -> None:

    try:
        MACDIndicator(
            fast_period=3,
            slow_period=0,
        )

        assert False

    except ValueError:
        assert True


def test_macd_rejects_fast_period_greater_than_or_equal_slow_period() -> None:

    try:
        MACDIndicator(
            fast_period=5,
            slow_period=5,
        )

        assert False

    except ValueError:
        assert True


def test_macd_returns_none_for_empty_candles() -> None:

    indicator = MACDIndicator(
        fast_period=3,
        slow_period=5,
    )

    result = indicator.calculate(
        []
    )

    assert result is None
