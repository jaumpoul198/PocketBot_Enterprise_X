from __future__ import annotations

from pocketbot.production.health.check import (
    HealthStatus,
    check_health,
)


class ProductionHealth:
    def __init__(self, service_name: str = "pocketbot") -> None:
        self._service_name = service_name

    def check(self) -> HealthStatus:
        return check_health(
            self._service_name,
        )
