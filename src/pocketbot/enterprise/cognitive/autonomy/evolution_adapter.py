from typing import Dict, Any

from pocketbot.enterprise.cognitive.evolution import CognitiveEvolution


class EvolutionAdapter:
    """
    Adapter entre Autonomy Layer
    e Cognitive Evolution Layer.

    Converte experiências autônomas
    em métricas evolutivas.
    """

    def __init__(self):
        self.evolution = CognitiveEvolution()

    def process_event(
        self,
        event: Dict[str, Any]
    ):

        reward = event.get(
            "reward",
            0
        )

        signal = event.get(
            "signal"
        )

        learning_score = reward

        memory_count = 1

        metric = self.evolution.evaluate(
            memory_count=memory_count,
            learning_score=learning_score,
        )

        return {
            "signal": signal,
            "metric": metric,
        }

    def latest(self):

        return self.evolution.latest()
