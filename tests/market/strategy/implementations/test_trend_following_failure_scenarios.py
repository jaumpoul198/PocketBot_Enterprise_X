import math

import pytest

from pocketbot.market.strategy.implementations.trend_following import (
    TrendFollowingStrategy,
)
from pocketbot.market.strategy.models import StrategySignal


def test_rejects_invalid_market_data_type() -> None:
    strategy = TrendFollowingStrategy()

    result = strategy.analyze(
        None,
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_rejects_non_numeric_ema() -> None:
    strategy = TrendFollowingStrategy()

    with pytest.raises(TypeError):
        strategy.analyze(
            {
                "ema": "120",
                "sma": 100,
            }
        )


def test_rejects_non_numeric_sma() -> None:
    strategy = TrendFollowingStrategy()

    with pytest.raises(TypeError):
        strategy.analyze(
            {
                "ema": 120,
                "sma": "100",
            }
        )


def test_rejects_boolean_moving_average_values() -> None:
    strategy = TrendFollowingStrategy()

    with pytest.raises(TypeError):
        strategy.analyze(
            {
                "ema": True,
                "sma": 100,
            }
        )


def test_rejects_nan_values() -> None:
    strategy = TrendFollowingStrategy()

    with pytest.raises(ValueError):
        strategy.analyze(
            {
                "ema": math.nan,
                "sma": 100,
            }
        )
