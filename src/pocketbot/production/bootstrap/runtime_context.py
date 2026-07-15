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
    application lifecycle and optional health runtime.
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

        self._health_runtime = None

    @property
    def settings(self) -> ProductionSettings:
        """
        Returns runtime settings.
        """
        return self.runtime.settings

    @property
    def lifecycle(self) -> LifecycleManager | None:
        """
        Returns configured lifecycle manager.
        """
        return self._lifecycle

    def attach_health_runtime(
        self,
        health_runtime: object,
    ) -> None:
        """
        Attach production health HTTP runtime.
        """

        self._health_runtime = health_runtime

    def start(self) -> bool:
        """
        Starts application lifecycle and runtime.
        """

        self.context.metrics.increment(
            "startup",
        )

        if self._lifecycle is not None:
            self._lifecycle.start()

        result = self.runtime.start()

        if result and self._health_runtime is not None:
            self._health_runtime.start()

        return result

    def shutdown(self) -> bool:
        """
        Stops runtime, health service and lifecycle.
        """

        self.context.metrics.increment(
            "shutdown",
        )

        if self._health_runtime is not None:
            self._health_runtime.stop()

        runtime_result = self.runtime.shutdown()

        if self._lifecycle is not None:
            self._lifecycle.stop()

        return runtime_result
