from pocketbot.production.observability.metrics import (
    ProductionMetrics,
)


def test_metrics_contract_isolated_instances() -> None:
    first = ProductionMetrics()
    second = ProductionMetrics()

    first.increment("startup")

    assert first.get("startup") == 1
    assert second.get("startup") == 0


def test_metrics_contract_multiple_counters() -> None:
    metrics = ProductionMetrics()

    metrics.increment("startup")
    metrics.increment("startup")
    metrics.increment("shutdown")

    assert metrics.get("startup") == 2
    assert metrics.get("shutdown") == 1


def test_metrics_contract_missing_values_are_safe() -> None:
    metrics = ProductionMetrics()

    assert metrics.get("unknown") == 0
