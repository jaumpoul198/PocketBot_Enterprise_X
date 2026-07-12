from __future__ import annotations

from pocketbot.infrastructure.container.service_scope import (
    ServiceScope,
)


class MutableService:
    def __init__(self) -> None:
        self.value = 1


def test_scope_instances_cache_isolated() -> None:
    scope = ServiceScope()

    service = MutableService()

    scope.set_instance(
        MutableService,
        service,
    )

    cached = scope.get_instance(MutableService)

    assert cached is not None

    cached.value = 999

    stored = scope.get_instance(MutableService)

    assert stored is not None
    assert stored.value == 999
