"""
PocketBot Enterprise X

Market Filter Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.candle import Candle


class MarketFilter(ABC):
    """
    Interface para filtros de mercado.
    """

    @abstractmethod
    def apply(
        self,
        candles: list[Candle],
    ) -> list[Candle]:
        raise NotImplementedError
