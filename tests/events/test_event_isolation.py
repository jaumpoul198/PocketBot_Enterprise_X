from __future__ import annotations

from pocketbot.events.event import Event


def test_event_payload_isolated_from_constructor_input() -> None:
    payload = {
        "status": "healthy",
    }

    event = Event(
        name="runtime.started",
        payload=payload,
    )

    payload["status"] = "broken"

    assert event.payload["status"] == "healthy"


def test_event_payload_mutation_does_not_affect_source_payload() -> None:
    payload = {
        "nested": {
            "value": 1,
        },
    }

    event = Event(
        name="runtime.started",
        payload=payload,
    )

    event.payload["nested"]["value"] = 999

    assert payload["nested"]["value"] == 1
