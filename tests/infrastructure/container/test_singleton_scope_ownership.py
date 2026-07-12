from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class DisposableSingleton:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


def test_singleton_shared_between_scopes_disposed_once() -> None:
    services = ServiceCollection()

    services.add_singleton(DisposableSingleton)

    provider = services.build_provider()

    scope_a = provider.create_scope()
    scope_b = provider.create_scope()

    instance_a = scope_a.service_provider.get_service(
        DisposableSingleton
    )

    instance_b = scope_b.service_provider.get_service(
        DisposableSingleton
    )

    assert instance_a is instance_b

    provider.dispose()

    assert instance_a.dispose_calls == 1
