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

        self._validate_score(score)

        return score.score >= minimum

    def confidence_ok(
        self,
        score: ScoreResult,
        minimum: float = 0.70,
    ) -> bool:
        """
        Checks confidence.
        """

        self._validate_score(score)

        return score.confidence >= minimum

    def strength_ok(
        self,
        score: ScoreResult,
        minimum: float = 0.60,
    ) -> bool:
        """
        Checks indicator strength.
        """

        self._validate_score(score)

        return score.strength >= minimum

    def _validate_score(
        self,
        score: ScoreResult,
    ) -> None:

        if score is None:
            raise TypeError(
                "score cannot be None"
            )

        if not isinstance(
            score,
            ScoreResult,
        ):
            raise TypeError(
                "score must be ScoreResult"
            )