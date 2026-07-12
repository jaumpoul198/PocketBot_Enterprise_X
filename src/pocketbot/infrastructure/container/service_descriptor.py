"""
PocketBot Enterprise X
Infrastructure Container

Service registration descriptor.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


from pocketbot.infrastructure.container.service_lifetime import (
    ServiceLifetime,
)

FactoryType = Callable[[Any], Any]


@dataclass(slots=True)
class ServiceDescriptor:
    """
    Describes a registered service.
    """

    service_type: type[Any]

    implementation_type: type[Any]

    lifetime: ServiceLifetime

    implementation_instance: Any | None = None

    implementation_factory: FactoryType | None = None

    @property
    def has_instance(self) -> bool:
        """
        Indicates whether the singleton instance already exists.
        """
        return self.implementation_instance is not None

    @property
    def has_factory(self) -> bool:
        """
        Indicates whether the descriptor uses a factory.
        """
        return self.implementation_factory is not None
