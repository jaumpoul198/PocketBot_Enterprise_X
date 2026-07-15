"""
PocketBot Enterprise X

Hosted Service Manager.
"""

from __future__ import annotations

from collections.abc import Iterable

from pocketbot.application.hosting.hosted_service_state import (
    HostedServiceState,
)
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

        self._states[service.name] = (
            HostedServiceState.CREATED
        )

    def start(self) -> None:
        """
        Starts all hosted services.
        """

        for service in self._services:

            if self._states[service.name] is (
                HostedServiceState.RUNNING
            ):
                continue

            self._states[service.name] = (
                HostedServiceState.STARTING
            )

            try:
                service.start()
            except Exception:
                self._states[service.name] = (
                    HostedServiceState.FAILED
                )
                raise

            self._states[service.name] = (
                HostedServiceState.RUNNING
            )

    def stop(self) -> None:
        """
        Stops all hosted services.
        """

        for service in reversed(self._services):

            if self._states[service.name] is (
                HostedServiceState.STOPPED
            ):
                continue

            self._states[service.name] = (
                HostedServiceState.STOPPING
            )

            try:
                service.stop()
            except Exception:
                self._states[service.name] = (
                    HostedServiceState.FAILED
                )
                raise

            self._states[service.name] = (
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
        Returns the health status of all hosted services.
        """

        return {
            service.name: service.health()
            for service in self._services
        }

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

    def state(
        self,
        service_name: str,
    ) -> HostedServiceState:
        """
        Returns service lifecycle state.
        """

        return self._states[service_name]