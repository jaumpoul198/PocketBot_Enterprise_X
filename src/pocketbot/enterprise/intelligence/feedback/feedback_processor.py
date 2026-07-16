from __future__ import annotations

from .feedback_models import DecisionFeedback


class FeedbackProcessor:
    """
    Converts feedback results into learning signals.
    """

    def process(
        self,
        feedback: DecisionFeedback,
    ) -> float:

        if feedback.success:
            return min(
                1.0,
                feedback.accuracy + 0.2,
            )

        return max(
            0.0,
            feedback.accuracy - 0.2,
        )
