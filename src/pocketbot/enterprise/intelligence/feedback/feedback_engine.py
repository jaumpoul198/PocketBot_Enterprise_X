from __future__ import annotations

from datetime import datetime, timezone

from .feedback_models import DecisionFeedback
from .feedback_processor import FeedbackProcessor


class FeedbackEngine:
    """
    Enterprise decision feedback controller.
    """

    def __init__(
        self,
        processor: FeedbackProcessor | None = None,
    ) -> None:

        self.processor = (
            processor
            or FeedbackProcessor()
        )

        self._history: list[DecisionFeedback] = []

    def evaluate(
        self,
        decision: str,
        expected_score: float,
        actual_score: float,
        success: bool,
    ) -> DecisionFeedback:

        feedback = DecisionFeedback(
            decision=decision,
            expected_score=expected_score,
            actual_score=actual_score,
            success=success,
            timestamp=datetime.now(
                timezone.utc
            ),
        )

        self._history.append(feedback)

        return feedback

    def learning_signal(
        self,
        feedback: DecisionFeedback,
    ) -> float:

        return self.processor.process(
            feedback
        )

    def count(self) -> int:
        return len(self._history)
