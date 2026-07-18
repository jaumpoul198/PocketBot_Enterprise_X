from datetime import UTC, datetime


class GoalFeedback:

    def __init__(self):

        self.history = []


    def record(
        self,
        goal,
        result: str,
        score: float = 1.0,
    ):

        feedback = {
            "goal": goal,
            "result": result,
            "score": score,
            "timestamp": datetime.now(UTC),
        }

        self.history.append(feedback)

        return feedback


    def latest(self):

        if not self.history:
            return None

        return self.history[-1]
