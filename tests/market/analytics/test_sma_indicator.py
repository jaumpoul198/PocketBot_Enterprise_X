from datetime import UTC, datetime

import pytest

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.analytics.indicators.sma_indicator import (
    SMAIndicator,
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


def test_sma_calculates_simple_moving_average():

    candles = [
        create_candle(100),
        create_candle(102),
        create_candle(104),
    ]

    indicator = SMAIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result == 102


def test_sma_returns_none_when_not_enough_candles():

    candles = [
        create_candle(100),
        create_candle(102),
    ]

    indicator = SMAIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result is None


def test_sma_uses_last_period_candles_only():

    candles = [
        create_candle(90),
        create_candle(100),
        create_candle(110),
        create_candle(120),
    ]

    indicator = SMAIndicator(
        period=3
    )

    result = indicator.calculate(
        candles
    )

    assert result == 110


def test_sma_requires_positive_period():

    with pytest.raises(ValueError):

        SMAIndicator(
            period=0
        )

def test_sma_returns_none_for_empty_candles():

    indicator = SMAIndicator(
        period=3
    )

    result = indicator.calculate(
        []
    )

    assert result is None


def test_sma_requires_positive_negative_period():

    with pytest.raises(ValueError):

        SMAIndicator(
            period=-1
        )
