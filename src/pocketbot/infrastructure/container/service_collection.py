"""
PocketBot Enterprise X
Infrastructure Container

Service collection implementation.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any

from pocketbot.infrastructure.container.exceptions import (
    ServiceRegistrationError,
)
from pocketbot.infrastructure.container.interfaces import (
    IServiceCollection,
    IServiceProvider,
)
from pocketbot.infrastructure.container.service_descriptor import (
    FactoryType,
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
        return iter(
            ServiceDescriptor(
                service_type=descriptor.service_type,
                implementation_type=descriptor.implementation_type,
                lifetime=descriptor.lifetime,
                implementation_instance=descriptor.implementation_instance,
                implementation_factory=descriptor.implementation_factory,
            )
            for descriptor in self._descriptors.values()
        )

    def __len__(self) -> int:
        return len(self._descriptors)

    @property
    def descriptors(self) -> dict[type[Any], ServiceDescriptor]:
        """
        Returns isolated registered descriptors.
        """
        return {
            service_type: ServiceDescriptor(
                service_type=descriptor.service_type,
                implementation_type=descriptor.implementation_type,
                lifetime=descriptor.lifetime,
                implementation_instance=descriptor.implementation_instance,
                implementation_factory=descriptor.implementation_factory,
            )
            for service_type, descriptor in self._descriptors.items()
        }

    def add_singleton(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
        *,
        factory: FactoryType | None = None,
    ) -> None:
        self._add(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=ServiceLifetime.SINGLETON,
            factory=factory,
        )

    def add_scoped(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
        *,
        factory: FactoryType | None = None,
    ) -> None:
        self._add(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=ServiceLifetime.SCOPED,
            factory=factory,
        )

    def add_transient(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None = None,
        *,
        factory: FactoryType | None = None,
    ) -> None:
        self._add(
            service_type=service_type,
            implementation_type=implementation_type,
            lifetime=ServiceLifetime.TRANSIENT,
            factory=factory,
        )

    def add_instance(
        self,
        service_type: type[Any],
        instance: Any,
    ) -> None:
        """
        Registers an existing singleton instance.
        """
        self._descriptors[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation_type=type(instance),
            lifetime=ServiceLifetime.SINGLETON,
            implementation_instance=instance,
        )

    def _add(
        self,
        service_type: type[Any],
        implementation_type: type[Any] | None,
        lifetime: ServiceLifetime,
        *,
        factory: FactoryType | None = None,
    ) -> None:
        if service_type in self._descriptors:
            raise ServiceRegistrationError(
                f"Service '{service_type.__name__}' is already registered."
            )

        if factory is not None and implementation_type is not None:
            raise ServiceRegistrationError(
                "Factory and implementation type cannot be registered together."
            )

        if factory is None and implementation_type is None:
            implementation_type = service_type

        implementation = implementation_type or service_type

        self._descriptors[service_type] = ServiceDescriptor(
            service_type=service_type,
            implementation_type=implementation,
            lifetime=lifetime,
            implementation_factory=factory,
        )

    def build_provider(self) -> IServiceProvider:
        """
        Builds the root service provider.
        """
        from pocketbot.infrastructure.container.service_provider import (
            ServiceProvider,
        )

        descriptors = {
            service_type: ServiceDescriptor(
                service_type=descriptor.service_type,
                implementation_type=descriptor.implementation_type,
                lifetime=descriptor.lifetime,
                implementation_instance=descriptor.implementation_instance,
                implementation_factory=descriptor.implementation_factory,
            )
            for service_type, descriptor in self._descriptors.items()
        }

        return ServiceProvider(descriptors)