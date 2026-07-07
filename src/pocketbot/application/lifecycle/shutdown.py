"""
PocketBot Enterprise X

Application Shutdown Lifecycle.
"""

from __future__ import annotations

from pocketbot.application.hosting.hosted_service_manager import (
    HostedServiceManager,
)


class Shutdown:
    """
    Handles application shutdown operations.
    """

    def __init__(
        self,
        hosted_services: HostedServiceManager,
    ) -> None:
        self._hosted_services = hosted_services

    def execute(self) -> None:
        """
        Executes shutdown sequence.
        """

        self._hosted_services.stop()
