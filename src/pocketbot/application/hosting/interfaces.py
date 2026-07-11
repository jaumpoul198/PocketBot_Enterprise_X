"""
PocketBot Enterprise X

Hosted Service Interfaces.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class HostedService(ABC):
    """
    Base contract for application hosted services.

    Hosted services are components managed by the
    application lifecycle.
    """

    @abstractmethod
    def start(self) -> None:
        """
        Starts the hosted service.
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """
        Stops the hosted service.
        """
        raise NotImplementedError
