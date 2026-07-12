import pytest

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Database:
    pass


def test_scope_cannot_attach_different_provider() -> None:
    services = ServiceCollection()

    services.add_scoped(Database)

    provider = services.build_provider()

    scope = provider.create_scope()

    another_provider = services.build_provider()

    with pytest.raises(RuntimeError):
        scope.attach_provider(another_provider)
