from pocketbot.enterprise.cognitive.goals.goal_models import (
    CognitiveGoal,
)

from pocketbot.enterprise.cognitive.goals.runtime.goal_runtime import (
    GoalRuntime,
)

from pocketbot.enterprise.cognitive.goals.runtime.goal_state_machine import (
    GoalExecutionState,
)


def test_goal_runtime_execution_cycle():

    runtime = GoalRuntime()

    goal = CognitiveGoal(
        name="optimize_system",
        objective="improve autonomy",
    )

    runtime.register(goal)

    assert runtime.states[id(goal)] == GoalExecutionState.CREATED

    runtime.prepare(goal)

    assert runtime.states[id(goal)] == GoalExecutionState.READY

    runtime.execute(goal)

    assert runtime.states[id(goal)] == GoalExecutionState.EXECUTING

    runtime.complete(
        goal,
        score=0.95,
    )

    assert runtime.states[id(goal)] == GoalExecutionState.COMPLETED

    feedback = runtime.feedback.latest()

    assert feedback["result"] == "completed"
    assert feedback["score"] == 0.95
