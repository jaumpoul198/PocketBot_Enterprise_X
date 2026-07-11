from dataclasses import dataclass

from pocketbot.market.strategy.performance.models import (
    StrategyPerformance,
)


@dataclass
class StrategyEvaluator:
    """
    Evaluates strategy performance metrics.
    """

    def evaluate(
        self,
        strategy_name: str,
        predictions: list[bool],
        outcomes: list[bool],
    ) -> StrategyPerformance:
        """
        Calculate strategy performance.
        """

        if not predictions or not outcomes:
            return StrategyPerformance(
                strategy_name=strategy_name,
                total_signals=0,
                successful_signals=0,
                failed_signals=0,
            )

        total = min(len(predictions), len(outcomes))

        successful = sum(
            1
            for index in range(total)
            if predictions[index] == outcomes[index]
        )

        failed = total - successful

        return StrategyPerformance(
            strategy_name=strategy_name,
            total_signals=total,
            successful_signals=successful,
            failed_signals=failed,
        )
