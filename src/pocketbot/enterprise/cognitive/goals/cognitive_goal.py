from .goal_models import CognitiveGoal


class CognitiveGoalEngine:

    def create(
        self,
        name: str,
        objective: str,
        priority: int = 1,
    ) -> CognitiveGoal:

        return CognitiveGoal(
            name=name,
            objective=objective,
            priority=priority,
        )

    def activate(
        self,
        goal: CognitiveGoal,
    ) -> CognitiveGoal:

        goal.activate()
        return goal

    def complete(
        self,
        goal: CognitiveGoal,
    ) -> CognitiveGoal:

        goal.complete()
        return goal

    def fail(
        self,
        goal: CognitiveGoal,
    ) -> CognitiveGoal:

        goal.fail()
        return goal
