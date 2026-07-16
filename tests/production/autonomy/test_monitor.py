from pocketbot.enterprise.autonomy import (
    AutonomyMonitor,
    AutonomySnapshot,
)


def test_autonomy_monitor_initial_state() -> None:
    monitor = AutonomyMonitor()

    snapshot = monitor.snapshot()

    assert isinstance(snapshot, AutonomySnapshot)
    assert snapshot.healthy is True
    assert snapshot.active is False
    assert snapshot.metrics == {}


def test_autonomy_monitor_start_and_stop() -> None:
    monitor = AutonomyMonitor()

    monitor.start()

    assert monitor.active is True

    monitor.stop()

    assert monitor.active is False


def test_autonomy_monitor_health_update() -> None:
    monitor = AutonomyMonitor()

    monitor.update_health(False)

    snapshot = monitor.snapshot()

    assert snapshot.healthy is False


def test_autonomy_monitor_metrics() -> None:
    monitor = AutonomyMonitor()

    monitor.update_metric(
        "cycles",
        10,
    )

    snapshot = monitor.snapshot()

    assert snapshot.metrics["cycles"] == 10
