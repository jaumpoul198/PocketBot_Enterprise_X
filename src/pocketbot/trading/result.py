"""
PocketBot Enterprise X

Trade Result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from pocketbot.decision.result import DecisionResult
from pocketbot.execution.result import ExecutionResult
from pocketbot.risk.result import RiskResult
from pocketbot.score.result import ScoreResult


@dataclass(frozen=True, slots=True)
class TradeResult:
    """
    Complete result of one trading cycle.
    """

    score: ScoreResult

    decision: DecisionResult

    risk: RiskResult

    execution: ExecutionResult

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    @property
    def approved(self) -> bool:
        return self.execution.executed