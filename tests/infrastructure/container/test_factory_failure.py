from __future__ import annotations

import pytest

from pocketbot.infrastructure.container.exceptions import (
    ServiceResolutionError,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class BrokenService:
    pass


def broken_factory(provider) -> BrokenService:
    raise RuntimeError("factory failure")


def test_factory_failure_is_wrapped_as_resolution_error() -> None:
    services = ServiceCollection()

    services.add_transient(
        BrokenService,
        factory=broken_factory,
    )

    provider = services.build_provider()

    with pytest.raises(ServiceResolutionError):
        provider.get_service(BrokenService)
