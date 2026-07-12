import pytest

from pocketbot.infrastructure.container.exceptions import ServiceNotRegisteredError
from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Database:
    pass


class Cache:
    pass


def test_provider_does_not_receive_late_registrations() -> None:
    services = ServiceCollection()

    services.add_singleton(Database)

    provider = services.build_provider()

    services.add_singleton(Cache)

    with pytest.raises(ServiceNotRegisteredError):
        provider.get_service(Cache)
