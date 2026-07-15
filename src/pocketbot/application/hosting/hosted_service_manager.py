"""
PocketBot Enterprise X

Hosted Service Manager.
"""

from __future__ import annotations

from collections.abc import Iterable

from pocketbot.application.hosting.interfaces import (
    HostedService,
)
from pocketbot.application.hosting.hosted_service_state import (
    HostedServiceState,
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
        self._states: dict[str, HostedServiceState] = {}

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

        self._services.append(
            service,
        )

        service_name = getattr(
            service,
            "name",
            service.__class__.__name__,
        )

        self._states[service_name] = (
            HostedServiceState.CREATED
        )

    def start(self) -> None:
        """
        Starts all hosted services.
        """

        for service in self._services:
            service.start()

            service_name = getattr(
                service,
                "name",
                service.__class__.__name__,
            )

            self._states[service_name] = (
                HostedServiceState.RUNNING
            )

    def stop(self) -> None:
        """
        Stops all hosted services.

        Services are stopped in reverse order
        to preserve dependency lifecycle.
        """

        for service in reversed(self._services):
            service.stop()

            service_name = getattr(
                service,
                "name",
                service.__class__.__name__,
            )

            self._states[service_name] = (
                HostedServiceState.STOPPED
            )

    def restart(self) -> None:
        """
        Restarts all hosted services.
        """

        self.stop()
        self.start()

    def health(self) -> dict[str, bool]:
        """
        Returns health status of all hosted services.
        """

        return {
            getattr(
                service,
                "name",
                service.__class__.__name__,
            ): service.health()
            for service in self._services
        }

    def state(
        self,
        service: HostedService,
    ) -> HostedServiceState:
        """
        Returns current service lifecycle state.
        """

        service_name = getattr(
            service,
            "name",
            service.__class__.__name__,
        )

        return self._states[service_name]

    @property
    def services(
        self,
    ) -> tuple[HostedService, ...]:
        """
        Returns registered hosted services.
        """

        return tuple(
            self._services,
        )

    @property
    def states(
        self,
    ) -> dict[str, HostedServiceState]:
        """
        Returns lifecycle states snapshot.
        """

        return dict(
            self._states,
        )