from dataclasses import dataclass


@dataclass
class GoalPriorityScore:

    score: float

    reason: str



class GoalPriorityEngine:


    def calculate(
        self,
        priority: int,
        urgency: float = 0.5,
        impact: float = 0.5,
        progress: float = 0.0,
    ) -> GoalPriorityScore:

        base = priority / 10

        score = (
            (base * 0.35)
            +
            (urgency * 0.25)
            +
            (impact * 0.30)
            +
            ((1 - progress) * 0.10)
        )


        score = min(
            max(score, 0.0),
            1.0,
        )


        return GoalPriorityScore(
            score=round(score, 3),
            reason=self._reason(score),
        )


    def _reason(
        self,
        score: float,
    ) -> str:

        if score >= 0.75:
            return "high_priority"

        if score >= 0.45:
            return "medium_priority"

        return "low_priority"
