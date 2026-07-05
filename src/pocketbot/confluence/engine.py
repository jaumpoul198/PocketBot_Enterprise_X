"""
PocketBot Enterprise X

Confluence Engine.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult
from pocketbot.confluence.validator import ConfluenceValidator
from pocketbot.confluence.scorer import ConfluenceScorer


class ConfluenceEngine:
    """
    Calculates the overall confluence from indicator results.
    """

    def __init__(self) -> None:
        self._validator = ConfluenceValidator()
        self._scorer = ConfluenceScorer()

    def calculate(
        self,
        results: Sequence[IndicatorResult],
    ) -> float:

        if not self._validator.validate(results):
            return 0.0

        return self._scorer.calculate(results)