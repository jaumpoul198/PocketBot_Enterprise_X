from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.infrastructure.container.service_lifetime import (
    ServiceLifetime,
)


class Database:
    pass


def test_service_collection_iteration_exposes_isolated_descriptors() -> None:
    services = ServiceCollection()

    services.add_singleton(Database)

    descriptor = next(iter(services))

    descriptor.lifetime = ServiceLifetime.TRANSIENT

    stored = next(iter(services))

    assert stored.lifetime is ServiceLifetime.SINGLETON
