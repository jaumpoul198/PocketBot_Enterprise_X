from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class DisposableScoped:
    def __init__(self) -> None:
        self.disposed = False

    def dispose(self) -> None:
        self.disposed = True


def test_scope_disposes_scoped_instances() -> None:
    services = ServiceCollection()

    services.add_scoped(DisposableScoped)

    provider = services.build_provider()

    scope = provider.create_scope()

    instance = scope.service_provider.get_service(
        DisposableScoped
    )

    scope.dispose()

    assert instance.disposed is True
