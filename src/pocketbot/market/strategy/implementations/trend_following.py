from __future__ import annotations

import math

from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


class TrendFollowingStrategy(BaseStrategy):

    @property
    def name(self) -> str:
        return "trend_following"

    def analyze(
        self,
        market_data: object,
    ) -> StrategyResult:
        """
        Simple trend detection using EMA and SMA values.

        Expected market_data:
        {
            "ema": float,
            "sma": float,
        }
        """

        if not isinstance(
            market_data,
            dict,
        ):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Invalid market data",
            )

        ema = market_data.get("ema")
        sma = market_data.get("sma")

        if ema is None or sma is None:
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Missing moving averages",
            )

        self._validate_average(
            ema,
            "ema",
        )

        self._validate_average(
            sma,
            "sma",
        )

        if ema > sma:
            return StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.8,
                reason="EMA above SMA indicates bullish trend",
            )

        if ema < sma:
            return StrategyResult(
                signal=StrategySignal.SELL,
                confidence=0.8,
                reason="EMA below SMA indicates bearish trend",
            )

        return StrategyResult(
            signal=StrategySignal.HOLD,
            confidence=0.5,
            reason="EMA equals SMA",
        )

    @staticmethod
    def _validate_average(
        value: object,
        field_name: str,
    ) -> None:
        if isinstance(value, bool):
            raise TypeError(
                f"{field_name} must be numeric"
            )

        if not isinstance(
            value,
            (int, float),
        ):
            raise TypeError(
                f"{field_name} must be numeric"
            )

        if not math.isfinite(
            float(value),
        ):
            raise ValueError(
                f"{field_name} must be finite"
            )
