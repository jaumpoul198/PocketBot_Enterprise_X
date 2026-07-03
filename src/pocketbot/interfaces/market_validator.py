"""
PocketBot Enterprise X
Market Validator Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.entities.candle import Candle


class MarketValidator(ABC):
    """
    Valida candles antes de serem utilizados.
    """

    @abstractmethod
    def validate(
        self,
        candles: list[Candle],
    ) -> bool:
        raise NotImplementedError
