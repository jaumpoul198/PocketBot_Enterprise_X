"""
PocketBot Enterprise X

Decision filter interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from pocketbot.decision.result import DecisionResult
from pocketbot.score.result import ScoreResult


class DecisionFilter(ABC):
    """
    Base interface for every decision filter.
    """

    @abstractmethod
    def evaluate(
        self,
        score: ScoreResult,
    ) -> DecisionResult | None:
        """
        Returns None when the filter approves
        the operation.

        Returns DecisionResult when the operation
        must be rejected.
        """
        raise NotImplementedError