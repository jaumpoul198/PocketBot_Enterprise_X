"""
Failure scenarios for Default Market Normalizer.
"""

import pytest

from pocketbot.market.normalizers.default_market_normalizer import (
    DefaultMarketNormalizer,
)


def test_empty_raw_data_returns_empty_list() -> None:
    normalizer = DefaultMarketNormalizer()

    result = normalizer.normalize(
        []
    )

    assert result == []


def test_invalid_timestamp_is_rejected() -> None:
    normalizer = DefaultMarketNormalizer()

    with pytest.raises(
        ValueError,
    ):
        normalizer.normalize(
            [
                {
                    "timestamp": "invalid",
                    "open": 100,
                    "high": 110,
                    "low": 90,
                    "close": 105,
                    "volume": 500,
                }
            ]
        )
