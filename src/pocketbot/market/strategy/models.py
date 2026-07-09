from dataclasses import dataclass
from enum import Enum


class StrategySignal(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


@dataclass(frozen=True)
class StrategyResult:
    signal: StrategySignal
    confidence: float
    reason: str
