from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
)


class BreakoutStrategy(BaseStrategy):
    """
    Breakout strategy based on support and resistance levels.
    """

    name = "breakout"

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

        indicators: dict[str, float] = data

        price = indicators.get("price")
        support = indicators.get("support")
        resistance = indicators.get("resistance")

        if (
            price is None
            or support is None
            or resistance is None
        ):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Missing support or resistance levels",
            )

        if price > resistance:
            return StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.9,
                reason="Price broke above resistance",
            )

        if price < support:
            return StrategyResult(
                signal=StrategySignal.SELL,
                confidence=0.9,
                reason="Price broke below support",
            )

        return StrategyResult(
            signal=StrategySignal.HOLD,
            confidence=0.5,
            reason="Price within support and resistance",
        )
