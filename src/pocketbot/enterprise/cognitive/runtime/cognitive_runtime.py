from datetime import datetime, UTC

from ..core.cognitive_engine import CognitiveEngine
from ..memory.cognitive_memory import CognitiveMemory
from ..learning.cognitive_learning import CognitiveLearning
from ...intelligence.runtime import IntelligenceRuntime


class CognitiveRuntime:

    def __init__(self):
        self.engine = CognitiveEngine()
        self.intelligence = IntelligenceRuntime()
        self.memory = CognitiveMemory()
        self.learning = CognitiveLearning()

        self.started_at = datetime.now(UTC)
        self.last_decision = None
        self.last_intelligence_decision = None
        self.last_memory_entry = None
        self.last_learning_experience = None

    def execute(self, health_score: float = 1.0):

        cognitive_decision = self.engine.process()

        intelligence_decision = self.intelligence.evaluate(
            health_score
        )

        memory_entry = self.memory.remember(
            cycle=cognitive_decision.action,
            action=cognitive_decision.action,
            confidence=cognitive_decision.confidence,
        )

        learning_experience = self.learning.learn(
            event=cognitive_decision.action,
            outcome=intelligence_decision.action,
            score=health_score,
        )

        self.last_decision = cognitive_decision
        self.last_intelligence_decision = intelligence_decision
        self.last_memory_entry = memory_entry
        self.last_learning_experience = learning_experience

        return cognitive_decision

    def status(self):

        return {
            "started_at": self.started_at,
            "last_decision": self.last_decision,
            "last_intelligence_decision": self.last_intelligence_decision,
            "last_memory_entry": self.last_memory_entry,
            "memory": self.memory.history(),
            "last_learning_experience": self.last_learning_experience,
            "learning_score": self.learning.score(),
            "engine": self.engine.status(),
            "intelligence": self.intelligence.status(),
        }
