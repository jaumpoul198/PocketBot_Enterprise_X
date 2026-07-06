"""
PocketBot Enterprise X
Infrastructure Container

Service collection implementation.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from pocketbot.infrastructure.container.interfaces import (
    IServiceCollection,
    IServiceProvider,
)
from pocketbot.infrastructure.container.service_descriptor import (
    ServiceDescriptor,
)
from pocketbot.infrastructure.container.service_lifetime import (
    ServiceLifetime,
)


class ServiceCollection(IServiceCollection):
    """
    Stores service registrations.
    """

    def __init__(self) -> None:
        self._descriptors: dict[type[Any], ServiceDescriptor] = {}

    def __iter__(self) -> Iterator[ServiceDescriptor]:
        return iter(self._descriptors.values())

    def __len__(self) -> int:
        return len(self._descriptors)

    @property
    def descriptors(self) -> dict[type[Any], ServiceDescriptor]:
        """
        Returns all registered descriptors.
        """
        return self._descriptors

    def add_singleton(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
    ) -> None:
        self._add(
            service_type,
            implementation_type,
            ServiceLifetime.SINGLETON,
        )

    def add_scoped(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
    ) -> None:
        self._add(
            service_type,
            implementation_type,
            ServiceLifetime.SCOPED,
        )

    def add_transient(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
    ) -> None:
        self._add(
            service_type,
            implementation_type,
            ServiceLifetime.TRANSIENT,
        )

    def _add(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None,
        lifetime: ServiceLifetime,
    ) -> None:
        implementation = implementation_type or service_type

        self._descriptors[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation,
            lifetime=lifetime,
        )

    def build_provider(self) -> IServiceProvider:
        """
        Builds the root service provider.
        """
        from pocketbot.infrastructure.container.service_provider import (
            ServiceProvider,
        )

        return ServiceProvider(self._descriptors)