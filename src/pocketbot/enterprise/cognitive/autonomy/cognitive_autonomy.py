from datetime import datetime, timezone
from typing import Dict, Any


class CognitiveAutonomy:
    """
    Cognitive Autonomy Layer

    Responsável por:
    - avaliar capacidade de ação autônoma
    - controlar ciclos cognitivos
    - registrar estado de autonomia
    - preparar decisões independentes
    """

    def __init__(self):
        self.created_at = datetime.now(timezone.utc)
        self.state = "initialized"
        self.autonomy_score = 0.0
        self.cycles = 0

    def evaluate_autonomy(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Avalia se o sistema possui condições
        para executar ações autônomas.
        """

        confidence = context.get("confidence", 0)

        if confidence >= 0.8:
            status = "autonomous_ready"
            self.autonomy_score = confidence
        elif confidence >= 0.5:
            status = "assisted_autonomy"
            self.autonomy_score = confidence
        else:
            status = "dependent_mode"
            self.autonomy_score = confidence

        self.state = status

        return {
            "status": status,
            "autonomy_score": self.autonomy_score,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def execute_cycle(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa um ciclo autônomo baseado
        em uma decisão cognitiva.
        """

        self.cycles += 1

        return {
            "cycle": self.cycles,
            "decision": decision,
            "state": self.state,
            "executed": True,
        }

    def get_status(self) -> Dict[str, Any]:
        return {
            "state": self.state,
            "autonomy_score": self.autonomy_score,
            "cycles": self.cycles,
            "created_at": self.created_at.isoformat(),
        }
