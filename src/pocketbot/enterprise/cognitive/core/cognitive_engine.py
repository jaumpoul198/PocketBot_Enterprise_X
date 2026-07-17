from datetime import datetime, UTC

from ..models.cognitive_models import CognitiveDecision
from .cognitive_cycle import CognitiveCycle
from .cognitive_state import CognitiveState


class CognitiveEngine:

    def __init__(self):
        self.state = CognitiveState()
        self.cycle = CognitiveCycle()

    def process(self):

        current_cycle = self.cycle.next()

        self.state.update(
            state=current_cycle,
            confidence=1.0,
        )

        return CognitiveDecision(
            action=current_cycle,
            confidence=1.0,
            reasoning="cognitive foundation cycle execution",
            timestamp=datetime.now(UTC),
        )

    def status(self):
        return {
            "state": self.state.snapshot(),
            "cycle": self.cycle.position,
        }
