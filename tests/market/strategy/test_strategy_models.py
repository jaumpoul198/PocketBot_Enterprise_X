from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


def test_strategy_signal_values():
    assert StrategySignal.BUY.value == "BUY"
    assert StrategySignal.SELL.value == "SELL"
    assert StrategySignal.HOLD.value == "HOLD"


def test_strategy_result_creation():
    result = StrategyResult(
        signal=StrategySignal.BUY,
        confidence=0.85,
        reason="Strong bullish signal",
    )

    assert result.signal == StrategySignal.BUY
    assert result.confidence == 0.85
    assert result.reason == "Strong bullish signal"
