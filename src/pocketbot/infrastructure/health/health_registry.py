"""
PocketBot Enterprise X

Infrastructure Health Registry.
"""

from __future__ import annotations

from pocketbot.infrastructure.health.health_check import (
    HealthCheck,
    HealthStatus,
)


class HealthRegistry:
    """
    Registry for operational health checks.
    """

    def __init__(self) -> None:
        self._checks: dict[str, HealthCheck] = {}

    def register(
        self,
        check: HealthCheck,
    ) -> None:
        """
        Register or replace a health check.
        """

        self._checks[check.name] = check

    def get(
        self,
        name: str,
    ) -> HealthCheck | None:
        """
        Retrieve a health check by name.
        """

        return self._checks.get(name)

    def all(self) -> list[HealthCheck]:
        """
        Return all registered health checks.
        """

        return list(self._checks.values())

    def overall_status(self) -> HealthStatus:
        """
        Calculate overall infrastructure health.
        """

        statuses = {
            check.status
            for check in self._checks.values()
        }

        if HealthStatus.UNHEALTHY in statuses:
            return HealthStatus.UNHEALTHY

        if HealthStatus.DEGRADED in statuses:
            return HealthStatus.DEGRADED

        return HealthStatus.HEALTHY
