from __future__ import annotations

from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Dependency:
    pass


class ServiceA:
    def __init__(self, dependency: Dependency) -> None:
        self.dependency = dependency


def test_provider_resolvers_do_not_share_resolution_state() -> None:
    services = ServiceCollection()

    services.add_transient(ServiceA)
    services.add_transient(Dependency)

    provider_a = services.build_provider()
    provider_b = services.build_provider()

    instance_a = provider_a.get_service(ServiceA)
    instance_b = provider_b.get_service(ServiceA)

    assert instance_a is not instance_b
    assert instance_a.dependency is not instance_b.dependency
