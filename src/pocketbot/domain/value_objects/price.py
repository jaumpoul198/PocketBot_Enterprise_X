from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Price:
    """
    Represents a market price.
    """

    value: float

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError("Price must be greater than zero.")

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:.5f}"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Price):
            return NotImplemented
        return self.value < other.value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Price):
            return NotImplemented
        return self.value <= other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Price):
            return NotImplemented
        return self.value > other.value

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Price):
            return NotImplemented
        return self.value >= other.value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Price):
            return NotImplemented
        return self.value == other.value
