from .reflection_memory import ReflectionMemory
from .reflection_analyzer import ReflectionAnalyzer
from .reflection_score import ReflectionScore


class SelfReflection:

    def __init__(self):

        self.memory = ReflectionMemory()

        self.analyzer = ReflectionAnalyzer()

        self.score = ReflectionScore()


    def reflect(
        self,
        decision_confidence,
        feedback,
    ):

        analysis = self.analyzer.analyze(
            feedback
        )

        result = self.score.calculate(
            decision_confidence,
            feedback.get(
                "score",
                0,
            ),
        )

        reflection = {
            "analysis": analysis,
            "score": result,
        }

        return self.memory.store(
            reflection
        )
