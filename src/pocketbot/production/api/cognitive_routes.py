from __future__ import annotations

from pocketbot.enterprise.cognitive.runtime.cognitive_runtime import (
    CognitiveRuntime,
)


class CognitiveAPI:
    """
    Production API adapter for Cognitive Platform.
    """

    def __init__(self) -> None:

        self._runtime = CognitiveRuntime()


    def status(self) -> dict:

        return self._runtime.status()


    def execute(self) -> dict:

        decision = self._runtime.execute()

        if decision is None:

            return {
                "status": "failed",
                "error": self._runtime.last_error,
            }


        return {
            "status": "executed",
            "action": decision.action,
            "confidence": decision.confidence,
        }
