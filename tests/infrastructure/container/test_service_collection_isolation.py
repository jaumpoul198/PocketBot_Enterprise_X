from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class MutableService:
    def __init__(self) -> None:
        self.value = 1


def test_service_collection_iteration_exposes_isolated_instances() -> None:
    collection = ServiceCollection()

    collection.add_instance(
        MutableService,
        MutableService(),
    )

    descriptor = next(iter(collection))

    assert descriptor.implementation_instance is not None

    descriptor.implementation_instance.value = 999

    stored = next(iter(collection))

    assert stored.implementation_instance is not None
    assert stored.implementation_instance.value == 1
