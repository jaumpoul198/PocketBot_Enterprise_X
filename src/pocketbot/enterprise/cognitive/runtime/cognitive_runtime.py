from datetime import datetime, UTC

from ..core.cognitive_engine import CognitiveEngine
from ...intelligence.runtime import IntelligenceRuntime


class CognitiveRuntime:

    def __init__(self):
        self.engine = CognitiveEngine()
        self.intelligence = IntelligenceRuntime()

        self.started_at = datetime.now(UTC)
        self.last_decision = None
        self.last_intelligence_decision = None

    def execute(self, health_score: float = 1.0):

        cognitive_decision = self.engine.process()

        intelligence_decision = self.intelligence.evaluate(
            health_score
        )

        self.last_decision = cognitive_decision
        self.last_intelligence_decision = intelligence_decision

        return cognitive_decision

    def status(self):

        return {
            "started_at": self.started_at,
            "last_decision": self.last_decision,
            "last_intelligence_decision": self.last_intelligence_decision,
            "engine": self.engine.status(),
            "intelligence": self.intelligence.status(),
        }
