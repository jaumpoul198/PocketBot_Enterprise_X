import time

from ..observability import CognitiveMonitor
from .decision_models import CognitiveDecisionResult


class CognitiveDecision:

    def __init__(
        self,
        observability: CognitiveMonitor | None = None,
    ):
        self.last_decision = None
        self.observability = observability

    def decide(
        self,
        cognitive_state,
        memory_score: float = 1.0,
        learning_score: float = 1.0,
    ):

        start_time = time.perf_counter()

        if self.observability:
            self.observability.emit_event(
                event_type="DECISION_STARTED",
                source="decision",
            )

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

        if self.observability:

            duration = time.perf_counter() - start_time

            self.observability.record_metric(
                name="decision_duration",
                value=duration,
                component="decision",
            )

            self.observability.record_metric(
                name="decision_confidence",
                value=confidence,
                component="decision",
            )

            self.observability.emit_event(
                event_type="DECISION_COMPLETED",
                source="decision",
                payload={
                    "confidence": confidence,
                },
            )

        return decision

    def status(self):

        return {
            "last_decision": self.last_decision
        }
