from __future__ import annotations

from typing import TYPE_CHECKING

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)
from pocketbot.enterprise.autonomy.autonomy_runtime_service import (
    AutonomyRuntimeService,
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

if TYPE_CHECKING:
    from pocketbot.production.bootstrap.health_runtime import (
        ProductionHealthRuntime,
    )


class ProductionRuntimeContext:
    """
    Coordinates the production runtime together with the
    application lifecycle, autonomy runtime and optional health runtime.
    """

    def __init__(
        self,
        runtime: ProductionRuntime,
        context: ProductionContext,
        lifecycle: LifecycleManager | None = None,
        autonomy: AutonomyRuntimeService | None = None,
    ) -> None:
        self.runtime = runtime
        self.context = context
        self._lifecycle = lifecycle
        self._autonomy = autonomy

        self._health_runtime: (
            ProductionHealthRuntime | None
        ) = None

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

    @property
    def autonomy(self) -> AutonomyRuntimeService | None:
        """
        Returns configured autonomy runtime service.
        """
        return self._autonomy

    def attach_health_runtime(
        self,
        health_runtime: ProductionHealthRuntime,
    ) -> None:
        """
        Attach production health HTTP runtime.
        """
        self._health_runtime = health_runtime

    def start(self) -> bool:
        """
        Starts application lifecycle, autonomy and runtime.
        """

        self.context.metrics.increment(
            "startup",
        )

        if self._lifecycle is not None:
            self._lifecycle.start()

        if self._autonomy is not None:
            self._autonomy.start()

        result = self.runtime.start()

        if result and self._health_runtime is not None:
            self._health_runtime.start()

        return result

    def shutdown(self) -> bool:
        """
        Stops health service, autonomy, runtime and lifecycle.
        """

        self.context.metrics.increment(
            "shutdown",
        )

        if self._health_runtime is not None:
            self._health_runtime.stop()

        if self._autonomy is not None:
            self._autonomy.stop()

        runtime_result = self.runtime.shutdown()

        if self._lifecycle is not None:
            self._lifecycle.stop()

        return runtime_result
