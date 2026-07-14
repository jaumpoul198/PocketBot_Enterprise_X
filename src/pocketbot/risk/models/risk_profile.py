"""
PocketBot Enterprise X

Risk profile models.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True, slots=True)
class RiskProfile:
    """
    Defines trading risk parameters.

    This model represents the limits that control
    how much exposure a trading operation can assume.
    """

    max_position_size: float
    max_loss_percentage: float
    max_exposure_percentage: float

    def __post_init__(self) -> None:
        """
        Validate risk constraints.
        """

        values = (
            (
                "max_position_size",
                self.max_position_size,
            ),
            (
                "max_loss_percentage",
                self.max_loss_percentage,
            ),
            (
                "max_exposure_percentage",
                self.max_exposure_percentage,
            ),
        )

        for name, value in values:
            if isinstance(value, bool):
                raise TypeError(
                    f"{name} cannot be boolean"
                )

            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"{name} must be numeric"
                )

            numeric_value = float(value)

            if not math.isfinite(numeric_value):
                raise ValueError(
                    f"{name} must be finite"
                )

        if self.max_position_size <= 0:
            raise ValueError(
                "Maximum position size must be positive."
            )

        if not 0 < self.max_loss_percentage <= 100:
            raise ValueError(
                "Maximum loss percentage must be between 0 and 100."
            )

        if not 0 < self.max_exposure_percentage <= 100:
            raise ValueError(
                "Maximum exposure percentage must be between 0 and 100."
            )