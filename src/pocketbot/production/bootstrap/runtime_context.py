from __future__ import annotations

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.production.bootstrap.context import (
    ProductionContext,
)
from pocketbot.production.bootstrap.runtime import (
    ProductionRuntime,
)
from pocketbot.production.config.settings import (
    ProductionSettings,
)


class ProductionRuntimeContext:
    """
    Coordinates the production runtime together with the
    application lifecycle.
    """

    def __init__(
        self,
        runtime: ProductionRuntime,
        context: ProductionContext,
        lifecycle: LifecycleManager | None = None,
    ) -> None:
        self.runtime = runtime
        self.context = context
        self._lifecycle = lifecycle

    @property
    def settings(self) -> ProductionSettings:
        """
        Returns runtime settings.
        """
        return self.runtime.settings

    @property
    def lifecycle(self) -> LifecycleManager | None:
        """
        Returns the configured lifecycle manager.
        """
        return self._lifecycle

    def start(self) -> bool:
        """
        Starts the application lifecycle and then the runtime.
        """
        self.context.metrics.increment("startup")

        if self._lifecycle is not None:
            self._lifecycle.start()

        return self.runtime.start()

    def shutdown(self) -> bool:
        """
        Stops the runtime and then the application lifecycle.
        """
        self.context.metrics.increment("shutdown")

        runtime_result = self.runtime.shutdown()

        if self._lifecycle is not None:
            self._lifecycle.stop()

        return runtime_result