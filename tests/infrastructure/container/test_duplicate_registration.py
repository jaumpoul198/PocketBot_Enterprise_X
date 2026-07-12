import pytest

from pocketbot.infrastructure.container.exceptions import ServiceRegistrationError
from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Database:
    pass


def test_duplicate_service_registration_is_rejected() -> None:
    services = ServiceCollection()

    services.add_singleton(Database)

    with pytest.raises(ServiceRegistrationError):
        services.add_scoped(Database)
