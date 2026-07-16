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

    def autonomy(self) -> dict:
        """
        Return operational autonomy metrics.
        """

        score = self._runtime.history.autonomy_score()

        if score >= 90:
            status = "high_autonomy"
        elif score >= 70:
            status = "medium_autonomy"
        else:
            status = "low_autonomy"

        return {
            "autonomy_score": score,
            "decision_count": self._runtime.history.count(),
            "status": status,
        }
