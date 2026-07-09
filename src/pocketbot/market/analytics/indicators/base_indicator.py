"""
PocketBot Enterprise X
Base Indicator Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.candle import Candle


class BaseIndicator(ABC):
    """
    Contrato base para indicadores de mercado.
    """

    @abstractmethod
    def calculate(
        self,
        candles: list[Candle],
    ) -> float | None:
        """
        Calcula o valor do indicador.
        """

        raise NotImplementedError
