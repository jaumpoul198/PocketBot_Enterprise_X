from .goal_state_machine import (
    GoalExecutionState,
    GoalStateMachine,
)

from .goal_feedback import GoalFeedback


class GoalRuntime:

    def __init__(self):

        self.state_machine = GoalStateMachine()

        self.feedback = GoalFeedback()

        self.states = {}


    def register(
        self,
        goal,
    ):

        self.states[id(goal)] = GoalExecutionState.CREATED

        return goal


    def prepare(
        self,
        goal,
    ):

        state = self.states.get(
            id(goal),
            GoalExecutionState.CREATED,
        )

        new_state = self.state_machine.transition(
            state,
            "prepare",
        )

        self.states[id(goal)] = new_state

        return new_state


    def execute(
        self,
        goal,
    ):

        state = self.states.get(
            id(goal),
            GoalExecutionState.READY,
        )

        new_state = self.state_machine.transition(
            state,
            "execute",
        )

        self.states[id(goal)] = new_state

        return new_state


    def complete(
        self,
        goal,
        score: float = 1.0,
    ):

        state = self.states.get(
            id(goal),
            GoalExecutionState.EXECUTING,
        )

        new_state = self.state_machine.transition(
            state,
            "complete",
        )

        self.states[id(goal)] = new_state

        self.feedback.record(
            goal,
            "completed",
            score,
        )

        return new_state


    def fail(
        self,
        goal,
    ):

        state = self.states.get(
            id(goal),
            GoalExecutionState.EXECUTING,
        )

        new_state = self.state_machine.transition(
            state,
            "fail",
        )

        self.states[id(goal)] = new_state

        self.feedback.record(
            goal,
            "failed",
            0.0,
        )

        return new_state


    def status(
        self,
    ):

        return {
            "active_goals": len(self.states),
            "feedback": self.feedback.history,
        }
