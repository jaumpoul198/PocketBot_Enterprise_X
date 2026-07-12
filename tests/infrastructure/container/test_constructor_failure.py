import pytest

from pocketbot.infrastructure.container.exceptions import (
    ServiceResolutionError,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)


class BrokenService:
    def __init__(self) -> None:
        raise RuntimeError("constructor failed")


def test_constructor_failure_is_wrapped_as_resolution_error() -> None:
    services = ServiceCollection()

    services.add_transient(BrokenService)

    provider = services.build_provider()

    with pytest.raises(ServiceResolutionError):
        provider.get_service(BrokenService)
