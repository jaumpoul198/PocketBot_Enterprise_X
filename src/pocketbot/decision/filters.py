"""
PocketBot Enterprise X

Decision filters.
"""

from __future__ import annotations

from pocketbot.score.result import ScoreResult


class DecisionFilters:
    """
    Collection of decision validation rules.
    """

    def score_ok(
        self,
        score: ScoreResult,
        minimum: float = 80.0,
    ) -> bool:
        """
        Checks whether the score is sufficient.
        """
        return score.score >= minimum

    def confidence_ok(
        self,
        score: ScoreResult,
        minimum: float = 0.70,
    ) -> bool:
        """
        Checks confidence.
        """
        return score.confidence >= minimum

    def strength_ok(
        self,
        score: ScoreResult,
        minimum: float = 0.60,
    ) -> bool:
        """
        Checks indicator strength.
        """
        return score.strength >= minimum