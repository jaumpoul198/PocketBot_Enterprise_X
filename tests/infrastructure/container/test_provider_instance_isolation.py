from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_provider_descriptor_instance_snapshot_isolated() -> None:
    services = ServiceCollection()

    services.add_instance(
        Config,
        Config(),
    )

    provider = services.build_provider()

    descriptor = provider.get_descriptor(Config)

    assert descriptor.implementation_instance is not None

    descriptor.implementation_instance.value = 999

    stored = provider.get_descriptor(Config)

    assert stored.implementation_instance is not None
    assert stored.implementation_instance.value == 1
