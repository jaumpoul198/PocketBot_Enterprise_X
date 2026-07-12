from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_provider_descriptor_instance_is_isolated_from_registered_instance() -> None:
    services = ServiceCollection()

    config = Config()

    services.add_instance(Config, config)

    provider = services.build_provider()

    descriptor = provider.get_descriptor(Config)

    assert descriptor is not None

    descriptor.implementation_instance.value = 999

    assert config.value == 1


def test_provider_descriptor_mutation_does_not_change_collection_registration() -> None:
    services = ServiceCollection()

    config = Config()

    services.add_instance(Config, config)

    provider = services.build_provider()

    descriptor = provider.get_descriptor(Config)

    assert descriptor is not None

    descriptor.implementation_instance.value = 999

    provider_again = services.build_provider()

    descriptor_again = provider_again.get_descriptor(Config)

    assert descriptor_again is not None
    assert descriptor_again.implementation_instance.value == 1
