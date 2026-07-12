from __future__ import annotations

from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


class ProductionShutdown:
    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
    ) -> None:
        self._runtime_context = runtime_context

    def shutdown(self) -> bool:
        return self._runtime_context.shutdown()
