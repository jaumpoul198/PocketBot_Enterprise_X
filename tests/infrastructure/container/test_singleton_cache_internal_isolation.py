from __future__ import annotations

import pytest

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class MutableSingleton:
    pass


def test_provider_does_not_expose_singleton_cache_attribute() -> None:
    services = ServiceCollection()

    services.add_singleton(MutableSingleton)

    provider = services.build_provider()

    with pytest.raises(AttributeError):
        _ = provider.singleton_cache
