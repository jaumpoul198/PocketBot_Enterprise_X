from datetime import datetime, timezone
from typing import Dict, Any


class AutonomousExecutor:
    """
    Executor responsável por transformar
    decisões cognitivas em ações autônomas.
    """

    def __init__(self):
        self.executions = []

    def execute(
        self,
        decision: Dict[str, Any]
    ) -> Dict[str, Any]:

        confidence = decision.get(
            "confidence",
            0
        )

        approved = confidence >= 0.8

        result = {
            "approved": approved,
            "action": decision.get(
                "action"
            ),
            "confidence": confidence,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.executions.append(result)

        return result

    def get_execution_count(self):

        return len(self.executions)
