from dataclasses import dataclass


@dataclass(frozen=True)
class StrategyScore:
    """
    Represents the performance score of a strategy.
    """

    strategy_name: str
    win_rate: float


@dataclass(frozen=True)
class StrategyRanking:
    """
    Represents a ranking of strategies.
    """

    scores: list[StrategyScore]
