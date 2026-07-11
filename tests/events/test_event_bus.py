from __future__ import annotations

import pytest

from pocketbot.events.event import Event
from pocketbot.events.event_bus import EventBus
from pocketbot.events.exceptions import EventHandlingError
from pocketbot.events.handlers import EventHandler


class SuccessfulHandler(EventHandler):
    def __init__(self) -> None:
        self.called = False

    def handle(self, event: Event) -> None:
        self.called = True


class FailingHandler(EventHandler):
    def handle(self, event: Event) -> None:
        raise RuntimeError("handler failure")


def test_event_bus_executes_handler() -> None:
    bus = EventBus()

    handler = SuccessfulHandler()

    bus.subscribe(
        "test",
        handler,
    )

    bus.publish(
        Event(
            name="test",
            payload={},
        )
    )

    assert handler.called is True


def test_event_bus_wraps_handler_failure() -> None:
    bus = EventBus()

    bus.subscribe(
        "test",
        FailingHandler(),
    )

    with pytest.raises(EventHandlingError):
        bus.publish(
            Event(
                name="test",
                payload={},
            )
        )


def test_event_bus_executes_global_handler() -> None:
    bus = EventBus()

    handler = SuccessfulHandler()

    bus.add_global_handler(
        handler,
    )

    bus.publish(
        Event(
            name="application.started",
            payload={},
        )
    )

    assert handler.called is True
