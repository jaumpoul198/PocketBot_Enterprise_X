from __future__ import annotations

from datetime import UTC, datetime

from .adaptive import AdaptiveEngine
from .feedback import FeedbackEngine
from .learning import LearningEngine
from .metrics import IntelligenceMetrics
from .models import IntelligenceDecision


class IntelligenceEngine:
    """
    Core Enterprise Intelligence decision engine.

    Coordinates adaptive intelligence,
    learning and feedback.
    """

    def __init__(self) -> None:

        self.metrics = IntelligenceMetrics()
        self.adaptive = AdaptiveEngine()
        self.feedback = FeedbackEngine()
        self.learning = LearningEngine()

    def analyze(
        self,
        health_score: float,
    ) -> IntelligenceDecision:

        self.metrics.record(
            "health_score",
            health_score,
        )

        adaptive = self.adaptive.evaluate(
            health_score,
        )

        if health_score >= 90:

            action = "maintain"
            confidence = 0.95
            reason = "System operating normally"

        elif health_score >= 70:

            action = "monitor"
            confidence = 0.80
            reason = "Minor degradation detected"

        else:

            action = "intervene"
            confidence = 0.90
            reason = "Operational risk detected"

        decision = IntelligenceDecision(
            action=action,
            confidence=confidence,
            reason=reason,
            timestamp=datetime.now(UTC),
        )

        feedback = self.feedback.evaluate(
            decision=action,
            expected_score=health_score,
            actual_score=health_score,
            success=health_score >= 70,
        )

        self.learning.learn(
            decision=action,
            score_before=health_score,
            score_after=health_score,
            feedback=self.feedback.learning_signal(
                feedback,
            ),
        )

        self.metrics.record(
            "adaptive_mode",
            adaptive.mode,
        )

        self.metrics.record(
            "learning_records",
            self.learning.state().total_records,
        )

        return decision
