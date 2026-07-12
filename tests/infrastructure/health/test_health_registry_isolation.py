from __future__ import annotations

from pocketbot.infrastructure.health.health_check import (
    HealthCheck,
    HealthStatus,
)
from pocketbot.infrastructure.health.health_registry import (
    HealthRegistry,
)


def test_registered_health_check_is_isolated_from_external_mutation() -> None:
    registry = HealthRegistry()

    check = HealthCheck(
        name="database",
        status=HealthStatus.HEALTHY,
        metadata={"connection": "ok"},
    )

    registry.register(check)

    check.status = HealthStatus.UNHEALTHY
    check.metadata["connection"] = "broken"

    stored = registry.get("database")

    assert stored is not None
    assert stored.status is HealthStatus.HEALTHY
    assert stored.metadata == {"connection": "ok"}


def test_get_returns_isolated_health_check_copy() -> None:
    registry = HealthRegistry()

    registry.register(
        HealthCheck(
            name="cache",
            status=HealthStatus.HEALTHY,
            metadata={"state": "ready"},
        )
    )

    retrieved = registry.get("cache")

    assert retrieved is not None

    retrieved.status = HealthStatus.UNHEALTHY
    retrieved.metadata["state"] = "broken"

    stored = registry.get("cache")

    assert stored is not None
    assert stored.status is HealthStatus.HEALTHY
    assert stored.metadata == {"state": "ready"}


def test_all_returns_isolated_health_check_collection() -> None:
    registry = HealthRegistry()

    registry.register(
        HealthCheck(
            name="api",
            status=HealthStatus.DEGRADED,
        )
    )

    checks = registry.all()

    checks[0].status = HealthStatus.UNHEALTHY

    stored = registry.get("api")

    assert stored is not None
    assert stored.status is HealthStatus.DEGRADED


def test_overall_status_returns_worst_state() -> None:
    registry = HealthRegistry()

    registry.register(
        HealthCheck(
            name="api",
            status=HealthStatus.HEALTHY,
        )
    )

    registry.register(
        HealthCheck(
            name="database",
            status=HealthStatus.DEGRADED,
        )
    )

    assert registry.overall_status() is HealthStatus.DEGRADED
