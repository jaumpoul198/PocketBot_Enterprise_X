from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_child_provider_descriptor_reference_is_isolated() -> None:
    services = ServiceCollection()

    services.add_instance(Config, Config())

    provider = services.build_provider()

    scope = provider.create_scope()

    child_provider = scope.service_provider

    parent_descriptor = provider.get_descriptor(Config)
    child_descriptor = child_provider.get_descriptor(Config)

    assert parent_descriptor is not None
    assert child_descriptor is not None

    child_descriptor.implementation_instance.value = 999

    assert parent_descriptor.implementation_instance.value == 1
