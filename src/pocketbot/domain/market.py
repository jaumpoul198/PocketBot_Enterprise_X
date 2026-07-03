from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Market:
    """
    Representa o estado atual do mercado para um ativo.
    """

    symbol: str

    timeframe: str

    trend: str = "NEUTRAL"

    volatility: float = 0.0

    momentum: float = 0.0

    volume: float = 0.0

    spread: float = 0.0

    score: float = 0.0

    updated_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def bullish(self) -> bool:
        return self.trend.upper() == "BULLISH"

    @property
    def bearish(self) -> bool:
        return self.trend.upper() == "BEARISH"

    @property
    def neutral(self) -> bool:
        return self.trend.upper() == "NEUTRAL"

    @property
    def tradable(self) -> bool:
        return self.score >= 70.0
