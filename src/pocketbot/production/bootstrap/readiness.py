from __future__ import annotations

from dataclasses import dataclass

from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.bootstrap.runtime_health import (
    ProductionRuntimeHealth,
)
from pocketbot.production.dependencies.check import (
    check_dependencies,
)


@dataclass
class ReadinessStatus:
    ready: bool


class ProductionReadiness:
    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
    ) -> None:
        self._runtime_context = runtime_context
        self._health = ProductionRuntimeHealth(
            runtime_context,
        )

    def check(self) -> ReadinessStatus:
        dependencies_ok = check_dependencies()
        health_ok = self._health.check().healthy

        return ReadinessStatus(
            ready=(
                dependencies_ok
                and health_ok
            )
        )
