"""
PocketBot Enterprise X

Execution failure scenario tests.
"""

import pytest

from pocketbot.decision.result import DecisionResult
from pocketbot.domain.enums import SignalType
from pocketbot.execution.engine import ExecutionEngine
from pocketbot.risk.result import RiskResult


def create_decision(
    approved: bool = True,
) -> DecisionResult:
    return DecisionResult(
        signal=SignalType.BUY,
        score=90.0,
        confidence=0.90,
        approved=approved,
        reason="test",
    )


def create_risk(
    approved: bool = True,
) -> RiskResult:
    return RiskResult(
        approved=approved,
        risk_level=0.10,
        position_size=100.0,
        max_loss=10.0,
        reason="test",
    )


def test_execution_rejects_unapproved_decision() -> None:
    engine = ExecutionEngine()

    result = engine.execute(
        "BTCUSDT",
        60,
        create_decision(False),
        create_risk(),
    )

    assert result.executed is False
    assert result.order is None
    assert result.message == "Decision rejected."


def test_execution_rejects_failed_risk() -> None:
    engine = ExecutionEngine()

    result = engine.execute(
        "BTCUSDT",
        60,
        create_decision(),
        create_risk(False),
    )

    assert result.executed is False
    assert result.order is None
    assert result.message == "Risk rejected."


def test_execution_creates_order_when_approved() -> None:
    engine = ExecutionEngine()

    result = engine.execute(
        "BTCUSDT",
        60,
        create_decision(),
        create_risk(),
    )

    assert result.executed is True
    assert result.order is not None
    assert result.order.asset == "BTCUSDT"


def test_execution_rejects_none_risk() -> None:
    engine = ExecutionEngine()

    with pytest.raises(TypeError):
        engine.execute(
            "BTCUSDT",
            60,
            create_decision(),
            None,  # type: ignore[arg-type]
        )