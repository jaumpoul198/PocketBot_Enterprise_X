from datetime import datetime, timezone
from typing import Dict, Any, List


class AutonomyFeedback:
    """
    Feedback Loop da autonomia cognitiva.

    Registra resultados das ações autônomas
    para evolução e aprendizado futuro.
    """

    def __init__(self):
        self.feedback_history: List[Dict[str, Any]] = []

    def register_feedback(
        self,
        action: Dict[str, Any],
        success: bool,
        reward: float
    ) -> Dict[str, Any]:

        feedback = {
            "action": action,
            "success": success,
            "reward": reward,
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.feedback_history.append(feedback)

        return feedback

    def success_rate(self):

        if not self.feedback_history:
            return 0

        successes = sum(
            1
            for item in self.feedback_history
            if item["success"]
        )

        return successes / len(
            self.feedback_history
        )

    def get_history(self):

        return self.feedback_history
