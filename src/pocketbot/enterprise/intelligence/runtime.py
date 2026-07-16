from datetime import datetime, UTC

from .history import IntelligenceHistory
from .intelligence_engine import IntelligenceEngine


class IntelligenceRuntime:
    """
    Enterprise Intelligence runtime controller.

    Connects operational signals,
    intelligence decisions and decision history.
    """

    def __init__(self):
        self.engine = IntelligenceEngine()
        self.history = IntelligenceHistory()
        self.last_decision = None
        self.started_at = datetime.now(UTC)

    def evaluate(self, health_score: float):
        """
        Evaluate current operational health.
        """

        decision = self.engine.analyze(
            health_score
        )

        self.last_decision = decision

        self.history.record(
            decision=decision.action,
            confidence=decision.confidence,
            health_score=health_score,
        )

        return decision

    def status(self):
        """
        Return intelligence runtime status.
        """

        return {
            "started_at": self.started_at,
            "last_decision": self.last_decision,
            "metrics": self.engine.metrics.latest(),
            "decision_history": self.history.latest(),
            "autonomy_score": self.history.autonomy_score(),
        }
