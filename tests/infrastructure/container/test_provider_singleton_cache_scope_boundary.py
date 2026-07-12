from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class MutableSingleton:
    pass


def test_child_scopes_share_singleton_instances_only_within_provider_tree() -> None:
    services = ServiceCollection()

    services.add_singleton(MutableSingleton)

    provider = services.build_provider()

    scope1 = provider.create_scope()
    scope2 = provider.create_scope()

    first = scope1.service_provider.get_service(MutableSingleton)
    second = scope2.service_provider.get_service(MutableSingleton)

    assert first is second
