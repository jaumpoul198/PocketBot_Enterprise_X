from __future__ import annotations

from threading import Thread

from pocketbot.production.api.health_server import (
    HealthServer,
)
from pocketbot.production.bootstrap.runtime_context import (
    ProductionRuntimeContext,
)
from pocketbot.production.health.service import (
    ProductionHealthService,
)


class ProductionHealthRuntime:
    """
    Controls production health HTTP runtime.
    """

    def __init__(
        self,
        runtime_context: ProductionRuntimeContext,
        port: int,
    ) -> None:

        self._service = ProductionHealthService(
            runtime_context,
        )

        self._server = HealthServer(
            port,
            self._service,
        )

        self._thread: Thread | None = None

    def start(self) -> None:
        if self._thread is not None:
            return

        self._thread = Thread(
            target=self._server.start,
            daemon=True,
        )

        self._thread.start()

    def stop(self) -> None:
        self._server.stop()

        if self._thread is not None:
            self._thread.join(
                timeout=5,
            )

        self._thread = None
