"""
PocketBot Enterprise X
Market Normalizer Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.domain.entities.candle import Candle


class MarketNormalizer(ABC):
    """
    Converte dados da corretora para entidades do domínio.
    """

    @abstractmethod
    def normalize(
        self,
        raw_data: list[dict],
    ) -> list[Candle]:
        raise NotImplementedError
