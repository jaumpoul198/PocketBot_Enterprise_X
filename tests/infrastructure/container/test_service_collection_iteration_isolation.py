from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_collection_iteration_does_not_expose_internal_descriptor_state() -> None:
    services = ServiceCollection()

    services.add_instance(Config, Config())

    descriptor = next(iter(services))

    descriptor.implementation_instance.value = 999

    descriptor_again = next(iter(services))

    assert descriptor_again.implementation_instance.value == 1
