"""
Tests for MetricsRegistry state isolation.
"""

from pocketbot.infrastructure.metrics.metrics_registry import (
    MetricsRegistry,
)


def test_returned_metric_is_isolated_from_registry_state() -> None:
    registry = MetricsRegistry()

    registry.increment(
        "orders",
    )

    metric = registry.get(
        "orders",
    )

    assert metric is not None

    metric.value = 999

    stored = registry.get(
        "orders",
    )

    assert stored is not None
    assert stored.value == 1


def test_returned_metrics_are_isolated_from_registry_state() -> None:
    registry = MetricsRegistry()

    registry.increment(
        "orders",
    )

    metrics = registry.all()

    metrics[0].value = 999

    stored = registry.get(
        "orders",
    )

    assert stored is not None
    assert stored.value == 1
