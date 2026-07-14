from pocketbot.market.strategy.selector.models import StrategyScore


class StrategyRankingEngine:
    """
    Ranks strategies based on performance score.
    """

    def rank(
        self,
        scores: list[StrategyScore],
    ) -> list[StrategyScore]:

        if scores is None:
            raise ValueError(
                "scores cannot be None",
            )

        return sorted(
            scores,
            key=lambda score: score.win_rate,
            reverse=True,
        )