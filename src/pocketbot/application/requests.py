"""
PocketBot Enterprise X

Application request models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TradingRequest:
    """
    Request used by trading application flow.
    """

    asset: str
    timeframe: int

    def __post_init__(self) -> None:
        """
        Validate request contract.
        """

        if not isinstance(self.asset, str):
            raise TypeError(
                "asset must be a string",
            )

        if not self.asset.strip():
            raise ValueError(
                "asset cannot be empty",
            )

        if isinstance(self.timeframe, bool):
            raise TypeError(
                "timeframe cannot be boolean",
            )

        if not isinstance(self.timeframe, int):
            raise TypeError(
                "timeframe must be int",
            )

        if self.timeframe <= 0:
            raise ValueError(
                "timeframe must be greater than zero",
            )