from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Config:
    def __init__(self) -> None:
        self.value = 1


def test_scope_factory_descriptor_mutation_does_not_affect_root() -> None:
    services = ServiceCollection()

    services.add_scoped(
        Config,
        factory=lambda _: Config(),
    )

    provider = services.build_provider()

    scope = provider.create_scope()

    root_descriptor = provider.get_descriptor(Config)
    scoped_descriptor = scope.service_provider.get_descriptor(Config)

    assert root_descriptor is not None
    assert scoped_descriptor is not None

    scoped_descriptor.implementation_factory = None

    assert root_descriptor.implementation_factory is not None
