from datetime import UTC, datetime

import pytest

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.analytics.indicators.bollinger_bands_indicator import (
    BollingerBandsIndicator,
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


def test_bollinger_bands_calculates_values():

    candles = [
        create_candle(100),
        create_candle(102),
        create_candle(104),
    ]

    indicator = BollingerBandsIndicator(
        period=3,
        multiplier=2,
    )

    result = indicator.calculate(
        candles
    )

    assert result is not None

    assert result.middle == 102
    assert result.upper > result.middle
    assert result.lower < result.middle


def test_bollinger_bands_returns_none_without_enough_candles():

    candles = [
        create_candle(100),
    ]

    indicator = BollingerBandsIndicator(
        period=3,
        multiplier=2,
    )

    result = indicator.calculate(
        candles
    )

    assert result is None


def test_bollinger_bands_requires_positive_period():

    with pytest.raises(ValueError):

        BollingerBandsIndicator(
            period=0,
            multiplier=2,
        )
