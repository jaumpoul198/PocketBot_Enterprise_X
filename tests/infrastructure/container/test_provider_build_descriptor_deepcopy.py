from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_build_provider_does_not_share_descriptor_instance_between_providers() -> None:
    services = ServiceCollection()

    services.add_instance(Config, Config())

    provider_a = services.build_provider()
    provider_b = services.build_provider()

    descriptor_a = provider_a.get_descriptor(Config)
    descriptor_b = provider_b.get_descriptor(Config)

    assert descriptor_a is not None
    assert descriptor_b is not None

    descriptor_a.implementation_instance.value = 999

    assert descriptor_b.implementation_instance.value == 1
