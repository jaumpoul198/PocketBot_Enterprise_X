"""
PocketBot Enterprise X

Application Startup Lifecycle.
"""

from __future__ import annotations

from pocketbot.application.hosting.hosted_service_manager import (
    HostedServiceManager,
)


class Startup:
    """
    Handles application startup operations.
    """

    def __init__(
        self,
        hosted_services: HostedServiceManager,
    ) -> None:
        self._hosted_services = hosted_services

    def execute(self) -> None:
        """
        Executes startup sequence.
        """

        self._hosted_services.start()
