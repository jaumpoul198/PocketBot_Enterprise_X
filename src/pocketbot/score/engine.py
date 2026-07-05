"""
PocketBot Enterprise X

Score Engine.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult

from pocketbot.score.calculator import ScoreCalculator
from pocketbot.score.result import ScoreResult


class ScoreEngine:
    """
    Orchestrates the complete score calculation process.
    """

    def __init__(self) -> None:
        self._calculator = ScoreCalculator()

    def calculate(
        self,
        results: Sequence[IndicatorResult],
    ) -> ScoreResult:
        """
        Calculates the final score.

        Parameters
        ----------
        results
            Indicator results.

        Returns
        -------
        ScoreResult
        """

        return self._calculator.calculate(results)