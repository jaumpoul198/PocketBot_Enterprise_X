from datetime import datetime, UTC

from .evolution_models import EvolutionMetric


class CognitiveEvolution:

    def __init__(self):
        self.metrics = []

    def evaluate(
        self,
        memory_count: int,
        learning_score: float,
    ):

        score = (
            (memory_count * 0.1)
            + (learning_score * 0.9)
        )

        if score >= 0.8:
            maturity = "ADVANCED"

        elif score >= 0.5:
            maturity = "INTERMEDIATE"

        else:
            maturity = "INITIAL"

        metric = EvolutionMetric(
            score=score,
            experiences=memory_count,
            maturity=maturity,
            timestamp=datetime.now(UTC),
        )

        self.metrics.append(metric)

        return metric

    def latest(self):

        if not self.metrics:
            return None

        return self.metrics[-1]
