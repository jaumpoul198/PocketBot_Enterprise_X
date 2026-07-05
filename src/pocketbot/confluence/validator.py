"""
PocketBot Enterprise X

Confluence validator.
"""

from __future__ import annotations

from collections.abc import Sequence

from pocketbot.indicators.base.result import IndicatorResult


class ConfluenceValidator:
    """
    Validates indicator results.
    """

    def validate(
        self,
        results: Sequence[IndicatorResult],
    ) -> bool:
        return len(results) > 0
