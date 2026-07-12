import pytest

from pocketbot.infrastructure.container.exceptions import ScopeDisposedError
from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Database:
    pass


def test_scope_dispose() -> None:
    services = ServiceCollection()

    services.add_scoped(Database)

    provider = services.build_provider()

    scope = provider.create_scope()

    scope.dispose()

    with pytest.raises(ScopeDisposedError):
        _ = scope.service_provider
