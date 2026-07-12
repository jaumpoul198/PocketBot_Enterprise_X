from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class DisposableSingleton:
    def __init__(self) -> None:
        self.dispose_calls = 0

    def dispose(self) -> None:
        self.dispose_calls += 1


def test_provider_disposes_singleton_instances() -> None:
    services = ServiceCollection()

    services.add_singleton(DisposableSingleton)

    provider = services.build_provider()

    instance = provider.get_service(
        DisposableSingleton
    )

    provider.dispose()

    assert instance.dispose_calls == 1
