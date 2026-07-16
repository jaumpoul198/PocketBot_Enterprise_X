from datetime import datetime, UTC

from .models import IntelligenceDecision
from .metrics import IntelligenceMetrics


class IntelligenceEngine:
    """
    Core Enterprise Intelligence decision engine.

    Evaluates operational health signals
    and produces autonomous recommendations.
    """

    def __init__(self):
        self.metrics = IntelligenceMetrics()

    def analyze(self, health_score: float) -> IntelligenceDecision:
        """
        Analyze system health and generate decision.
        """

        self.metrics.record(
            "health_score",
            health_score
        )

        if health_score >= 90:
            return IntelligenceDecision(
                action="maintain",
                confidence=0.95,
                reason="System operating normally",
                timestamp=datetime.now(UTC)
            )

        if health_score >= 70:
            return IntelligenceDecision(
                action="monitor",
                confidence=0.80,
                reason="Minor degradation detected",
                timestamp=datetime.now(UTC)
            )

        return IntelligenceDecision(
            action="intervene",
            confidence=0.90,
            reason="Operational risk detected",
            timestamp=datetime.now(UTC)
        )
