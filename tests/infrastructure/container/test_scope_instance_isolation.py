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

    scope.instances[MutableService] = service

    cached = scope.instances

    cached[MutableService].value = 999

    assert scope.instances[MutableService].value == 999
