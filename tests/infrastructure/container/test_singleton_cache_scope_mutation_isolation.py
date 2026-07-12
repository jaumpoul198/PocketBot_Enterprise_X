from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class SingletonService:
    pass


def test_scope_cannot_replace_root_singleton_cache_reference() -> None:
    services = ServiceCollection()

    services.add_singleton(SingletonService)

    provider = services.build_provider()

    root_instance = provider.get_service(SingletonService)

    scope = provider.create_scope()

    child_instance = scope.service_provider.get_service(
        SingletonService
    )

    assert child_instance is root_instance

    provider._singleton_cache[SingletonService] = object()  # type: ignore[attr-defined]

    assert scope.service_provider.get_service(
        SingletonService
    ) is not root_instance
