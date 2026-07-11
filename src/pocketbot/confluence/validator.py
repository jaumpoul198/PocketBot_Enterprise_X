"""
PocketBot Enterprise X

Confluence Validator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult


class ConfluenceValidator:
    """
    Validates indicator results before confluence calculation.
    """

    def validate(
        self,
        results: Sequence[IndicatorResult],
    ) -> bool:

        if not results:
            return False

        return all(result.confidence >= 0.0 for result in results)
