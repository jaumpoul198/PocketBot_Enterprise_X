from __future__ import annotations

from pocketbot.enterprise.intelligence import (
    IntelligenceRuntime,
)

from pocketbot.enterprise.intelligence.context.context_runtime import (
    ContextRuntime,
)

from pocketbot.enterprise.intelligence.context.context_metrics import (
    ContextMetrics,
)


class IntelligenceAPI:
    """
    Production API adapter for Enterprise Intelligence.
    """

    def __init__(self) -> None:

        self._runtime = IntelligenceRuntime()

        self._context = ContextRuntime()

        self._context_metrics = ContextMetrics()


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


    def context_history(self) -> dict:
        """
        Return intelligence context history.
        """

        history = self._context.get_context_history()

        return {
            "count": len(history),
            "history": [
                {
                    "decision_id": item.decision_id,
                    "score": item.score,
                }
                for item in history
            ],
        }


    def context_metrics(self) -> dict:
        """
        Return context intelligence metrics.
        """

        return self._context_metrics.snapshot()
