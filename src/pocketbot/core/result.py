"""
PocketBot Enterprise X
Core - Result Pattern
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Result(Generic[T]):
    """
    Representa o resultado de uma operação.
    """

    success: bool
    value: T | None = None
    error: str | None = None

    @classmethod
    def ok(cls, value: T | None = None) -> Result[T]:
        return cls(
            success=True,
            value=value,
            error=None,
        )

    @classmethod
    def fail(cls, error: str) -> Result[T]:
        return cls(
            success=False,
            value=None,
            error=error,
        )

    @property
    def is_success(self) -> bool:
        return self.success

    @property
    def is_failure(self) -> bool:
        return not self.success
