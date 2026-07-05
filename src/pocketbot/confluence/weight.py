"""
PocketBot Enterprise X

Weight manager.
"""

from __future__ import annotations

from pocketbot.indicators.base.result import IndicatorResult


class WeightManager:
    """
    Normalizes indicator weights.
    """

    def normalize(
        self,
        result: IndicatorResult,
    ) -> IndicatorResult:

        return result
