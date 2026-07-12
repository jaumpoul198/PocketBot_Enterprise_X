"""
PocketBot Enterprise X
Infrastructure Container

Dependency injection service provider.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from pocketbot.infrastructure.container.exceptions import (
    ServiceNotRegisteredError,
    ServiceResolutionError,
)
from pocketbot.infrastructure.container.interfaces import IServiceProvider
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
    Root dependency injection container.
    """

    def __init__(
        self,
        descriptors: dict[type[Any], ServiceDescriptor],
        scope: ServiceScope | None = None,
        singleton_cache: dict[type[Any], Any] | None = None,
    ) -> None:
        self._descriptors = descriptors
        self._resolver = ServiceResolver()

        if scope is None:
            scope = ServiceScope()

        self._scope = scope
        self._scope.attach_provider(self)

        if singleton_cache is None:
            singleton_cache = {}

        self._singleton_cache = singleton_cache
        self._disposed = False

    def create_scope(self) -> ServiceScope:
        """
        Creates a child scope sharing singleton instances.
        """
        scope = ServiceScope()

        provider = ServiceProvider(
            descriptors=self._descriptors,
            scope=scope,
            singleton_cache=self._singleton_cache,
        )

        scope.attach_provider(provider)

        return scope

    def get_service(
        self,
        service_type: type[Any],
    ) -> Any:
        """
        Resolves a registered service.
        """

        if self._disposed:
            raise ServiceResolutionError(
                "ServiceProvider has been disposed."
            )

        descriptor = self._descriptors.get(service_type)

        if descriptor is None:
            raise ServiceNotRegisteredError(
                f"Service '{service_type.__name__}' is not registered."
            )

        return self._resolve(descriptor)

    def _resolve(
        self,
        descriptor: ServiceDescriptor,
    ) -> Any:
        """
        Resolves a service according to its lifetime.
        """
        lifetime = descriptor.lifetime

        if lifetime is ServiceLifetime.SINGLETON:
            return self._resolve_singleton(descriptor)

        if lifetime is ServiceLifetime.SCOPED:
            return self._resolve_scoped(descriptor)

        if lifetime is ServiceLifetime.TRANSIENT:
            return self._create_instance(descriptor)

        raise ServiceResolutionError(
            f"Unsupported lifetime: {lifetime}"
        )

    def _resolve_singleton(
        self,
        descriptor: ServiceDescriptor,
    ) -> Any:
        """
        Resolves a singleton service.
        """
        service_type = descriptor.service_type

        if service_type in self._singleton_cache:
            return self._singleton_cache[service_type]

        instance = self._create_instance(descriptor)

        self._singleton_cache[service_type] = instance

        return instance

    def _resolve_scoped(
        self,
        descriptor: ServiceDescriptor,
    ) -> Any:
        """
        Resolves a scoped service.
        """
        service_type = descriptor.service_type

        cached = self._scope.get_instance(service_type)

        if cached is not None:
            return cached

        instance = self._create_instance(descriptor)

        self._scope.set_instance(
            service_type,
            instance,
        )

        return instance

    def _create_instance(
        self,
        descriptor: ServiceDescriptor,
    ) -> Any:
        """
        Creates a new service instance.
        """

        if descriptor.has_instance:
            instance = descriptor.implementation_instance

            if instance is None:
                raise ServiceResolutionError(
                    "Registered instance cannot be None."
                )

            return instance

        if descriptor.has_factory:
            factory = descriptor.implementation_factory

            if factory is None:
                raise ServiceResolutionError(
                    "Factory is not available."
                )

            try:
                return factory(self)

            except ServiceResolutionError:
                raise

            except Exception as exc:
                raise ServiceResolutionError(
                    f"Failed creating service '{descriptor.service_type.__name__}'"
                ) from exc

        implementation = descriptor.implementation_type

        return self._resolver.create_instance(
            implementation_type=implementation,
            provider=self,
        )

    def is_registered(
        self,
        service_type: type[Any],
    ) -> bool:
        """
        Returns True if a service has been registered.
        """
        return service_type in self._descriptors

    def get_descriptor(
        self,
        service_type: type[Any],
    ) -> ServiceDescriptor:
        """
        Returns the descriptor associated with a service.
        """
        descriptor = self._descriptors.get(service_type)

        if descriptor is None:
            raise ServiceNotRegisteredError(
                f"Service '{service_type.__name__}' is not registered."
            )

        return ServiceDescriptor(
            service_type=descriptor.service_type,
            implementation_type=descriptor.implementation_type,
            lifetime=descriptor.lifetime,
            implementation_instance=deepcopy(
                descriptor.implementation_instance,
            ),
            implementation_factory=descriptor.implementation_factory,
        )

    def dispose(self) -> None:
        """
        Releases provider resources.
        """

        if self._disposed:
            return

        self._disposed = True

        instances = tuple(
            self._singleton_cache.values()
        )

        self._singleton_cache.clear()

        for instance in instances:
            dispose = getattr(instance, "dispose", None)

            if callable(dispose):
                dispose()
