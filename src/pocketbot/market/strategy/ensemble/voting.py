from collections import Counter

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


class MajorityVotingEnsemble(BaseStrategyEnsemble):
    """
    Ensemble based on majority voting between strategies.
    """

    def evaluate(
        self,
        results: list[StrategyResult],
    ) -> EnsembleResult:

        if not results:
            return EnsembleResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                votes={},
                reason="No strategy results available",
            )

        votes = {
            result.reason: result.signal
            for result in results
        }

        signals = [
            result.signal
            for result in results
        ]

        counter = Counter(signals)

        signal, count = counter.most_common(1)[0]

        confidence = count / len(results)

        return EnsembleResult(
            signal=signal,
            confidence=confidence,
            votes=votes,
            reason="Majority vote selected signal",
        )
