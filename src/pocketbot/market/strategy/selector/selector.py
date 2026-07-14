from typing import Protocol

from pocketbot.market.strategy.selector.models import (
    StrategyScore,
)
from pocketbot.market.strategy.selector.ranking import (
    StrategyRankingEngine,
)


class RankingEngineProtocol(Protocol):
    """
    Contract required by strategy selector ranking engine.
    """

    def rank(
        self,
        scores: list[StrategyScore],
    ) -> list[StrategyScore]:
        ...


class StrategySelectorEngine:
    """
    Selects the best strategy based on ranking.
    """

    def __init__(
        self,
        ranking_engine: RankingEngineProtocol | None = None,
    ) -> None:

        if ranking_engine is None:
            self._ranking_engine: RankingEngineProtocol = (
                StrategyRankingEngine()
            )
        else:
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
        scores: list[StrategyScore] | None,
    ) -> StrategyScore:

        if scores is None:
            raise ValueError(
                "scores cannot be None",
            )

        ranked_scores = self._ranking_engine.rank(
            scores,
        )

        return ranked_scores[0]