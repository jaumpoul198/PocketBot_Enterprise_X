from .goal_priority import GoalPriorityEngine


class GoalEvaluator:


    def __init__(self):

        self.priority_engine = GoalPriorityEngine()



    def evaluate(
        self,
        goal,
    ):

        return self.priority_engine.calculate(
            priority=goal.priority,
            urgency=goal.metadata.get(
                "urgency",
                0.5,
            ),
            impact=goal.metadata.get(
                "impact",
                0.5,
            ),
            progress=goal.metadata.get(
                "progress",
                0.0,
            ),
        )
