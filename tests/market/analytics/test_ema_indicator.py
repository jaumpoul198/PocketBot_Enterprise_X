from datetime import UTC, datetime

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.analytics.indicators.ema_indicator import (
    EMAIndicator,
)


def create_candle(close: float) -> Candle:
    return Candle(
        symbol="BTCUSDT",
        timeframe="60",
        open=Price(close),
        high=Price(close),
        low=Price(close),
        close=Price(close),
        volume=100,
        timestamp=datetime.now(UTC),
    )


def test_ema_calculates_exponential_average():

    candles = [
        create_candle(100),
        create_candle(102),
        create_candle(104),
    ]

    indicator = EMAIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result == 102.5


def test_ema_returns_none_when_not_enough_candles():

    candles = [
        create_candle(100),
        create_candle(102),
    ]

    indicator = EMAIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result is None


def test_ema_requires_positive_period():

    try:
        EMAIndicator(
            period=0
        )

        assert False

    except ValueError:
        assert True

def test_ema_returns_none_for_empty_candles() -> None:

    indicator = EMAIndicator(
        period=3,
    )

    result = indicator.calculate(
        []
    )

    assert result is None


def test_ema_rejects_negative_period() -> None:

    try:
        EMAIndicator(
            period=-1,
        )

        assert False

    except ValueError:
        assert True


def test_ema_with_period_one_returns_last_price() -> None:

    candles = [
        create_candle(100),
        create_candle(105),
    ]

    indicator = EMAIndicator(
        period=1,
    )

    result = indicator.calculate(
        candles,
    )

    assert result == 105