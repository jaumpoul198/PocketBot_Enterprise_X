from dataclasses import dataclass

from pocketbot.market.strategy.models import StrategySignal


@dataclass(frozen=True)
class EnsembleResult:
    """
    Result produced by a strategy ensemble.
    """

    signal: StrategySignal
    confidence: float
    votes: dict[str, StrategySignal]
    reason: str
