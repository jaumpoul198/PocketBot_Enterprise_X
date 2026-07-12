from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class MutableSingleton:
    def __init__(self) -> None:
        self.value = 1


def test_child_scope_shares_singleton_cache() -> None:
    services = ServiceCollection()

    services.add_singleton(MutableSingleton)

    provider = services.build_provider()

    scope = provider.create_scope()

    child_provider = scope.service_provider

    first = provider.get_service(MutableSingleton)
    second = child_provider.get_service(MutableSingleton)

    assert first is second


def test_child_scope_does_not_mutate_descriptor_collection() -> None:
    services = ServiceCollection()

    services.add_singleton(MutableSingleton)

    provider = services.build_provider()

    child_scope = provider.create_scope()
    child_provider = child_scope.service_provider

    assert child_provider.is_registered(MutableSingleton)
    assert provider.is_registered(MutableSingleton)
