from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Score:
    """
    Representa um score entre 0 e 100.
    """

    value: float

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 100:
            raise ValueError("Score deve estar entre 0 e 100.")

    @property
    def low(self) -> bool:
        return self.value < 40

    @property
    def medium(self) -> bool:
        return 40 <= self.value < 70

    @property
    def high(self) -> bool:
        return self.value >= 70

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:.2f}"
