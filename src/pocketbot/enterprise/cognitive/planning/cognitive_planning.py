import time
from datetime import UTC, datetime

from ..observability import CognitiveMonitor
from .planning_models import PlanningResult


class CognitivePlanning:

    def __init__(
        self,
        observability: CognitiveMonitor | None = None,
    ):

        self.history = []
        self.observability = observability

    def plan(
        self,
        learning_score: float,
        evolution_score: float,
    ) -> PlanningResult:

        start_time = time.perf_counter()

        if self.observability:
            self.observability.emit_event(
                event_type="PLANNING_STARTED",
                source="planning",
            )

        priority = (
            learning_score * 0.7
            + evolution_score * 0.3
        )

        if priority >= 0.80:
            strategy = "EXPAND"

        elif priority >= 0.50:
            strategy = "OPTIMIZE"

        else:
            strategy = "LEARN"

        result = PlanningResult(
            objective="continuous_improvement",
            priority=priority,
            strategy=strategy,
            timestamp=datetime.now(UTC),
        )

        self.history.append(result)

        if self.observability:

            duration = time.perf_counter() - start_time

            self.observability.record_metric(
                name="planning_duration",
                value=duration,
                component="planning",
            )

            self.observability.record_metric(
                name="planning_priority",
                value=priority,
                component="planning",
            )

            self.observability.emit_event(
                event_type="PLANNING_COMPLETED",
                source="planning",
                payload={
                    "strategy": strategy,
                    "priority": priority,
                },
            )

        return result

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def status(self):

        return {
            "plans": len(self.history),
            "latest": self.latest(),
            "last_plan": self.latest(),
        }
