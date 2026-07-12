from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class MutableService:
    def __init__(self) -> None:
        self.value = 1


def test_descriptor_instance_isolated_from_collection_state() -> None:
    collection = ServiceCollection()

    instance = MutableService()

    collection.add_instance(
        MutableService,
        instance,
    )

    descriptors = collection.descriptors

    descriptor = descriptors[MutableService]

    assert descriptor.implementation_instance is not None

    descriptor.implementation_instance.value = 999

    stored = collection.descriptors[MutableService]

    assert stored.implementation_instance is not None
    assert stored.implementation_instance.value == 1
