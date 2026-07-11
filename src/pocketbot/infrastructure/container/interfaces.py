"""
PocketBot Enterprise X
Infrastructure Container

Dependency Injection container interfaces.
"""

from __future__ import annotations

from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class IServiceProvider(Protocol):
    """
    Resolves registered services.
    """

    def get_service(
        self,
        service_type: type[T],
    ) -> T:
        """
        Resolve a service.

        Raises:
            ServiceNotRegisteredError
            ServiceResolutionError
        """
        ...

    def create_scope(self) -> "IServiceScope":
        """
        Creates a new dependency scope.
        """
        ...


class IServiceScope(Protocol):
    """
    Represents a dependency injection scope.
    """

    @property
    def service_provider(self) -> IServiceProvider:
        """
        Returns the scoped provider.
        """
        ...

    def dispose(self) -> None:
        """
        Releases all scoped resources.
        """
        ...


class IServiceCollection(Protocol):
    """
    Service registration interface.
    """

    def add_singleton(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
    ) -> None:
        ...

    def add_scoped(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
    ) -> None:
        ...

    def add_transient(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
    ) -> None:
        ...

    def build_provider(self) -> IServiceProvider:
        """
        Builds the service provider.
        """
        ...