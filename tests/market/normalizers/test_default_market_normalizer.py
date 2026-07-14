"""
Tests for Default Market Normalizer.
"""

from datetime import datetime

from pocketbot.market.normalizers.default_market_normalizer import (
    DefaultMarketNormalizer,
)


def test_normalizer_converts_raw_market_data() -> None:
    normalizer = DefaultMarketNormalizer()

    candles = normalizer.normalize(
        [
            {
                "symbol": "BTCUSDT",
                "timeframe": "1m",
                "timestamp": 1710000000,
                "open": 100,
                "high": 110,
                "low": 90,
                "close": 105,
                "volume": 500,
            }
        ]
    )

    assert len(candles) == 1

    assert candles[0].symbol == "BTCUSDT"
    assert candles[0].timeframe == "1m"

    assert float(candles[0].open) == 100
    assert float(candles[0].close) == 105
    assert candles[0].volume == 500

    assert isinstance(
        candles[0].timestamp,
        datetime,
    )
