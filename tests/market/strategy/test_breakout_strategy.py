from pocketbot.market.strategy.breakout import BreakoutStrategy
from pocketbot.market.strategy.models import StrategySignal


def test_breakout_buy_signal() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": 111.0,
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.BUY
    assert result.confidence == 0.9
    assert result.reason == "Price broke above resistance"


def test_breakout_sell_signal() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": 94.0,
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.SELL
    assert result.confidence == 0.9
    assert result.reason == "Price broke below support"


def test_breakout_hold_signal() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": 100.0,
            "support": 95.0,
            "resistance": 110.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.5
    assert result.reason == "Price within support and resistance"


def test_breakout_missing_levels() -> None:
    strategy = BreakoutStrategy()

    result = strategy.analyze(
        {
            "price": 100.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
    assert result.reason == "Missing support or resistance levels"
