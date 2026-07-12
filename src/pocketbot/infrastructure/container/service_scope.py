"""
PocketBot Enterprise X
Infrastructure Container

Dependency injection scope implementation.
"""

from __future__ import annotations

from typing import Any

from pocketbot.infrastructure.container.exceptions import (
    ScopeDisposedError,
)
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
    IServiceScope,
)


class ServiceScope(IServiceScope):
    """
    Represents an isolated dependency injection scope.
    """

    def __init__(self) -> None:
        self._provider: IServiceProvider | None = None
        self._instances: dict[type[Any], Any] = {}
        self._disposed = False

    @property
    def service_provider(self) -> IServiceProvider:
        """
        Returns the scoped service provider.
        """
        if self._disposed:
            raise ScopeDisposedError(
                "This service scope has already been disposed."
            )

        if self._provider is None:
            raise RuntimeError(
                "Scoped provider has not been attached."
            )

        return self._provider

    @property
    def instances(self) -> dict[type[Any], Any]:
        """
        Returns the scoped instances cache.

        Internal scope resolution requires direct access,
        therefore this remains an internal cache contract.
        """
        if self._disposed:
            raise ScopeDisposedError(
                "This service scope has already been disposed."
            )

        return self._instances

    @property
    def is_disposed(self) -> bool:
        """
        Indicates whether the scope has been disposed.
        """
        return self._disposed

    def attach_provider(
        self,
        provider: IServiceProvider,
    ) -> None:
        """
        Attaches the scoped provider.
        """
        if self._provider is not None and self._provider is not provider:
            raise RuntimeError(
                "Scoped provider is already attached."
            )

        self._provider = provider

    def dispose(self) -> None:
        """
        Releases all scoped instances.
        """
        self._instances.clear()
        self._disposed = True
