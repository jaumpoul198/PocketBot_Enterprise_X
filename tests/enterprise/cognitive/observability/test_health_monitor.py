from pocketbot.enterprise.cognitive.observability.cognitive_monitor import (
    CognitiveMonitor,
)

from pocketbot.enterprise.cognitive.observability.health_monitor import (
    HealthMonitor,
)


def test_health_status():
    monitor = CognitiveMonitor()

    health = HealthMonitor(
        monitor,
    )

    status = health.status()

    assert status["healthy"] is True
    assert status["metrics"] == 0
    assert status["events"] == 0
    assert status["traces"] == 0


def test_health_after_activity():
    monitor = CognitiveMonitor()

    health = HealthMonitor(
        monitor,
    )

    monitor.record_metric(
        name="performance",
        value=1.0,
        component="runtime",
    )

    monitor.emit_event(
        event_type="cycle",
        source="runtime",
    )

    status = health.status()

    assert status["healthy"] is True
    assert status["metrics"] == 1
    assert status["events"] == 1


def test_is_healthy():
    monitor = CognitiveMonitor()

    health = HealthMonitor(
        monitor,
    )

    assert health.is_healthy() is True
