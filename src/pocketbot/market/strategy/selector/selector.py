from typing import Final, Protocol

from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.ranking import StrategyRankingEngine


_UNSET: Final = object()


class RankingEngineProtocol(Protocol):
    """
    Contract required by strategy ranking engine.
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
        ranking_engine: RankingEngineProtocol | object = _UNSET,
    ) -> None:

        if ranking_engine is _UNSET:
            self._ranking_engine: RankingEngineProtocol = (
                StrategyRankingEngine()
            )
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

        self._ranking_engine = ranking_engine  # type: ignore[assignment]

    def select(
        self,
        scores: list[StrategyScore],
    ) -> StrategyScore:
        """
        Returns the highest ranked strategy.
        """

        if scores is None:
            raise ValueError(
                "scores cannot be None",
            )

        ranked_scores = self._ranking_engine.rank(
            scores,
        )

        return ranked_scores[0]