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
    Representa o resultado padronizado de uma operação.
    """

    success: bool
    data: T | None = None
    message: str = ""

    @property
    def failed(self) -> bool:
        return not self.success

    @classmethod
    def ok(cls, data: T | None = None, message: str = "") -> "Result[T]":
        return cls(
            success=True,
            data=data,
            message=message,
        )

    @classmethod
    def fail(cls, message: str) -> "Result[T]":
        return cls(
            success=False,
            data=None,
            message=message,
        )