from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class ScopedService:
    def __init__(self) -> None:
        self.value = 1


def test_scope_does_not_expose_internal_instance_cache() -> None:
    services = ServiceCollection()

    services.add_scoped(
        ScopedService,
        ScopedService,
    )

    provider = services.build_provider()

    scope = provider.create_scope()

    first = scope.service_provider.get_service(ScopedService)

    first.value = 999

    second = scope.service_provider.get_service(ScopedService)

    assert first is second
    assert second.value == 999
