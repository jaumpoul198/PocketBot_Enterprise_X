from pocketbot.market.strategy.ensemble.weighted import (
    WeightedVotingEnsemble,
)
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


def test_weighted_voting_buy() -> None:
    ensemble = WeightedVotingEnsemble()

    results = [
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=0.9,
            reason="trend",
        ),
        StrategyResult(
            signal=StrategySignal.BUY,
            confidence=0.8,
            reason="momentum",
        ),
        StrategyResult(
            signal=StrategySignal.SELL,
            confidence=0.4,
            reason="mean",
        ),
    ]

    result = ensemble.evaluate(results)

    assert result.signal == StrategySignal.BUY


def test_weighted_voting_empty() -> None:
    ensemble = WeightedVotingEnsemble()

    result = ensemble.evaluate([])

    assert result.signal == StrategySignal.HOLD
