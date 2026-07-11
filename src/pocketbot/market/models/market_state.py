
"""
PocketBot Enterprise X

Market State Model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MarketState:
    """
    Represents the current market condition.
    """

    asset: str

    timeframe: int

    trend: str

    volatility: float

    momentum: float

    last_price: float
