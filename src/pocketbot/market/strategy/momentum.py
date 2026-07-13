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


class MomentumStrategy(BaseStrategy):
    """
    Strategy based on RSI and MACD momentum indicators.
    """

    name = "momentum"

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

        rsi = indicators.get("rsi")
        macd = indicators.get("macd")
        macd_signal = indicators.get("macd_signal")

        if (
            rsi is None
            or macd is None
            or macd_signal is None
        ):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Missing RSI or MACD indicators",
            )

        if not (
            _is_valid_number(rsi)
            and _is_valid_number(macd)
            and _is_valid_number(macd_signal)
        ):
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Invalid indicator values",
            )

        if rsi < 30 and macd > macd_signal:
            return StrategyResult(
                signal=StrategySignal.BUY,
                confidence=0.8,
                reason="RSI oversold with MACD bullish crossover",
            )

        if rsi > 70 and macd < macd_signal:
            return StrategyResult(
                signal=StrategySignal.SELL,
                confidence=0.8,
                reason="RSI overbought with MACD bearish crossover",
            )

        return StrategyResult(
            signal=StrategySignal.HOLD,
            confidence=0.5,
            reason="No momentum confirmation",
        )
