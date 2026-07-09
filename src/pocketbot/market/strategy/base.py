from abc import ABC, abstractmethod

from pocketbot.market.strategy.models import StrategyResult


class BaseStrategy(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Strategy identifier.
        """
        ...


    @abstractmethod
    def analyze(self, market_data) -> StrategyResult:
        """
        Analyze market data and generate a strategy result.
        """
        ...
