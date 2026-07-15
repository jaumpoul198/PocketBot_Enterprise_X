from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


@dataclass(frozen=True)
class RuntimeHealthStatus:
    healthy: bool
    ready: bool
    alive: bool
    service: str
    uptime_seconds: float


class ProductionHealthService:
    """
    Enterprise runtime health service.

    Provides:
    - liveness validation
    - readiness validation
    - complete health status
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
        )

    def _uptime(self) -> float:
        return (
            datetime.now(
                timezone.utc,
            )
            - self._started_at
        ).total_seconds()
