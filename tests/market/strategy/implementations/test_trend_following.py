from pocketbot.market.strategy.implementations.trend_following import (
    TrendFollowingStrategy,
)
from pocketbot.market.strategy.models import StrategySignal


def test_trend_following_buy_signal():

    strategy = TrendFollowingStrategy()

    result = strategy.analyze(
        {
            "ema": 120,
            "sma": 100,
        }
    )

    assert result.signal == StrategySignal.BUY


def test_trend_following_sell_signal():

    strategy = TrendFollowingStrategy()

    result = strategy.analyze(
        {
            "ema": 90,
            "sma": 100,
        }
    )

    assert result.signal == StrategySignal.SELL


def test_trend_following_hold_when_missing_data():

    strategy = TrendFollowingStrategy()

    result = strategy.analyze({})

    assert result.signal == StrategySignal.HOLD
