"""
PocketBot Enterprise X

Hosted Service Runtime Wrapper.
"""

from __future__ import annotations

from pocketbot.application.hosting.interfaces import (
    HostedService,
)


class HostedServiceRuntime:
    """
    Runtime wrapper responsible for tracking
    hosted service lifecycle state.
    """

    def __init__(
        self,
        service: HostedService,
    ) -> None:

        if service is None:
            raise TypeError(
                "hosted service cannot be None",
            )

        self._service = service
        self._running = False
        self._failed = False

    def start(self) -> None:
        """
        Starts hosted service runtime.
        """

        try:
            self._service.start()
            self._running = True
            self._failed = False

        except Exception:
            self._running = False
            self._failed = True
            raise

    def stop(self) -> None:
        """
        Stops hosted service runtime.
        """

        try:
            self._service.stop()
            self._running = False

        except Exception:
            self._failed = True
            raise

    def health(self) -> bool:
        """
        Returns runtime health.
        """

        if self._failed:
            return False

        return self._service.health()

    @property
    def name(self) -> str:
        """
        Returns service name.
        """

        return self._service.name

    @property
    def running(self) -> bool:
        """
        Returns running state.
        """

        return self._running

    @property
    def failed(self) -> bool:
        """
        Returns failure state.
        """

        return self._failed

    @property
    def service(self) -> HostedService:
        """
        Returns wrapped service.
        """

        return self._service