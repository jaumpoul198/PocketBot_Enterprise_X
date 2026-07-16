from pocketbot.enterprise.autonomy import (
    AutonomyMonitor,
    AutonomyRuntimeService,
)


def test_runtime_service_start_and_stop() -> None:
    monitor = AutonomyMonitor()
    service = AutonomyRuntimeService(
        monitor=monitor,
    )

    assert service.started is False

    service.start()

    assert service.started is True
    assert monitor.active is True

    service.stop()

    assert service.started is False
    assert monitor.active is False


def test_runtime_service_snapshot() -> None:
    monitor = AutonomyMonitor()
    service = AutonomyRuntimeService(
        monitor=monitor,
    )

    service.start()

    snapshot = service.snapshot()

    assert snapshot.active is True
    assert snapshot.healthy is True
