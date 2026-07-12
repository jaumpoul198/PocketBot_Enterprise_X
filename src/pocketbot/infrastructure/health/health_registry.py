"""
PocketBot Enterprise X

Infrastructure Health Registry.
"""

from __future__ import annotations

from copy import deepcopy

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

        The registry stores an isolated copy.
        """

        self._checks[check.name] = deepcopy(check)

    def get(
        self,
        name: str,
    ) -> HealthCheck | None:
        """
        Retrieve an isolated health check copy.
        """

        check = self._checks.get(name)

        if check is None:
            return None

        return deepcopy(check)

    def all(self) -> list[HealthCheck]:
        """
        Return isolated health check copies.
        """

        return [
            deepcopy(check)
            for check in self._checks.values()
        ]

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
