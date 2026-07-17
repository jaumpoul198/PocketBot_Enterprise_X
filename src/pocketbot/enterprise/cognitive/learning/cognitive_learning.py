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

        self.experiences.append(experience)

        return experience

    def history(self):

        return self.experiences

    def score(self):

        if not self.experiences:
            return 0.0

        total = sum(
            experience.score
            for experience in self.experiences
        )

        return total / len(self.experiences)
