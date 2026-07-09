from pocketbot.market.strategy.ensemble.base import (
    BaseStrategyEnsemble,
)
from pocketbot.market.strategy.ensemble.models import (
    EnsembleResult,
)
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


class WeightedVotingEnsemble(BaseStrategyEnsemble):
    """
    Ensemble that combines strategy signals using confidence weights.
    """

    name = "weighted_voting"

    def evaluate(
        self,
        results: list[StrategyResult],
    ) -> EnsembleResult:

        if not results:
            return EnsembleResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                votes={},
                reason="no strategy results",
            )

        scores: dict[StrategySignal, float] = {
            StrategySignal.BUY: 0.0,
            StrategySignal.SELL: 0.0,
            StrategySignal.HOLD: 0.0,
        }

        votes: dict[str, StrategySignal] = {}

        for index, result in enumerate(results):
            strategy_name = f"strategy_{index + 1}"

            scores[result.signal] += result.confidence
            votes[strategy_name] = result.signal

        final_signal = StrategySignal.HOLD
        highest_score = 0.0

        for signal, score in scores.items():
            if score > highest_score:
                highest_score = score
                final_signal = signal

        total_score = sum(scores.values())

        confidence = (
            highest_score / total_score
            if total_score > 0
            else 0.0
        )

        return EnsembleResult(
            signal=final_signal,
            confidence=confidence,
            votes=votes,
            reason="weighted voting ensemble",
        )
