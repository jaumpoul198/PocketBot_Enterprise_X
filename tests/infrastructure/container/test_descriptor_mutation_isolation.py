from pocketbot.infrastructure.container.service_collection import ServiceCollection
from pocketbot.infrastructure.container.service_lifetime import ServiceLifetime


class Database:
    pass


def test_provider_descriptor_state_is_isolated() -> None:
    services = ServiceCollection()

    services.add_singleton(Database)

    provider = services.build_provider()

    services.descriptors[Database].lifetime = ServiceLifetime.TRANSIENT

    first = provider.get_service(Database)
    second = provider.get_service(Database)

    assert first is second
