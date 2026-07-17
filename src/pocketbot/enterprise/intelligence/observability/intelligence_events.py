from __future__ import annotations

from datetime import datetime, timezone


class IntelligenceEvent:
    """
    Represents an Enterprise Intelligence event.
    """

    def __init__(
        self,
        event_type: str,
        payload: dict,
    ) -> None:

        self.event_type = event_type
        self.payload = payload
        self.created_at = datetime.now(timezone.utc)


    def to_dict(self) -> dict:
        return {
            "event_type": self.event_type,
            "payload": self.payload,
            "created_at": self.created_at.isoformat(),
        }



class IntelligenceEventStore:
    """
    Storage layer for intelligence events.
    """

    def __init__(self) -> None:

        self._events: list[IntelligenceEvent] = []


    def record(
        self,
        event_type: str,
        payload: dict,
    ) -> IntelligenceEvent:

        event = IntelligenceEvent(
            event_type,
            payload,
        )

        self._events.append(
            event
        )

        return event


    def all(self) -> list[dict]:

        return [
            event.to_dict()
            for event in self._events
        ]


    def latest(
        self,
        limit: int = 10,
    ) -> list[dict]:

        return [
            event.to_dict()
            for event in self._events[-limit:]
        ]



    def count(self) -> int:

        return len(
            self._events
        )



class IntelligenceEventManager:
    """
    Enterprise intelligence event manager.
    """

    def __init__(self) -> None:

        self.store = IntelligenceEventStore()


    def emit(
        self,
        event_type: str,
        payload: dict,
    ) -> dict:

        event = self.store.record(
            event_type,
            payload,
        )

        return event.to_dict()


    def history(self) -> list[dict]:

        return self.store.all()


    def recent(
        self,
        limit: int = 10,
    ) -> list[dict]:

        return self.store.latest(
            limit
        )


    def total_events(self) -> int:

        return self.store.count()
