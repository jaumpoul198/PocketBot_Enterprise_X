from datetime import datetime, UTC
from typing import Any, Dict, List


class AutonomyState:
    """
    Persistent state foundation for Cognitive Autonomy.

    Stores execution history,
    feedback records and evolution events.
    """

    def __init__(self):

        self.created_at = datetime.now(UTC)

        self.executions: List[Dict[str, Any]] = []

        self.feedback: List[Dict[str, Any]] = []

        self.evolution_events: List[Dict[str, Any]] = []


    def add_execution(
        self,
        execution: Dict[str, Any],
    ):

        self.executions.append(
            execution
        )


    def add_feedback(
        self,
        feedback: Dict[str, Any],
    ):

        self.feedback.append(
            feedback
        )


    def add_evolution_event(
        self,
        event: Dict[str, Any],
    ):

        self.evolution_events.append(
            event
        )


    def snapshot(self) -> Dict[str, Any]:

        return {
            "created_at": self.created_at.isoformat(),

            "executions": len(
                self.executions
            ),

            "feedback": len(
                self.feedback
            ),

            "evolution_events": len(
                self.evolution_events
            ),
        }
