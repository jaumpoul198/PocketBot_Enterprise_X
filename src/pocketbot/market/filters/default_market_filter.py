"""
PocketBot Enterprise X

Default Market Filter
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_filter import MarketFilter


class DefaultMarketFilter(MarketFilter):
    """
    Filtro padrão de mercado.

    Remove candles inválidos.
    """


    def apply(
        self,
        candles: list[Candle],
    ) -> list[Candle]:

        return [
            candle
            for candle in candles
            if candle.volume >= 0
        ]
