from datetime import datetime, timezone
from typing import Dict, Any, List


class AutonomyEvolutionBridge:
    """
    Ponte entre Autonomy Layer
    e Cognitive Evolution Layer.

    Transforma feedbacks de execução
    em sinais de evolução cognitiva.
    """

    def __init__(self):
        self.evolution_events: List[Dict[str, Any]] = []

    def process_feedback(
        self,
        feedback: Dict[str, Any]
    ) -> Dict[str, Any]:

        reward = feedback.get(
            "reward",
            0
        )

        if reward >= 0.8:
            signal = "reinforce"
        elif reward >= 0.4:
            signal = "adjust"
        else:
            signal = "discard"

        event = {
            "signal": signal,
            "reward": reward,
            "source": "autonomy",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.evolution_events.append(event)

        return event

    def get_events(self):

        return self.evolution_events
