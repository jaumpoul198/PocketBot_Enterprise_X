from __future__ import annotations

from datetime import datetime

from pocketbot.enterprise.intelligence.observability.intelligence_events import (
    IntelligenceEventManager,
)


class IntelligenceMonitor:
    """
    Enterprise Intelligence runtime monitor.
    Collects runtime events and provides operational statistics.
    """

    def __init__(self) -> None:

        self._events = IntelligenceEventManager()

        self._started_at = datetime.utcnow()

        self._checks = 0


    def record(
        self,
        category: str,
        payload: dict,
    ) -> dict:

        self._checks += 1

        return self._events.emit(
            category,
            payload,
        )


    def health(self) -> dict:

        return {
            "status": "healthy",
            "checks": self._checks,
            "uptime_seconds": (
                datetime.utcnow() - self._started_at
            ).total_seconds(),
            "events": self._events.total_events(),
        }


    def history(self) -> list[dict]:

        return self._events.history()


    def recent(
        self,
        limit: int = 10,
    ) -> list[dict]:

        return self._events.recent(
            limit
        )


    def summary(self) -> dict:

        return {
            "status": "running",
            "events": self._events.total_events(),
            "checks": self._checks,
        }
