from __future__ import annotations

from pocketbot.events.event import Event
from pocketbot.events.event_bus import EventBus
from pocketbot.events.publisher import EventPublisher


class MutatingHandler:
    def handle(self, event: Event) -> None:
        event.payload["status"] = "changed"


class CapturingHandler:
    def __init__(self) -> None:
        self.payload = None

    def handle(self, event: Event) -> None:
        self.payload = event.payload


def test_event_payload_isolated_from_external_mutation() -> None:
    bus = EventBus()
    publisher = EventPublisher(bus)

    captured = CapturingHandler()

    bus.subscribe(
        "runtime.started",
        captured,
    )

    payload = {
        "status": "healthy",
    }

    publisher.publish(
        "runtime.started",
        payload,
    )

    payload["status"] = "broken"

    assert captured.payload["status"] == "healthy"


def test_event_handlers_receive_isolated_event_instances() -> None:
    bus = EventBus()

    mutator = MutatingHandler()
    captured = CapturingHandler()

    bus.subscribe(
        "runtime.started",
        mutator,
    )

    bus.subscribe(
        "runtime.started",
        captured,
    )

    bus.publish(
        Event(
            name="runtime.started",
            payload={
                "status": "healthy",
            },
        )
    )

    assert captured.payload["status"] == "healthy"
