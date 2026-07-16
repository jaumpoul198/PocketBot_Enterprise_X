from pocketbot.enterprise.intelligence.observability.intelligence_events import (
    IntelligenceEventManager,
)


def test_intelligence_event_emit():

    manager = IntelligenceEventManager()

    event = manager.emit(
        "decision",
        {
            "action": "buy",
            "confidence": 95,
        },
    )

    assert event["event_type"] == "decision"



def test_intelligence_event_history():

    manager = IntelligenceEventManager()

    manager.emit(
        "signal",
        {
            "value": 10,
        },
    )

    assert manager.total_events() == 1


def test_intelligence_event_recent():

    manager = IntelligenceEventManager()

    manager.emit(
        "runtime",
        {
            "status": "ok",
        },
    )

    events = manager.recent()

    assert len(events) == 1
