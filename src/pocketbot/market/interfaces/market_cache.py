"""
PocketBot Enterprise X
Market Cache Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.candle import Candle


class MarketCache(ABC):
    """
    Interface de cache do mercado.
    """

    @abstractmethod
    def save(
        self,
        asset: str,
        timeframe: int,
        candles: list[Candle],
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(
        self,
        asset: str,
        timeframe: int,
    ) -> list[Candle]:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError
