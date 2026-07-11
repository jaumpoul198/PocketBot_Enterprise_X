from pocketbot.market.strategy.selector.models import StrategyScore


class StrategyRankingEngine:
    """
    Ranks strategies based on performance score.
    """

    def rank(
        self,
        scores: list[StrategyScore],
    ) -> list[StrategyScore]:
        """
        Returns strategies ordered by highest win rate.
        """

        return sorted(
            scores,
            key=lambda score: score.win_rate,
            reverse=True,
        )
