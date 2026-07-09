from abc import ABC, abstractmethod

from pocketbot.market.strategy.ensemble.models import EnsembleResult
from pocketbot.market.strategy.models import StrategyResult


class BaseStrategyEnsemble(ABC):
    """
    Base contract for strategy ensembles.
    """

    @abstractmethod
    def evaluate(
        self,
        results: list[StrategyResult],
    ) -> EnsembleResult:
        """
        Combine multiple strategy results.
        """
        pass
