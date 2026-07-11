"""
PocketBot Enterprise X
Market Snapshot
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from pocketbot.domain.candle import Candle


@dataclass(slots=True)
class MarketSnapshot:
    """
    Representa um snapshot completo do mercado.
    """

    asset: str

    timeframe: int

    candles: list[Candle] = field(default_factory=list)

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    provider: str = ""

    connected: bool = False

    latency_ms: float = 0.0

    spread: float = 0.0

    volume: float = 0.0

    def is_empty(self) -> bool:
        return len(self.candles) == 0

    @property
    def last_candle(self) -> Candle | None:
        if self.is_empty():
            return None
        return self.candles[-1]
