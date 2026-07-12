import pytest

from pocketbot.infrastructure.container.exceptions import (
    ServiceRegistrationError,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class Logger:
    pass


def test_factory_and_implementation_type_cannot_be_combined() -> None:
    services = ServiceCollection()

    with pytest.raises(ServiceRegistrationError):
        services.add_singleton(
            Logger,
            Logger,
            factory=lambda provider: Logger(),
        )
