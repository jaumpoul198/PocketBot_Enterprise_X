from pocketbot.market.strategy.performance.models import (
    StrategyPerformance,
)


def test_strategy_performance_accuracy() -> None:
    performance = StrategyPerformance(
        strategy_name="momentum",
        total_signals=100,
        successful_signals=75,
        failed_signals=25,
    )

    assert performance.accuracy == 0.75


def test_strategy_performance_empty() -> None:
    performance = StrategyPerformance(
        strategy_name="momentum",
        total_signals=0,
        successful_signals=0,
        failed_signals=0,
    )

    assert performance.accuracy == 0.0
