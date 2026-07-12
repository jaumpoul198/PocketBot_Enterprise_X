from __future__ import annotations

from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)


class ProductionLifecycle:
    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
    ) -> None:
        self._runtime_context = runtime_context

    def start(self) -> bool:
        return self._runtime_context.start()

    def shutdown(self) -> bool:
        return self._runtime_context.shutdown()
