from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Database:
    pass


def test_scoped_returns_same_instance_inside_scope() -> None:
    services = ServiceCollection()

    services.add_scoped(Database)

    provider = services.build_provider()

    scope = provider.create_scope()

    first = scope.service_provider.get_service(Database)
    second = scope.service_provider.get_service(Database)

    assert first is second


def test_scoped_returns_different_instances_between_scopes() -> None:
    services = ServiceCollection()

    services.add_scoped(Database)

    provider = services.build_provider()

    scope1 = provider.create_scope()
    scope2 = provider.create_scope()

    first = scope1.service_provider.get_service(Database)
    second = scope2.service_provider.get_service(Database)

    assert first is not second