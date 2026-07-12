from __future__ import annotations

from pocketbot.production.bootstrap.context import (
    ProductionContext,
)
from pocketbot.production.bootstrap.runtime import (
    ProductionRuntime,
)


class ProductionRuntimeContext:
    def __init__(
        self,
        runtime: ProductionRuntime,
        context: ProductionContext,
    ) -> None:
        self.runtime = runtime
        self.context = context

    def start(self) -> bool:
        self.context.metrics.increment("startup")

        return self.runtime.start()

    def shutdown(self) -> bool:
        self.context.metrics.increment("shutdown")

        return self.runtime.shutdown()
