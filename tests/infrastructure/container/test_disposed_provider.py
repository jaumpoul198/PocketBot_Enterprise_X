import pytest

from pocketbot.infrastructure.container.exceptions import ScopeDisposedError
from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Database:
    pass


def test_provider_cannot_resolve_after_scope_dispose() -> None:
    services = ServiceCollection()

    services.add_scoped(Database)

    provider = services.build_provider()

    scope = provider.create_scope()

    scoped_provider = scope.service_provider

    scope.dispose()

    with pytest.raises(ScopeDisposedError):
        scoped_provider.get_service(Database)
