from datetime import datetime, UTC

from ..models.cognitive_models import CognitiveStateModel


class CognitiveState:

    def __init__(self):
        self.current = CognitiveStateModel(
            state="IDLE",
            confidence=0.0,
            timestamp=datetime.now(UTC),
        )

    def update(
        self,
        state: str,
        confidence: float,
    ):
        self.current = CognitiveStateModel(
            state=state,
            confidence=confidence,
            timestamp=datetime.now(UTC),
        )

        return self.current

    def snapshot(self):
        return self.current
