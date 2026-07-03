"""
PocketBot Enterprise X
Market Collector Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.entities.candle import Candle


class MarketCollector(ABC):
    """
    Responsável por coletar dados do provedor.
    """

    @abstractmethod
    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Coleta candles do mercado.
        """
        raise NotImplementedError
