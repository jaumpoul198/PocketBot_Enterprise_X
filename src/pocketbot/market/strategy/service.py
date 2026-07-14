from __future__ import annotations

from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import StrategyResult
from pocketbot.market.strategy.selector.models import StrategyScore
from pocketbot.market.strategy.selector.selector import (
    StrategySelectorEngine,
)


class StrategyService:
    """
    Service responsible for executing and selecting strategies.
    """

    def __init__(
        self,
        strategies: list[BaseStrategy],
        selector: StrategySelectorEngine | None = None,
    ) -> None:

        if strategies is None:
            raise ValueError(
                "strategies cannot be None",
            )

        if selector is not None and not hasattr(
            selector,
            "select",
        ):
            raise TypeError(
                "selector must provide select",
            )

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
            strategy.analyze(
                market_data,
            )
            for strategy in self._strategies
        ]

    def select_best_strategy(
        self,
        scores: list[StrategyScore],
    ) -> StrategyScore:

        return self._selector.select(
            scores,
        )