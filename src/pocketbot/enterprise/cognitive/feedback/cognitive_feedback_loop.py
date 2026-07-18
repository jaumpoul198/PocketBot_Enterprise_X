from .feedback_models import CognitiveFeedback


class CognitiveFeedbackLoop:

    def __init__(self):

        self.history = []

    def evaluate(
        self,
        decision: str,
        outcome: str,
        score: float,
    ):

        feedback = CognitiveFeedback(
            decision=decision,
            outcome=outcome,
            score=score,
        )

        self.history.append(
            feedback
        )

        return feedback

    def all(self):

        return self.history

    def score(self):

        if not self.history:
            return 0.0

        total = sum(
            item.score
            for item in self.history
        )

        return total / len(
            self.history
        )
