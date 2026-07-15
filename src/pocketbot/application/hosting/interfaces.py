"""
PocketBot Enterprise X

Hosted Service Interfaces.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class HostedService(ABC):
    """
    Base contract for application hosted services.
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

    def health(self) -> bool:
        """
        Returns whether the service is healthy.

        Default implementation preserves backward compatibility.
        """
        return True

    def restart(self) -> None:
        """
        Restarts the hosted service.

        Default implementation preserves backward compatibility.
        """
        self.stop()
        self.start()

    @property
    def name(self) -> str:
        """
        Returns the hosted service name.
        """
        return self.__class__.__name__