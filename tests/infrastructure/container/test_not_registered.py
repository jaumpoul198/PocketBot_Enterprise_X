import pytest

from pocketbot.infrastructure.container.exceptions import (
    ServiceNotRegisteredError,
)
from pocketbot.infrastructure.container.service_collection import ServiceCollection


class Logger:
    pass


def test_service_not_registered() -> None:
    provider = ServiceCollection().build_provider()

    with pytest.raises(ServiceNotRegisteredError):
        provider.get_service(Logger)