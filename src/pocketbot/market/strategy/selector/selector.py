from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.ranking import StrategyRankingEngine


class StrategySelectorEngine:
    """
    Selects the best strategy based on ranking.
    """

    def __init__(
        self,
        ranking_engine: StrategyRankingEngine | None = None,
    ) -> None:
        self._ranking_engine = (
            ranking_engine
            if ranking_engine is not None
            else StrategyRankingEngine()
        )

    def select(
        self,
        scores: list[StrategyScore],
    ) -> StrategyScore:
        """
        Returns the highest ranked strategy.
        """

        ranked_scores = self._ranking_engine.rank(scores)

        return ranked_scores[0]
