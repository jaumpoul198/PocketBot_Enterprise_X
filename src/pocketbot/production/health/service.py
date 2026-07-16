from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


@dataclass(frozen=True)
class RuntimeAutonomyHealth:
    """
    Autonomy health status exposed by production health runtime.
    """

    status: str
    started: bool
    failures: int


@dataclass(frozen=True)
class RuntimeHealthStatus:
    healthy: bool
    ready: bool
    alive: bool
    service: str
    uptime_seconds: float
    autonomy: RuntimeAutonomyHealth


class ProductionHealthService:
    """
    Enterprise runtime health service.

    Provides:
    - liveness validation
    - readiness validation
    - complete health status
    - autonomy runtime visibility
    """

    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
        service_name: str = "pocketbot",
    ) -> None:
        self._runtime_context = runtime_context
        self._service_name = service_name
        self._started_at = datetime.now(
            timezone.utc,
        )

    def liveness(self) -> RuntimeHealthStatus:
        """
        Checks if process/runtime exists.
        """

        return RuntimeHealthStatus(
            healthy=True,
            ready=self._runtime_context.runtime.started,
            alive=True,
            service=self._service_name,
            uptime_seconds=self._uptime(),
            autonomy=self._autonomy_health(),
        )

    def readiness(self) -> RuntimeHealthStatus:
        """
        Checks if runtime is ready to serve.
        """

        ready = self._runtime_context.runtime.started

        return RuntimeHealthStatus(
            healthy=ready,
            ready=ready,
            alive=True,
            service=self._service_name,
            uptime_seconds=self._uptime(),
            autonomy=self._autonomy_health(),
        )

    def health(self) -> RuntimeHealthStatus:
        """
        Complete health status.
        """

        live = self.liveness()

        return RuntimeHealthStatus(
            healthy=live.alive and live.ready,
            ready=live.ready,
            alive=live.alive,
            service=live.service,
            uptime_seconds=live.uptime_seconds,
            autonomy=live.autonomy,
        )

    def _autonomy_health(self) -> RuntimeAutonomyHealth:
        """
        Converts autonomy runtime snapshot into health contract.
        """

        autonomy = self._runtime_context.autonomy

        if autonomy is None:
            return RuntimeAutonomyHealth(
                status="inactive",
                started=False,
                failures=0,
            )

        snapshot = autonomy.snapshot()

        failures = self._extract_failures(
            snapshot.metrics,
        )

        return RuntimeAutonomyHealth(
            status="active" if snapshot.active else "inactive",
            started=autonomy.started,
            failures=failures,
        )

    @staticmethod
    def _extract_failures(
        metrics: dict[str, Any],
    ) -> int:
        value = metrics.get(
            "failures",
            0,
        )

        if isinstance(value, int):
            return value

        return 0

    def _uptime(self) -> float:
        return (
            datetime.now(
                timezone.utc,
            )
            - self._started_at
        ).total_seconds()
