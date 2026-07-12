from __future__ import annotations

from pocketbot.infrastructure.container.service_resolver import (
    ServiceResolver,
)


class Dependency:
    pass


class Service:
    def __init__(self, dependency: Dependency) -> None:
        self.dependency = dependency


class CircularA:
    def __init__(self, b: "CircularB") -> None:
        self.b = b


class CircularB:
    def __init__(self, a: CircularA) -> None:
        self.a = a


class Provider:
    def get_service(self, service_type: type[object]) -> object:
        if service_type is Dependency:
            return Dependency()

        raise RuntimeError


def test_resolver_stack_is_empty_after_successful_resolution() -> None:
    resolver = ServiceResolver()

    resolver.create_instance(
        Service,
        Provider(),
    )

    assert resolver._resolution_stack == []


def test_resolver_stack_is_empty_after_failed_resolution() -> None:
    resolver = ServiceResolver()

    try:
        resolver.create_instance(
            CircularA,
            Provider(),
        )
    except Exception:
        pass

    assert resolver._resolution_stack == []
