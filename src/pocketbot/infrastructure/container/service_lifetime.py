"""
PocketBot Enterprise X
Infrastructure Container

Defines the lifetime of registered services.
"""

from __future__ import annotations

from enum import StrEnum


class ServiceLifetime(StrEnum):
    """
    Defines how long an instance should live.

    SINGLETON
        One instance shared by the entire application.

    SCOPED
        One instance per scope.

    TRANSIENT
        A new instance every resolution.
    """

    SINGLETON = "singleton"
    SCOPED = "scoped"
    TRANSIENT = "transient"