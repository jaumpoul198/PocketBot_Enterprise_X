from pocketbot.market.strategy.selector.models import (
    StrategyScore,
    StrategyRanking,
)


def test_strategy_score_creation():

    score = StrategyScore(
        strategy_name="momentum",
        win_rate=0.75,
    )

    assert score.strategy_name == "momentum"
    assert score.win_rate == 0.75


def test_strategy_ranking_creation():

    ranking = StrategyRanking(
        scores=[
            StrategyScore(
                strategy_name="momentum",
                win_rate=0.75,
            )
        ]
    )

    assert len(ranking.scores) == 1
