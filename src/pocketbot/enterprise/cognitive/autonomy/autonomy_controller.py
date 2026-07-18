from datetime import datetime, timezone
from typing import Dict, Any, List


class AutonomyController:
    """
    Enterprise Cognitive Autonomy Controller

    Responsável pelo gerenciamento dos ciclos
    de autonomia cognitiva.
    """

    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        self.active = False
        self.cycles = 0

    def start(self):
        self.active = True

        return {
            "status": "started",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def stop(self):
        self.active = False

        return {
            "status": "stopped",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def process_action(
        self,
        action: Dict[str, Any],
        confidence: float
    ) -> Dict[str, Any]:

        self.cycles += 1

        decision = {
            "cycle": self.cycles,
            "action": action,
            "confidence": confidence,
            "autonomous": confidence >= 0.8,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        self.history.append(decision)

        return decision

    def get_history(self):
        return self.history

    def get_metrics(self):

        return {
            "cycles": self.cycles,
            "actions": len(self.history),
            "active": self.active
        }
