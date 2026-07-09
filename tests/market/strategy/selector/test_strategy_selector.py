from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.selector import StrategySelectorEngine


def test_selector_returns_best_strategy():
    scores = [
        StrategyScore(
            strategy_name="momentum",
            win_rate=0.60,
        ),
        StrategyScore(
            strategy_name="breakout",
            win_rate=0.80,
        ),
        StrategyScore(
            strategy_name="mean_reversion",
            win_rate=0.70,
        ),
    ]

    selector = StrategySelectorEngine()

    result = selector.select(scores)

    assert result.strategy_name == "breakout"
    assert result.win_rate == 0.80
