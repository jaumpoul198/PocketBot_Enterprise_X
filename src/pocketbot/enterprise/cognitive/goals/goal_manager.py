from .cognitive_goal import CognitiveGoalEngine
from .goal_models import CognitiveGoal


class CognitiveGoalManager:

    def __init__(self):
        self.engine = CognitiveGoalEngine()
        self.goals: list[CognitiveGoal] = []

    def create_goal(
        self,
        name: str,
        objective: str,
        priority: int = 1,
    ) -> CognitiveGoal:

        goal = self.engine.create(
            name,
            objective,
            priority,
        )

        self.goals.append(goal)

        return goal

    def get_active_goals(self):

        return [
            goal
            for goal in self.goals
            if goal.status.value == "active"
        ]

    def complete_goal(
        self,
        goal: CognitiveGoal,
    ):

        return self.engine.complete(goal)
