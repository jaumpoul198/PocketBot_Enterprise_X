from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class SingletonService:
    pass


def test_singleton_cache_is_not_shared_between_independent_providers() -> None:
    services = ServiceCollection()

    services.add_singleton(SingletonService)

    provider_a = services.build_provider()
    provider_b = services.build_provider()

    instance_a = provider_a.get_service(SingletonService)
    instance_b = provider_b.get_service(SingletonService)

    assert instance_a is not instance_b
