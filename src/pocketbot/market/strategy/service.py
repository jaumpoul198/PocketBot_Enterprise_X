from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import StrategyResult


class StrategyService:

    def __init__(self, strategies: list[BaseStrategy]):
        self._strategies = strategies


    def analyze(self, market_data: object) -> list[StrategyResult]:
        return [
            strategy.analyze(market_data)
            for strategy in self._strategies
        ]
