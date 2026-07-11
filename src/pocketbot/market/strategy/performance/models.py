from dataclasses import dataclass


@dataclass(frozen=True)
class StrategyPerformance:
    """
    Stores performance metrics of a strategy.
    """

    strategy_name: str
    total_signals: int
    successful_signals: int
    failed_signals: int

    @property
    def accuracy(self) -> float:
        """
        Calculates strategy accuracy.
        """

        if self.total_signals == 0:
            return 0.0

        return self.successful_signals / self.total_signals

    @property
    def win_rate(self) -> float:
        """
        Alias for accuracy.
        """

        return self.accuracy
