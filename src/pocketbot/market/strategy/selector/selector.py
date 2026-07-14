from typing import Final

from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.ranking import StrategyRankingEngine


_UNSET: Final = object()


class StrategySelectorEngine:
    """
    Selects the best strategy based on ranking.
    """

    def __init__(
        self,
        ranking_engine: StrategyRankingEngine | object = _UNSET,
    ) -> None:

        if ranking_engine is _UNSET:
            self._ranking_engine = StrategyRankingEngine()
            return

        if ranking_engine is None:
            raise ValueError(
                "ranking_engine cannot be None",
            )

        if not hasattr(
            ranking_engine,
            "rank",
        ):
            raise TypeError(
                "ranking_engine must provide rank",
            )

        self._ranking_engine = ranking_engine

    def select(
        self,
        scores: list[StrategyScore],
    ) -> StrategyScore:

        if scores is None:
            raise ValueError(
                "scores cannot be None",
            )

        ranked_scores = self._ranking_engine.rank(
            scores,
        )

        return ranked_scores[0]