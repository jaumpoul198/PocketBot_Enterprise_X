from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Price:
    """
    Representa um preço.
    """

    value: float

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError("Preço deve ser maior que zero.")

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:.5f}"
