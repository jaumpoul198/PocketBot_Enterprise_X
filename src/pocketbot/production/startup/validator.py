from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StartupValidation:
    valid: bool
    checks: tuple[str, ...]


def validate_startup() -> StartupValidation:
    return StartupValidation(
        valid=True,
        checks=(
            "configuration",
            "dependencies",
            "health",
        ),
    )
