from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(slots=True)
class AdaptiveDecision:
    threshold: float
    mode: str
    confidence_floor: float

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_mapping(cls, data=None):
        data = data or {}

        return cls(
            threshold=data.get("threshold", 0.50),
            mode=data.get("mode", "supervised"),
            confidence_floor=data.get(
                "confidence_floor",
                0.60,
            ),
        )


class AdaptiveEngine:
    """
    Computes adaptive operating parameters based on
    the current autonomy score.
    """

    def evaluate(self, autonomy_score: float) -> AdaptiveDecision:
        if autonomy_score >= 90:
            return AdaptiveDecision(
                threshold=0.90,
                mode="autonomous",
                confidence_floor=0.95,
            )

        if autonomy_score >= 70:
            return AdaptiveDecision(
                threshold=0.70,
                mode="assisted",
                confidence_floor=0.80,
            )

        return AdaptiveDecision(
            threshold=0.50,
            mode="supervised",
            confidence_floor=0.60,
        )
