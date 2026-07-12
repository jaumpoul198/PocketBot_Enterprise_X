from __future__ import annotations

from collections.abc import Callable

from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


class ProductionErrorBoundary:
    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
    ) -> None:
        self._runtime_context = runtime_context

    def execute(
        self,
        operation: Callable[[], bool],
    ) -> bool:
        try:
            return operation()

        except Exception:
            self._runtime_context.context.metrics.increment(
                "errors",
            )

            return False
