from __future__ import annotations

from pocketbot.infrastructure.metrics.metrics_registry import (
    MetricsRegistry,
)


def test_metric_updates_replace_internal_state_isolated() -> None:
    registry = MetricsRegistry()

    registry.increment(
        "orders",
    )

    first = registry.get(
        "orders",
    )

    assert first is not None

    registry.increment(
        "orders",
    )

    second = registry.get(
        "orders",
    )

    assert second is not None

    assert first.value == 1
    assert second.value == 2
