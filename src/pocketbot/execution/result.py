"""
PocketBot Enterprise X

Execution Result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from pocketbot.decision.result import DecisionResult
from pocketbot.execution.order import ExecutionOrder
from pocketbot.risk.result import RiskResult


@dataclass(frozen=True, slots=True)
class ExecutionResult:
    """
    Final result of a trading cycle.
    """

    decision: DecisionResult

    risk: RiskResult

    order: ExecutionOrder | None

    executed: bool

    message: str

    metadata: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
