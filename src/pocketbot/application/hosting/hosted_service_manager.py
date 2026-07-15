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
            for service in services:
                self.add(service)

    def add(
        self,
        service: HostedService,
    ) -> None:
        """
        Registers a hosted service.
        """

        if service is None:
            raise TypeError(
                "hosted service cannot be None",
            )

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

        Services are stopped in reverse order
        to preserve dependency lifecycle.
        """

        for service in reversed(self._services):
            service.stop()

    def restart(self) -> None:
        """
        Restarts all hosted services.
        """

        self.stop()
        self.start()

    def health(self) -> dict[str, bool]:
        """
        Returns the health status of all hosted services.
        """

        return {
            service.name: service.health()
            for service in self._services
        }

    @property
    def services(self) -> tuple[HostedService, ...]:
        """
        Returns registered hosted services.
        """

        return tuple(self._services)