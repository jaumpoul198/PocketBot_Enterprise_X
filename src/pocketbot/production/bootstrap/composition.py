"""
PocketBot Enterprise X

Production Composition Root.
"""

from __future__ import annotations

from pocketbot.bootstrap.builder import (
    ApplicationBuilder,
)

from pocketbot.application.hosting.hosted_service_manager import (
    HostedServiceManager,
)

from pocketbot.application.lifecycle.lifecycle_manager import (
    LifecycleManager,
)

from pocketbot.application.lifecycle.startup import (
    Startup,
)

from pocketbot.application.lifecycle.shutdown import (
    Shutdown,
)

from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)


class ProductionComposition:
    """
    Builds production application dependencies.
    """

    def __init__(
        self,
    ) -> None:

        self._provider: IServiceProvider | None = None

        self._hosted_services = (
            HostedServiceManager()
        )

        self._lifecycle: LifecycleManager | None = None


    def build(
        self,
    ) -> LifecycleManager:
        """
        Builds production lifecycle.
        """

        builder = ApplicationBuilder()

        self._provider = builder.build()


        startup = Startup(
            self._hosted_services,
        )


        shutdown = Shutdown(
            self._hosted_services,
            self._provider,
        )


        self._lifecycle = LifecycleManager(
            startup=startup,
            shutdown=shutdown,
        )


        return self._lifecycle