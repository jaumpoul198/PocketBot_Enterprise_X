"""
PocketBot Enterprise X

Shared moving average calculations used by technical indicators.
"""

from __future__ import annotations

from collections.abc import Sequence


def simple_moving_average(
    values: Sequence[float],
    period: int,
) -> float:
    """
    Calculates the Simple Moving Average (SMA).

    Args:
        values:
            Ordered price series.

        period:
            Window size.

    Returns:
        SMA value.

    Raises:
        ValueError:
            If the period is invalid or there is insufficient data.
    """

    if period <= 0:
        raise ValueError("Period must be greater than zero.")

    if len(values) < period:
        raise ValueError("Insufficient data for SMA.")

    window = values[-period:]

    return sum(window) / period


def exponential_moving_average(
    values: Sequence[float],
    period: int,
) -> float:
    """
    Calculates the Exponential Moving Average (EMA).

    Args:
        values:
            Ordered price series.

        period:
            EMA period.

    Returns:
        EMA value.

    Raises:
        ValueError:
            If the period is invalid or there is insufficient data.
    """

    if period <= 0:
        raise ValueError("Period must be greater than zero.")

    if len(values) < period:
        raise ValueError("Insufficient data for EMA.")

    multiplier = 2.0 / (period + 1)

    ema = simple_moving_average(values[:period], period)

    for price in values[period:]:
        ema = ((price - ema) * multiplier) + ema

    return ema
