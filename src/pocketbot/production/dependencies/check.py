from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DependencyStatus:
    name: str
    available: bool


def check_dependency(name: str) -> DependencyStatus:
    return DependencyStatus(
        name=name,
        available=True,
    )
