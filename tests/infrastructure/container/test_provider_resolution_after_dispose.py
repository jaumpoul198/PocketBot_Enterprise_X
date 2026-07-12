from __future__ import annotations

import pytest

from pocketbot.infrastructure.container.exceptions import (
    ServiceResolutionError,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Service:
    pass


def test_provider_cannot_resolve_after_dispose() -> None:
    services = ServiceCollection()

    services.add_singleton(Service)

    provider = services.build_provider()

    provider.dispose()

    with pytest.raises(ServiceResolutionError):
        provider.get_service(Service)
