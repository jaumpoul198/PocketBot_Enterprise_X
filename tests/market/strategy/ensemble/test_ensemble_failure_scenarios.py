from dataclasses import FrozenInstanceError

import pytest

from pocketbot.market.strategy.ensemble.models import (
    EnsembleResult,
)
from pocketbot.market.strategy.ensemble.voting import (
    MajorityVotingEnsemble,
)
from pocketbot.market.strategy.ensemble.weighted import (
    WeightedVotingEnsemble,
)
from pocketbot.market.strategy.models import (
    StrategySignal,
)


def test_majority_voting_handles_none_result_failure() -> None:
    ensemble = MajorityVotingEnsemble()

    with pytest.raises(
        AttributeError,
    ):
        ensemble.evaluate(
            [None],
        )


def test_weighted_voting_handles_none_result_failure() -> None:
    ensemble = WeightedVotingEnsemble()

    with pytest.raises(
        AttributeError,
    ):
        ensemble.evaluate(
            [None],
        )


def test_weighted_voting_handles_zero_confidence_results() -> None:
    ensemble = WeightedVotingEnsemble()

    result = ensemble.evaluate(
        [
            type(
                "Result",
                (),
                {
                    "signal": StrategySignal.BUY,
                    "confidence": 0.0,
                },
            )(),
        ],
    )

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0


def test_ensemble_result_is_immutable() -> None:
    result = EnsembleResult(
        signal=StrategySignal.BUY,
        confidence=0.8,
        votes={},
        reason="test",
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        result.confidence = 0.5
