"""
PocketBot Enterprise X

Default Market Normalizer.
"""

from __future__ import annotations

from datetime import datetime

from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.interfaces.market_normalizer import (
    MarketNormalizer,
)


class DefaultMarketNormalizer(MarketNormalizer):
    """
    Default implementation for market normalization.
    """

    def normalize(
        self,
        raw_data: list[dict[str, object]],
    ) -> list[Candle]:
        """
        Converts raw market data into Candle entities.
        """

        candles: list[Candle] = []

        for item in raw_data:
            candles.append(
                Candle(
                    symbol=str(
                        item.get(
                            "symbol",
                            "UNKNOWN",
                        )
                    ),
                    timeframe=str(
                        item.get(
                            "timeframe",
                            "1m",
                        )
                    ),
                    open=Price(
                        float(
                            item["open"]
                        )
                    ),
                    high=Price(
                        float(
                            item["high"]
                        )
                    ),
                    low=Price(
                        float(
                            item["low"]
                        )
                    ),
                    close=Price(
                        float(
                            item["close"]
                        )
                    ),
                    volume=float(
                        item["volume"]
                    ),
                    timestamp=datetime.fromtimestamp(
                        float(
                            item["timestamp"]
                        )
                    ),
                )
            )

        return candles
