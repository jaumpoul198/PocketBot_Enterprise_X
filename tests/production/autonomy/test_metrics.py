from pocketbot.enterprise.autonomy.autonomy_metrics import (
    AutonomyMetrics,
)
from pocketbot.infrastructure.metrics import (
    MetricsRegistry,
)


def test_autonomy_metrics_lifecycle() -> None:
    registry = MetricsRegistry()
    metrics = AutonomyMetrics(registry)

    metrics.record_start()
    metrics.record_stop()

    assert registry.get(
        AutonomyMetrics.AUTONOMY_STARTED
    ).value == 1

    assert registry.get(
        AutonomyMetrics.AUTONOMY_STOPPED
    ).value == 1


def test_autonomy_metrics_failures() -> None:
    registry = MetricsRegistry()
    metrics = AutonomyMetrics(registry)

    assert metrics.failures() == 0

    metrics.record_failure()

    assert metrics.failures() == 1
