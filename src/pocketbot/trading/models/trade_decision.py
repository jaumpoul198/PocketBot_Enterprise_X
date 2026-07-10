"""
PocketBot Enterprise X

Trade Decision Model.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class TradeDecision:
    """
    Represents a generated trading decision.
    """

    asset: str

    decision: str

    strategy: str | None

    score: float

    timestamp: datetime
