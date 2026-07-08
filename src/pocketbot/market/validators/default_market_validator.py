"""
PocketBot Enterprise X

Default Market Validator.
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.interfaces.market_validator import (
    MarketValidator,
)


class DefaultMarketValidator(MarketValidator):
    """
    Default implementation for market data validation.
    """

    def validate(
        self,
        candles: list[Candle],
    ) -> bool:
        """
        Validates market candles.
        """

        if not candles:
            return False

        return all(
            candle is not None
            for candle in candles
        )