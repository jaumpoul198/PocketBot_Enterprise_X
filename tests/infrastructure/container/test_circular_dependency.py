from __future__ import annotations

import pytest

from pocketbot.infrastructure.container.exceptions import (
    CircularDependencyError,
)
from pocketbot.infrastructure.container.service_collection import ServiceCollection


class A:
    def __init__(self, b: B) -> None:
        self.b = b


class B:
    def __init__(self, a: A) -> None:
        self.a = a


def test_circular_dependency_detection() -> None:
    services = ServiceCollection()

    services.add_transient(A)
    services.add_transient(B)

    provider = services.build_provider()

    with pytest.raises(CircularDependencyError):
        provider.get_service(A)