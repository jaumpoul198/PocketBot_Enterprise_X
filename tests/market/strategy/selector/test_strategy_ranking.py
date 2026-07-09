from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.ranking import StrategyRankingEngine


def test_strategy_ranking_orders_by_win_rate():

    engine = StrategyRankingEngine()

    ranking = engine.rank(
        [
            StrategyScore(
                strategy_name="momentum",
                win_rate=0.75,
            ),
            StrategyScore(
                strategy_name="breakout",
                win_rate=0.65,
            ),
            StrategyScore(
                strategy_name="mean_reversion",
                win_rate=0.55,
            ),
        ]
    )

    assert ranking[0].strategy_name == "momentum"
    assert ranking[1].strategy_name == "breakout"
    assert ranking[2].strategy_name == "mean_reversion"


def test_strategy_ranking_empty():

    engine = StrategyRankingEngine()

    ranking = engine.rank([])

    assert ranking == []
