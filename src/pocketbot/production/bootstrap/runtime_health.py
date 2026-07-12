from __future__ import annotations

from pocketbot.production.bootstrap.health import (
    ProductionHealth,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.health.check import (
    HealthStatus,
)


class ProductionRuntimeHealth:
    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
    ) -> None:
        self._runtime_context = runtime_context
        self._health = ProductionHealth()

    def check(self) -> HealthStatus:
        return self._health.check()
