"""
PocketBot Enterprise X

Hosted Service Manager.
"""

from __future__ import annotations

from collections.abc import Iterable

from pocketbot.application.hosting.interfaces import (
    HostedService,
)


class HostedServiceManager:
    """
    Coordinates application hosted services lifecycle.
    """

    def __init__(
        self,
        services: Iterable[HostedService] | None = None,
    ) -> None:
        self._services: list[HostedService] = []

        if services is not None:
            self._services.extend(
                services,
            )

    def add(
        self,
        service: HostedService,
    ) -> None:
        """
        Registers a hosted service.
        """

        self._services.append(
            service,
        )

    def start(self) -> None:
        """
        Starts all hosted services.
        """

        for service in self._services:
            service.start()

    def stop(self) -> None:
        """
        Stops all hosted services.

        Services are stopped in reverse order
        to preserve dependency lifecycle.
        """

        for service in reversed(self._services):
            service.stop()