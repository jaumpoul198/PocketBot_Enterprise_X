"""
PocketBot Enterprise X

Trade Engine tests.
"""

from __future__ import annotations

import pytest

from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.execution.result import ExecutionResult
from pocketbot.risk.result import RiskResult
from pocketbot.score.result import ScoreResult
from pocketbot.trading.engine import TradeEngine
from pocketbot.trading.result import TradeResult


class StubDecisionEngine:
    """
    Stub decision engine for tests.
    """

    def decide(
        self,
        score: ScoreResult,
    ) -> DecisionResult:

        return DecisionResult(
            signal=SignalType.BUY,
            score=score.score,
            confidence=score.confidence,
            approved=True,
            reason="test",
        )


class StubRiskEvaluator:
    """
    Stub risk evaluator for tests.
    """

    def evaluate(
        self,
        decision: DecisionResult,
    ) -> RiskResult:

        return RiskResult(
            approved=True,
            risk_level=0.1,
            position_size=1.0,
            max_loss=10.0,
            reason="test",
        )


class StubExecutionEngine:
    """
    Stub execution engine for tests.
    """

    def execute(
        self,
        asset: str,
        timeframe: int,
        decision: DecisionResult,
        risk: RiskResult,
    ) -> ExecutionResult:

        return ExecutionResult(
            decision=decision,
            risk=risk,
            order=None,
            executed=True,
            message="test execution",
        )


def create_score() -> ScoreResult:

    return ScoreResult(
        score=90.0,
        confidence=0.9,
        strength=0.9,
        weight_sum=1.0,
        indicators=3,
    )


def create_engine() -> TradeEngine:

    return TradeEngine(
        decision=StubDecisionEngine(),
        risk=StubRiskEvaluator(),
        execution=StubExecutionEngine(),
    )


def test_trade_engine_process_returns_trade_result() -> None:

    engine = create_engine()

    result = engine.process(
        asset="BTCUSDT",
        timeframe=1,
        score=create_score(),
    )

    assert isinstance(
        result,
        TradeResult,
    )

    assert result.approved is True


def test_trade_engine_rejects_empty_asset() -> None:

    engine = create_engine()

    with pytest.raises(
        ValueError,
        match="asset cannot be empty",
    ):
        engine.process(
            asset="",
            timeframe=1,
            score=create_score(),
        )


def test_trade_engine_rejects_none_dependencies() -> None:

    with pytest.raises(
        TypeError,
        match="decision cannot be None",
    ):
        TradeEngine(
            decision=None,
            risk=StubRiskEvaluator(),
            execution=StubExecutionEngine(),
        )