from __future__ import annotations

import pytest

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Database:
    pass


def test_provider_does_not_expose_internal_scope_attribute() -> None:
    services = ServiceCollection()

    services.add_scoped(Database)

    provider = services.build_provider()

    with pytest.raises(AttributeError):
        _ = provider.scope
