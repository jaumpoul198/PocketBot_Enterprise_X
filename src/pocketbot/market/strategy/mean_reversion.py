import math
from typing import TypeGuard

from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


def _is_valid_number(value: object) -> TypeGuard[float]:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


class MeanReversionStrategy(BaseStrategy):
    """
    Mean reversion strategy based on Bollinger Bands.
    """

    name = "mean_reversion"

    def analyze(
        self,
        data: object,
    ) -> StrategyResult:

        if not isinstance(data, dict):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Invalid indicator data",
            )

        indicators: dict[str, object] = data

        price = indicators.get("price")
        lower_band = indicators.get("bollinger_lower")
        upper_band = indicators.get("bollinger_upper")

        if (
            price is None
            or lower_band is None
            or upper_band is None
        ):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Missing Bollinger Band indicators",
            )

        if not (
            _is_valid_number(price)
            and _is_valid_number(lower_band)
            and _is_valid_number(upper_band)
        ):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Invalid indicator values",
            )

        if price <= lower_band:
            return StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.8,
                reason="Price reached lower Bollinger Band",
            )

        if price >= upper_band:
            return StrategyResult(
                signal=StrategySignal.SELL,
                confidence=0.8,
                reason="Price reached upper Bollinger Band",
            )

        return StrategyResult(
            signal=StrategySignal.HOLD,
            confidence=0.5,
            reason="Price within Bollinger Bands",
        )
