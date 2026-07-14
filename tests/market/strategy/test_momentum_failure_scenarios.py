import math

from pocketbot.market.strategy.models import StrategySignal
from pocketbot.market.strategy.momentum import MomentumStrategy


def test_momentum_rejects_none_data() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(None)

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_momentum_rejects_non_dict_data() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(["rsi", 20])

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_momentum_rejects_string_rsi() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": "20",
            "macd": 1.0,
            "macd_signal": 0.5,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_momentum_rejects_boolean_rsi() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": True,
            "macd": 1.0,
            "macd_signal": 0.5,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_momentum_rejects_nan_values() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": math.nan,
            "macd": 1.0,
            "macd_signal": 0.5,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_momentum_rejects_infinite_values() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": math.inf,
            "macd": 1.0,
            "macd_signal": 0.5,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
