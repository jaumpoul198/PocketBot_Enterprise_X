from pocketbot.decision.engine import DecisionEngine
from pocketbot.domain.enums import SignalType
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)
from pocketbot.score.result import ScoreResult


def create_score() -> ScoreResult:
    return ScoreResult(
        score=90.0,
        confidence=0.90,
        strength=0.90,
        weight_sum=1.0,
        indicators=3,
    )


def test_decision_accepts_strategy_buy():

    engine = DecisionEngine()

    result = engine.decide(
        create_score(),
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=0.90,
            reason="momentum buy",
        ),
    )

    assert result.signal == SignalType.BUY
    assert result.approved is True


def test_decision_blocks_strategy_hold():

    engine = DecisionEngine()

    result = engine.decide(
        create_score(),
        StrategyResult(
            signal=StrategySignal.HOLD,
            confidence=0.50,
            reason="no clear trend",
        ),
    )

    assert result.signal == SignalType.NEUTRAL
    assert result.approved is False
