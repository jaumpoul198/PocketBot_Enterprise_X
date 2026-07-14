"""
PocketBot Enterprise X

Default Market Provider.
"""

from __future__ import annotations

from pocketbot.domain.candle import Candle
from pocketbot.market.providers.base_provider import BaseProvider


class DefaultMarketProvider(BaseProvider):
    """
    Default market provider implementation.
    """

    def get_candles(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        """
        Returns market candles.
        """

        self._validate_asset(asset)
        self._validate_timeframe(timeframe)
        self._validate_count(count)

        return []

    @staticmethod
    def _validate_asset(
        asset: str,
    ) -> None:

        if asset is None:
            raise ValueError(
                "asset cannot be None",
            )

        if not isinstance(asset, str):
            raise TypeError(
                "asset must be a string",
            )

    @staticmethod
    def _validate_timeframe(
        timeframe: int,
    ) -> None:

        if timeframe is None:
            raise ValueError(
                "timeframe cannot be None",
            )

        if isinstance(timeframe, bool):
            raise TypeError(
                "timeframe must be an integer",
            )

        if not isinstance(timeframe, int):
            raise TypeError(
                "timeframe must be an integer",
            )

    @staticmethod
    def _validate_count(
        count: int,
    ) -> None:

        if count is None:
            raise ValueError(
                "count cannot be None",
            )

        if isinstance(count, bool):
            raise TypeError(
                "count must be an integer",
            )

        if not isinstance(count, int):
            raise TypeError(
                "count must be an integer",
            )

        if count <= 0:
            raise ValueError(
                "count must be greater than zero",
            )
