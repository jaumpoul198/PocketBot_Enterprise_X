from pocketbot.market.strategy.ensemble.voting import (
    MajorityVotingEnsemble,
)
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


def test_majority_voting_buy() -> None:
    ensemble = MajorityVotingEnsemble()

    result = ensemble.evaluate(
        [
            StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.8,
                reason="trend",
            ),
            StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.7,
                reason="momentum",
            ),
            StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.5,
                reason="mean",
            ),
        ]
    )

    assert result.signal == StrategySignal.BUY
    assert result.confidence == 2 / 3


def test_majority_voting_empty() -> None:
    ensemble = MajorityVotingEnsemble()

    result = ensemble.evaluate([])

    assert result.signal == StrategySignal.HOLD
    assert result.confidence == 0.0
