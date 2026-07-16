from __future__ import annotations

from datetime import datetime, UTC


class IntelligenceHistory:
    """
    Operational decision history storage.

    Keeps runtime intelligence decisions
    for observability and autonomy analysis.
    """

    def __init__(self):
        self._records = []

    def record(
        self,
        decision: str,
        confidence: float,
        health_score: float,
    ) -> dict:
        """
        Register an intelligence decision event.
        """

        autonomy_score = self._calculate_autonomy(
            confidence,
            health_score,
        )

        event = {
            "decision": decision,
            "confidence": confidence,
            "health_score": health_score,
            "autonomy_score": autonomy_score,
            "timestamp": datetime.now(UTC),
        }

        self._records.append(event)

        return event

    def latest(self, limit: int = 10) -> list:
        """
        Return latest intelligence decisions.
        """

        return self._records[-limit:]

    def count(self) -> int:
        """
        Return number of stored decisions.
        """

        return len(self._records)

    def autonomy_score(self) -> float:
        """
        Return average autonomy score.
        """

        if not self._records:
            return 0.0

        total = sum(
            item["autonomy_score"]
            for item in self._records
        )

        return round(
            total / len(self._records),
            2,
        )

    def clear(self) -> None:
        """
        Clear decision history.
        """

        self._records.clear()

    def _calculate_autonomy(
        self,
        confidence: float,
        health_score: float,
    ) -> float:
        """
        Calculate operational autonomy score.
        """

        score = (
            (confidence * 100) * 0.5
            +
            health_score * 0.5
        )

        return round(score, 2)
