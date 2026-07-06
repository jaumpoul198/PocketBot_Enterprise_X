"""
PocketBot Enterprise X
Infrastructure Container

Enterprise service provider.
"""

from __future__ import annotations

from typing import Any

from pocketbot.infrastructure.container.exceptions import (
    ServiceNotRegisteredError,
)
from pocketbot.infrastructure.container.interfaces import (
    IServiceProvider,
)
from pocketbot.infrastructure.container.service_descriptor import (
    ServiceDescriptor,
)
from pocketbot.infrastructure.container.service_lifetime import (
    ServiceLifetime,
)
from pocketbot.infrastructure.container.service_resolver import (
    ServiceResolver,
)
from pocketbot.infrastructure.container.service_scope import (
    ServiceScope,
)


class ServiceProvider(IServiceProvider):
    """
    Enterprise dependency injection service provider.
    """

    def __init__(
        self,
        descriptors: dict[type[Any], ServiceDescriptor],
    ) -> None:
        self._descriptors = descriptors
        self._resolver = ServiceResolver()
        self._scope: ServiceScope | None = None

    @property
    def descriptors(
        self,
    ) -> dict[type[Any], ServiceDescriptor]:
        """
        Returns all registered service descriptors.
        """
        return self._descriptors

    @property
    def is_root(self) -> bool:
        """
        Indicates whether this is the root provider.
        """
        return self._scope is None

    def create_scope(self) -> ServiceScope:
        """
        Creates a dependency injection scope.
        """
        scope = ServiceScope()

        scope.attach_provider(self)

        return scope

    def get_service(
        self,
        service_type: type[Any],
    ) -> Any:
        """
        Resolves a registered service.
        """

        descriptor = self._descriptors.get(service_type)

        if descriptor is None:
            raise ServiceNotRegisteredError(
                f"Service '{service_type.__name__}' is not registered."
            )

        if descriptor.has_factory:
            factory = descriptor.implementation_factory

            if factory is None:
                raise RuntimeError(
                    "Service factory is not configured."
                )

            instance = factory(self)

            if descriptor.has_instance:
                descriptor.implementation_instance = instance

            return instance

        if descriptor.has_instance:
            return descriptor.implementation_instance

        instance = self._resolver.create_instance(
            descriptor.implementation_type,
            self,
        )

        descriptor.implementation_instance = instance

        return instance