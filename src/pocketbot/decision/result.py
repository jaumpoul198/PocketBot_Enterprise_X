"""
PocketBot Enterprise X

Decision result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pocketbot.domain.enums import SignalType


@dataclass(slots=True, frozen=True)
class DecisionResult:
    """
    Represents the final trading decision produced by
    the Decision Engine.
    """

    signal: SignalType

    score: float

    confidence: float

    approved: bool

    reason: str

    metadata: dict[str, Any] = field(default_factory=dict)
