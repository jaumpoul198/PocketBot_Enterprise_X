from datetime import datetime, UTC

from .learning_models import LearningExperience


class CognitiveLearning:

    def __init__(self):
        self.experiences = []

    def learn(
        self,
        event: str,
        outcome: str,
        score: float
    ):

        experience = LearningExperience(
            event=event,
            outcome=outcome,
            score=score,
            timestamp=datetime.now(UTC),
        )
