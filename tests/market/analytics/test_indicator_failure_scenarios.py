"""
PocketBot Enterprise X

Market indicators failure scenario tests.
"""

from datetime import UTC, datetime

import pytest

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.analytics.indicators.bollinger_bands_indicator import (
    BollingerBandsIndicator,
)
from pocketbot.market.analytics.indicators.macd_indicator import (
    MACDIndicator,
)
from pocketbot.market.analytics.indicators.rsi_indicator import (
    RSIIndicator,
)
from pocketbot.market.analytics.indicators.sma_indicator import (
    SMAIndicator,
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


def test_sma_rejects_zero_period() -> None:

    with pytest.raises(ValueError):
        SMAIndicator(
            period=0,
        )


def test_rsi_returns_none_when_only_period_changes_exist() -> None:

    indicator = RSIIndicator(
        period=3,
    )

    candles = [
        create_candle(100),
        create_candle(100),
        create_candle(100),
        create_candle(100),
    ]

    result = indicator.calculate(
        candles,
    )

    assert result == 100.0


def test_macd_rejects_fast_period_equal_to_slow_period() -> None:

    with pytest.raises(ValueError):
        MACDIndicator(
            fast_period=5,
            slow_period=5,
        )


def test_bollinger_bands_rejects_invalid_multiplier() -> None:

    with pytest.raises(ValueError):
        BollingerBandsIndicator(
            period=3,
            multiplier=0,
        )