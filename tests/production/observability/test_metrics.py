from pocketbot.production.observability.metrics import ProductionMetrics


def test_metrics_increment() -> None:
    metrics = ProductionMetrics()

    metrics.increment("startup")

    assert metrics.get("startup") == 1


def test_metrics_default_zero() -> None:
    metrics = ProductionMetrics()

    assert metrics.get("missing") == 0
