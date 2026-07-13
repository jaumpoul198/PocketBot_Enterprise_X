import math

from pocketbot.market.strategy.breakout import BreakoutStrategy
from pocketbot.market.strategy.models import StrategySignal


def test_breakout_rejects_none_data() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(None)

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_breakout_rejects_non_dict_data() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(["price", 100])

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_breakout_rejects_string_price() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": "100",
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_breakout_rejects_boolean_price() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": True,
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_breakout_rejects_nan_values() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": math.nan,
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_breakout_rejects_infinite_values() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": math.inf,
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
