from enum import Enum


class GoalExecutionState(Enum):

    CREATED = "created"

    READY = "ready"

    EXECUTING = "executing"

    COMPLETED = "completed"

    FAILED = "failed"


class GoalStateMachine:

    def transition(
        self,
        current: GoalExecutionState,
        event: str,
    ) -> GoalExecutionState:

        transitions = {

            GoalExecutionState.CREATED: {
                "prepare": GoalExecutionState.READY,
            },

            GoalExecutionState.READY: {
                "execute": GoalExecutionState.EXECUTING,
            },

            GoalExecutionState.EXECUTING: {
                "complete": GoalExecutionState.COMPLETED,
                "fail": GoalExecutionState.FAILED,
            },

        }

        allowed = transitions.get(
            current,
            {},
        )

        return allowed.get(
            event,
            current,
        )
