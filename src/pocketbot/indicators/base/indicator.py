"""
PocketBot Enterprise X

Base interface for every technical indicator.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence

from pocketbot.domain.candle import Candle
from pocketbot.indicators.base.result import IndicatorResult


class Indicator(ABC):
    """
    Base contract implemented by every indicator.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Indicator name.
        """
        raise NotImplementedError

    @abstractmethod
    def calculate(
        self,
        candles: Sequence[Candle],
    ) -> IndicatorResult:
        """
        Calculates the indicator result.
        """
        raise NotImplementedError
