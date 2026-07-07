"""
PocketBot Enterprise X

Hosted Service Manager.
"""

from __future__ import annotations

from pocketbot.application.hosting.interfaces import (
    HostedService,
)


class HostedServiceManager:
    """
    Coordinates application hosted services lifecycle.
    """

    def __init__(
        self,
    ) -> None:
        self._services: list[HostedService] = []

    def add(
        self,
        service: HostedService,
    ) -> None:
        """
        Registers a hosted service.
        """

        self._services.append(service)

    def start(self) -> None:
        """
        Starts all hosted services.
        """

        for service in self._services:
            service.start()

    def stop(self) -> None:
        """
        Stops all hosted services.
        """

        for service in reversed(self._services):
            service.stop()
