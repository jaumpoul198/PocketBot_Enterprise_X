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

    _REQUIRED_FIELDS = (
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
    )

    def _validate_raw_data(
        self,
        raw_data: list[dict[str, object]],
    ) -> None:
        if raw_data is None:
            raise ValueError(
                "raw_data cannot be None",
            )

        if not isinstance(
            raw_data,
            list,
        ):
            raise TypeError(
                "raw_data must be a list",
            )

        for index, item in enumerate(raw_data):
            if not isinstance(
                item,
                dict,
            ):
                raise TypeError(
                    f"raw_data[{index}] must be a dictionary",
                )

            for field in self._REQUIRED_FIELDS:
                if field not in item:
                    raise ValueError(
                        f"missing required field: {field}",
                    )

    def normalize(
        self,
        raw_data: list[dict[str, object]],
    ) -> list[Candle]:
        """
        Converts raw market data into Candle entities.
        """

        self._validate_raw_data(
            raw_data,
        )

        candles: list[Candle] = []

        for item in raw_data:
            timestamp = float(
                str(item["timestamp"])
            )

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
                            str(item["open"])
                        )
                    ),
                    high=Price(
                        float(
                            str(item["high"])
                        )
                    ),
                    low=Price(
                        float(
                            str(item["low"])
                        )
                    ),
                    close=Price(
                        float(
                            str(item["close"])
                        )
                    ),
                    volume=float(
                        str(item["volume"])
                    ),
                    timestamp=datetime.fromtimestamp(
                        timestamp
                    ),
                )
            )

        return candles