from datetime import UTC, datetime

from .learning_models import LearningExperience


class CognitiveLearning:

    def __init__(self):

        self.experiences = []

        self.feedback_history = []

    def learn(
        self,
        event: str,
        outcome: str,
        score: float,
    ):

        experience = LearningExperience(
            event=event,
            outcome=outcome,
            score=score,
            timestamp=datetime.now(UTC),
        )

        self.experiences.append(
            experience
        )

        return experience

    def update(
        self,
        reflection,
    ):

        self.feedback_history.append(
            reflection
        )

        return reflection

    def feedback(self):

        return self.feedback_history

    def history(self):

        return self.experiences

    def score(self):

        if not self.experiences:
            return 0.0

        total = sum(
            experience.score
            for experience in self.experiences
        )

        return total / len(
            self.experiences
        )

    def feedback_score(self):

        if not self.feedback_history:
            return 0.0

        values = []

        for reflection in self.feedback_history:

            score = reflection.get(
                "score",
                0.0,
            )

            if isinstance(
                score,
                (int, float),
            ):
                values.append(
                    float(score)
                )

        if not values:
            return 0.0

        return sum(values) / len(values)
