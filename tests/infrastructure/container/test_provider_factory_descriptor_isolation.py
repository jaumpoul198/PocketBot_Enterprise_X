from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    pass


def test_provider_factory_descriptor_isolation_between_builds() -> None:
    services = ServiceCollection()

    services.add_singleton(
        Config,
        factory=lambda _: Config(),
    )

    provider_a = services.build_provider()
    provider_b = services.build_provider()

    descriptor_a = provider_a.get_descriptor(Config)
    descriptor_b = provider_b.get_descriptor(Config)

    assert descriptor_a is not None
    assert descriptor_b is not None

    descriptor_a.implementation_factory = None

    assert descriptor_b.implementation_factory is not None
