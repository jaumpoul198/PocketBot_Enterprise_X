from pocketbot.market.strategy.performance.evaluator import (
    StrategyEvaluator,
)


def test_strategy_evaluator_accuracy():

    evaluator = StrategyEvaluator()

    result = evaluator.evaluate(
        strategy_name="momentum",
        predictions=[True, True, False, True],
        outcomes=[True, False, False, True],
    )

    assert result.strategy_name == "momentum"
    assert result.total_signals == 4
    assert result.successful_signals == 3
    assert result.failed_signals == 1
    assert result.accuracy == 0.75


def test_strategy_evaluator_empty():

    evaluator = StrategyEvaluator()

    result = evaluator.evaluate(
        strategy_name="momentum",
        predictions=[],
        outcomes=[],
    )

    assert result.total_signals == 0
    assert result.accuracy == 0.0
