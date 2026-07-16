from datetime import datetime, UTC

from .intelligence_engine import IntelligenceEngine


class IntelligenceRuntime:
    """
    Enterprise Intelligence runtime controller.

    Bridges production runtime signals
    with autonomous intelligence decisions.
    """

    def __init__(self):
        self.engine = IntelligenceEngine()
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

        return decision

    def status(self):
        """
        Return runtime intelligence status.
        """

        return {
            "started_at": self.started_at,
            "last_decision": self.last_decision,
            "metrics": self.engine.metrics.latest()
        }
