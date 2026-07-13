from dataclasses import FrozenInstanceError

import pytest

from pocketbot.market.strategy.performance.evaluator import (
    StrategyEvaluator,
)
from pocketbot.market.strategy.performance.models import (
    StrategyPerformance,
)


def test_evaluator_handles_empty_predictions() -> None:
    evaluator = StrategyEvaluator()

    result = evaluator.evaluate(
        strategy_name="momentum",
        predictions=[],
        outcomes=[True, False],
    )

    assert result.total_signals == 0
    assert result.successful_signals == 0
    assert result.failed_signals == 0


def test_evaluator_handles_empty_outcomes() -> None:
    evaluator = StrategyEvaluator()

    result = evaluator.evaluate(
        strategy_name="momentum",
        predictions=[True, False],
        outcomes=[],
    )

    assert result.total_signals == 0
    assert result.successful_signals == 0
    assert result.failed_signals == 0


def test_evaluator_uses_shortest_collection_when_sizes_differ() -> None:
    evaluator = StrategyEvaluator()

    result = evaluator.evaluate(
        strategy_name="momentum",
        predictions=[
            True,
            False,
            True,
        ],
        outcomes=[
            True,
            False,
        ],
    )

    assert result.total_signals == 2
    assert result.successful_signals == 2
    assert result.failed_signals == 0


def test_performance_model_is_immutable() -> None:
    performance = StrategyPerformance(
        strategy_name="momentum",
        total_signals=10,
        successful_signals=8,
        failed_signals=2,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        performance.total_signals = 20
