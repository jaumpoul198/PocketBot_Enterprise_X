"""
PocketBot Enterprise X

Decision failure scenario tests.
"""

from unittest.mock import Mock

import pytest

from pocketbot.decision.engine import DecisionEngine
from pocketbot.decision.filters import DecisionFilters
from pocketbot.domain.enums import SignalType
from pocketbot.score.result import ScoreResult


def create_score() -> ScoreResult:
    return ScoreResult(
        score=90.0,
        confidence=0.90,
        strength=0.90,
        weight_sum=1.0,
        indicators=3,
    )


def test_decision_blocks_low_score() -> None:
    engine = DecisionEngine()

    score = ScoreResult(
        score=50.0,
        confidence=0.90,
        strength=0.90,
        weight_sum=1.0,
        indicators=3,
    )

    result = engine.decide(score)

    assert result.signal == SignalType.NEUTRAL
    assert result.approved is False


def test_decision_blocks_low_confidence() -> None:
    engine = DecisionEngine()

    score = ScoreResult(
        score=90.0,
        confidence=0.40,
        strength=0.90,
        weight_sum=1.0,
        indicators=3,
    )

    result = engine.decide(score)

    assert result.approved is False
    assert "Confidence" in result.reason


def test_decision_blocks_low_strength() -> None:
    engine = DecisionEngine()

    score = ScoreResult(
        score=90.0,
        confidence=0.90,
        strength=0.20,
        weight_sum=1.0,
        indicators=3,
    )

    result = engine.decide(score)

    assert result.approved is False
    assert "Strength" in result.reason


def test_decision_propagates_filter_failure() -> None:
    engine = DecisionEngine()

    engine._filters = Mock(
        spec=DecisionFilters,
    )

    engine._filters.score_ok.side_effect = RuntimeError(
        "filter unavailable",
    )

    with pytest.raises(
        RuntimeError,
        match="filter unavailable",
    ):
        engine.decide(
            create_score(),
        )


def test_decision_approves_valid_score_without_strategy() -> None:
    engine = DecisionEngine()

    result = engine.decide(
        create_score(),
    )

    assert result.approved is True
    assert result.signal == SignalType.BUY
