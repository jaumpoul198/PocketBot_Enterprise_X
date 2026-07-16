from __future__ import annotations

from pocketbot.enterprise.intelligence import (
    IntelligenceRuntime,
)


class IntelligenceAPI:
    """
    Production API adapter for Enterprise Intelligence.
    """

    def __init__(self) -> None:
        self._runtime = IntelligenceRuntime()

    def status(self) -> dict:
        return self._runtime.status()

    def decision(self) -> dict:
        result = self._runtime.evaluate(100)

        return {
            "action": result.action,
            "confidence": result.confidence,
            "reason": result.reason,
            "timestamp": result.timestamp.isoformat(),
        }

    def signals(self) -> list:
        return (
            self._runtime
            .engine
            .metrics
            .latest()
        )
