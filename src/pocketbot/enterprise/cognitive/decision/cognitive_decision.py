from .decision_models import CognitiveDecisionResult


class CognitiveDecision:

    def __init__(self):
        self.last_decision = None

    def decide(
        self,
        cognitive_state,
        memory_score: float = 1.0,
        learning_score: float = 1.0,
    ):

        confidence = (
            memory_score +
            learning_score
        ) / 2

        action = cognitive_state

        decision = CognitiveDecisionResult(
            action=action,
            confidence=confidence,
            reasoning=(
                "decision generated from "
                "cognitive state, memory and learning"
            ),
        )

        self.last_decision = decision

        return decision

    def status(self):

        return {
            "last_decision": self.last_decision
        }
