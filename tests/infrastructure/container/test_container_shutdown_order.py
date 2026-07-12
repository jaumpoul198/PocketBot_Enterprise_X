from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class DisposableSingleton:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


class DisposableScoped:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


def test_provider_dispose_does_not_dispose_scoped_instances() -> None:
    services = ServiceCollection()

    services.add_singleton(DisposableSingleton)
    services.add_scoped(DisposableScoped)

    provider = services.build_provider()

    scope = provider.create_scope()

    singleton = provider.get_service(
        DisposableSingleton
    )

    scoped = scope.service_provider.get_service(
        DisposableScoped
    )

    provider.dispose()

    assert singleton.dispose_calls == 1
    assert scoped.dispose_calls == 0


def test_scope_dispose_after_provider_dispose_is_safe() -> None:
    services = ServiceCollection()

    services.add_scoped(DisposableScoped)

    provider = services.build_provider()

    scope = provider.create_scope()

    scoped = scope.service_provider.get_service(
        DisposableScoped
    )

    provider.dispose()

    scope.dispose()

    assert scoped.dispose_calls == 1
