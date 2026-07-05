"""
PocketBot Enterprise X

Signal domain enumeration.
"""

from __future__ import annotations

from enum import Enum


class SignalType(str, Enum):
    """
    Represents the direction suggested by an indicator
    or by the decision engine.
    """

    BUY = "BUY"
    SELL = "SELL"
    NEUTRAL = "NEUTRAL"
    WAIT = "WAIT"
