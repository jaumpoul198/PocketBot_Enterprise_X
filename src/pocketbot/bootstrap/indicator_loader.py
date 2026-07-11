"""
PocketBot Enterprise X

Indicator Loader.
"""

from __future__ import annotations

from pocketbot.indicators.momentum.rsi import RSIIndicator
from pocketbot.indicators.momentum.stochastic import (
    StochasticIndicator,
)
from pocketbot.indicators.registry import IndicatorRegistry
from pocketbot.indicators.trend.ema import EMAIndicator
from pocketbot.indicators.trend.macd import MACDIndicator
from pocketbot.indicators.trend.sma import SMAIndicator
from pocketbot.indicators.volatility.atr import ATRIndicator
from pocketbot.indicators.volatility.bollinger import BollingerIndicator


def load_indicators() -> IndicatorRegistry:
    """
    Carrega todos os indicadores disponíveis.
    """

    registry = IndicatorRegistry()

    registry.register("EMA", EMAIndicator)
    registry.register("SMA", SMAIndicator)
    registry.register("MACD", MACDIndicator)

    registry.register("ATR", ATRIndicator)
    registry.register("BOLLINGER", BollingerIndicator)

    registry.register("RSI", RSIIndicator)
    registry.register("STOCHASTIC", StochasticIndicator)

    return registry
