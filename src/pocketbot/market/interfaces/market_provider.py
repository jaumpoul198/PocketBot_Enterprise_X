"""
PocketBot Enterprise X
Market Provider Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.candle import Candle


class MarketProvider(ABC):
    """
    Interface base para qualquer provedor de mercado.
    """

    @abstractmethod
    def connect(self) -> None:
        """
        Estabelece conexão com a corretora.
        """
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        """
        Encerra conexão.
        """
        raise NotImplementedError

    @abstractmethod
    def is_connected(self) -> bool:
        """
        Retorna True caso esteja conectado.
        """
        raise NotImplementedError

    @abstractmethod
    def get_candles(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Retorna candles já convertidos para o domínio.
        """
        raise NotImplementedError
