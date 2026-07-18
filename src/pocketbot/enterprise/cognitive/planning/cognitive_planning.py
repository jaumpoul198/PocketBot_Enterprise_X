from datetime import UTC, datetime

from .planning_models import PlanningResult


class CognitivePlanning:

    def __init__(self):

        self.history = []


    def plan(
        self,
        learning_score: float,
        evolution_score: float,
    ) -> PlanningResult:

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

        return result


    def latest(self):

        if not self.history:
            return None

        return self.history[-1]


    def status(self):

        return {
            "plans": len(self.history),
            "latest": self.latest(),
        }
