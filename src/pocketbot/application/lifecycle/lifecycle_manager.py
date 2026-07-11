"""
PocketBot Enterprise X

Application Lifecycle Manager.
"""

from __future__ import annotations

from pocketbot.application.lifecycle.shutdown import (
    Shutdown,
)
from pocketbot.application.lifecycle.startup import (
    Startup,
)


class LifecycleManager:
    """
    Controls application lifecycle flow.
    """

    def __init__(
        self,
        startup: Startup,
        shutdown: Shutdown,
    ) -> None:
        self._startup = startup
        self._shutdown = shutdown

    def start(self) -> None:
        """
        Starts application lifecycle.
        """

        self._startup.execute()

    def stop(self) -> None:
        """
        Stops application lifecycle.
        """

        self._shutdown.execute()
