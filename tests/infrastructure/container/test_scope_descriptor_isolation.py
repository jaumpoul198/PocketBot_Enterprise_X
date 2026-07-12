from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_child_scope_cannot_mutate_root_descriptor() -> None:
    services = ServiceCollection()

    services.add_instance(Config, Config())

    provider = services.build_provider()

    scope = provider.create_scope()

    scoped_provider = scope.service_provider

    descriptor = scoped_provider.get_descriptor(Config)

    assert descriptor is not None

    descriptor.implementation_instance.value = 999

    root_descriptor = provider.get_descriptor(Config)

    assert root_descriptor.implementation_instance.value == 1
