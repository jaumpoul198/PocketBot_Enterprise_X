from .goal_evaluator import GoalEvaluator


class GoalOptimizer:


    def __init__(self):

        self.evaluator = GoalEvaluator()



    def optimize(
        self,
        goals: list,
    ):

        evaluated = []

        for goal in goals:

            score = self.evaluator.evaluate(
                goal
            )

            evaluated.append(
                {
                    "goal": goal,
                    "score": score,
                }
            )


        evaluated.sort(
            key=lambda item: item["score"].score,
            reverse=True,
        )


        return evaluated
