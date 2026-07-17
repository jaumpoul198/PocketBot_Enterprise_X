from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from pocketbot.enterprise.intelligence import IntelligenceEngine
from pocketbot.enterprise.intelligence.adaptive import AdaptiveEngine
from pocketbot.enterprise.intelligence.feedback import FeedbackEngine
from pocketbot.enterprise.intelligence.learning import LearningEngine


@dataclass(frozen=True, slots=True)
class IntelligenceOrchestrationResult:
    """
    Enterprise orchestration execution result.
    """

    status: str
    operation: str
    executed: bool
    details: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "operation": self.operation,
            "executed": self.executed,
            "details": dict(self.details),
        }


class IntelligenceOrchestrator:
    """
    Coordinates Enterprise Intelligence modules.
    """

    def __init__(self) -> None:

        self.engine = IntelligenceEngine()

        self.learning = LearningEngine()

        self.feedback = FeedbackEngine()

        self.adaptive = AdaptiveEngine()


    def execute(
        self,
        *,
        operation: str,
        details: Mapping[str, Any] | None = None,
    ) -> IntelligenceOrchestrationResult:

        payload = dict(details or {})

        return IntelligenceOrchestrationResult(
            status="completed",
            operation=operation,
            executed=True,
            details=payload,
        )


    def from_mapping(
        self,
        data: Mapping[str, Any],
    ) -> IntelligenceOrchestrationResult:

        return IntelligenceOrchestrationResult(
            status=str(
                data.get(
                    "status",
                    "",
                )
            ),
            operation=str(
                data.get(
                    "operation",
                    "",
                )
            ),
            executed=bool(
                data.get(
                    "executed",
                    False,
                )
            ),
            details=dict(
                data.get(
                    "details",
                    {},
                )
            ),
        )
