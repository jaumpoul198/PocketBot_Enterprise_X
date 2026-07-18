class ReflectionScore:

    def calculate(
        self,
        confidence: float,
        feedback_score: float,
    ):

        return {
            "confidence": confidence,
            "feedback_score": feedback_score,
            "reflection_score": (
                confidence + feedback_score
            ) / 2,
        }
