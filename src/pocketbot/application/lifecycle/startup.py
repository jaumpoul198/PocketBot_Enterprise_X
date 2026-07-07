"""
PocketBot Enterprise X

Application Startup Lifecycle.
"""

from __future__ import annotations

from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)


class Startup:
    """
    Handles application startup operations.
    """

    def __init__(
        self,
        provider: IServiceProvider,
    ) -> None:
        self._provider = provider

    def execute(self) -> None:
        """
        Executes startup sequence.
        """

        self._provider
