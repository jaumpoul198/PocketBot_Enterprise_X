from pocketbot.market.strategy.base import BaseStrategy
from pocketbot.market.strategy.models import (
    StrategyResult,
    StrategySignal,
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

        indicators: dict[str, float] = data

        rsi = indicators.get("rsi")
        macd = indicators.get("macd")
        macd_signal = indicators.get("macd_signal")

        if rsi is None or macd is None or macd_signal is None:
            return StrategyResult(
                signal=StrategySignal.HOLD,
                confidence=0.0,
                reason="Missing RSI or MACD indicators",
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
