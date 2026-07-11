from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import StrategyResult
from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.selector import StrategySelectorEngine


class StrategyService:

    def __init__(
        self,
        strategies: list[BaseStrategy],
        selector: StrategySelectorEngine | None = None,
    ):
        self._strategies = strategies
        self._selector = (
            selector
            if selector is not None
            else StrategySelectorEngine()
        )

    def analyze(
        self,
        market_data: object,
    ) -> list[StrategyResult]:
        return [
            strategy.analyze(market_data)
            for strategy in self._strategies
        ]

    def select_best_strategy(
        self,
        scores: list[StrategyScore],
    ) -> StrategyScore:
        return self._selector.select(scores)
