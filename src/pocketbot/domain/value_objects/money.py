from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Money:
    """
    Representa um valor monetário.
    """

    value: float

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Valor monetário não pode ser negativo.")

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:.2f}"
