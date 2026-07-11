"""
PocketBot Enterprise X
Base Indicator Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pocketbot.domain.candle import Candle


T = TypeVar("T")


class BaseIndicator(ABC, Generic[T]):
    """
    Contrato base genérico para indicadores de mercado.
    """

    @abstractmethod
    def calculate(
        self,
        candles: list[Candle],
    ) -> T | None:
        """
        Calcula o valor do indicador.
        """

        raise NotImplementedError
