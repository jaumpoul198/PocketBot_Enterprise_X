from pocketbot.market.strategy.models import StrategySignal
from pocketbot.market.strategy.momentum import MomentumStrategy


def test_momentum_strategy_buy_signal() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": 25,
            "macd": 2.0,
            "macd_signal": 1.0,
        }
    )

    assert result.signal == StrategySignal.BUY
    assert result.confidence == 0.8
    assert result.reason == "RSI oversold with MACD bullish crossover"


def test_momentum_strategy_sell_signal() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": 75,
            "macd": 0.5,
            "macd_signal": 1.0,
        }
    )

    assert result.signal == StrategySignal.SELL
    assert result.confidence == 0.8
    assert result.reason == "RSI overbought with MACD bearish crossover"


def test_momentum_strategy_hold_signal() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": 50,
            "macd": 1.0,
            "macd_signal": 1.0,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.5
    assert result.reason == "No momentum confirmation"


def test_momentum_strategy_missing_indicators() -> None:
    strategy = MomentumStrategy()

    result = strategy.analyze(
        {
            "rsi": 50,
        }
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
    assert result.reason == "Missing RSI or MACD indicators"
