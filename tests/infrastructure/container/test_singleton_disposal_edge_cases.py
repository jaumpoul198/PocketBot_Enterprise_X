from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class DisposableInstance:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


class DisposableFactoryService:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


class NonDisposableService:
    pass


def test_registered_singleton_instance_is_disposed() -> None:
    services = ServiceCollection()

    instance = DisposableInstance()

    services.add_instance(
        DisposableInstance,
        instance,
    )

    provider = services.build_provider()

    resolved = provider.get_service(
        DisposableInstance
    )

    provider.dispose()

    assert resolved.dispose_calls == 1


def test_factory_created_singleton_is_disposed() -> None:
    services = ServiceCollection()

    services.add_singleton(
        DisposableFactoryService,
    )

    provider = services.build_provider()

    instance = provider.get_service(
        DisposableFactoryService
    )

    provider.dispose()

    assert instance.dispose_calls == 1


def test_non_disposable_singleton_does_not_fail_dispose() -> None:
    services = ServiceCollection()

    services.add_singleton(
        NonDisposableService,
    )

    provider = services.build_provider()

    provider.get_service(
        NonDisposableService,
    )

    provider.dispose()
