from pocketbot.market.strategy.ensemble.models import EnsembleResult
from pocketbot.market.strategy.models import StrategySignal


def test_ensemble_result_creation() -> None:
    result = EnsembleResult(
        signal=StrategySignal.BUY,
        confidence=0.75,
        votes={
            "trend": StrategySignal.BUY,
            "momentum": StrategySignal.BUY,
            "breakout": StrategySignal.HOLD,
        },
        reason="Majority vote selected BUY",
    )

    assert result.signal == StrategySignal.BUY
    assert result.confidence == 0.75
    assert len(result.votes) == 3
    assert result.reason == "Majority vote selected BUY"
