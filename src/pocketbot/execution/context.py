"""
PocketBot Enterprise X

Execution Context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pocketbot.decision.result import DecisionResult
from pocketbot.domain.candle import Candle
from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.score.result import ScoreResult


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared context during a complete trading cycle.
    """

    asset: str

    timeframe: int

    candles: list[Candle]

    indicator_results: list[IndicatorResult] = field(default_factory=list)

    score: ScoreResult | None = None

    decision: DecisionResult | None = None

    metadata: dict[str, Any] = field(default_factory=dict)
