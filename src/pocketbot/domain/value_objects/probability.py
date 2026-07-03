from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Probability:
    """
    Representa uma probabilidade entre 0 e 1.
    """

    value: float

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 1:
            raise ValueError("Probabilidade deve estar entre 0 e 1.")

    @property
    def percentage(self) -> float:
        return self.value * 100

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.percentage:.2f}%"
