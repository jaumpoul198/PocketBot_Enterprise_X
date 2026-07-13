"""
PocketBot Enterprise X

Risk engine failure scenario tests.
"""

from __future__ import annotations

import pytest

from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.risk.engine import RiskEngine
from pocketbot.risk.result import RiskResult


class FailingRiskService:
    def evaluate(
        self,
        position_size: float,
        current_exposure: float,
    ):
        raise RuntimeError("risk service failure")


class ApprovedRiskService:
    def evaluate(
        self,
        position_size: float,
        current_exposure: float,
    ):
        return RiskResult(
            approved=True,
            risk_level=0.20,
            position_size=1.0,
            max_loss=1.0,
            reason="approved",
        )


def create_approved_decision() -> DecisionResult:
    return DecisionResult(
        signal=SignalType.BUY,
        score=90.0,
        confidence=0.90,
        approved=True,
        reason="approved",
    )


def create_rejected_decision() -> DecisionResult:
    return DecisionResult(
        signal=SignalType.NEUTRAL,
        score=50.0,
        confidence=0.40,
        approved=False,
        reason="rejected",
    )


def test_rejected_decision_blocks_risk_evaluation() -> None:
    engine = RiskEngine()

    result = engine.evaluate(
        create_rejected_decision(),
    )

    assert result.approved is False
    assert result.position_size == 0.0


def test_approved_decision_returns_approved_risk() -> None:
    engine = RiskEngine(
        risk_service=ApprovedRiskService(),
    )

    result = engine.evaluate(
        create_approved_decision(),
    )

    assert result.approved is True
    assert result.position_size == 1.0


def test_risk_service_failure_is_propagated() -> None:
    engine = RiskEngine(
        risk_service=FailingRiskService(),
    )

    with pytest.raises(
        RuntimeError,
        match="risk service failure",
    ):
        engine.evaluate(
            create_approved_decision(),
        )
