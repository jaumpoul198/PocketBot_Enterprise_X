from typing import Dict, Any

from .autonomy_controller import AutonomyController
from .autonomous_executor import AutonomousExecutor
from .autonomy_feedback import AutonomyFeedback
from .autonomy_evolution_bridge import AutonomyEvolutionBridge
from .evolution_adapter import EvolutionAdapter
from .autonomy_state import AutonomyState


class CognitiveAutonomyOrchestrator:
    """
    Coordinates Cognitive Autonomy components.
    """

    def __init__(self):

        self.controller = AutonomyController()

        self.executor = AutonomousExecutor()

        self.feedback = AutonomyFeedback()

        self.evolution_bridge = AutonomyEvolutionBridge()

        self.evolution = EvolutionAdapter()

        self.state = AutonomyState()


    def execute(
        self,
        action: Dict[str, Any],
        confidence: float,
    ) -> Dict[str, Any]:

        self.controller.start()


        execution = self.executor.execute(
            {
                "action": action,
                "confidence": confidence,
            }
        )


        feedback = self.feedback.register_feedback(
            action=action,
            success=execution["approved"],
            reward=confidence,
        )


        event = self.evolution_bridge.process_feedback(
            feedback
        )


        evolution = self.evolution.process_event(
            event
        )


        self.state.add_execution(
            execution
        )

        self.state.add_feedback(
            feedback
        )

        self.state.add_evolution_event(
            event
        )


        return {
            "execution": execution,
            "feedback": feedback,
            "evolution": evolution,
        }


    def status(self):

        return {
            "cycles": self.controller.cycles,

            "feedback": len(
                self.feedback.get_history()
            ),

            "evolution_events": len(
                self.evolution_bridge.get_events()
            ),

            "state": self.state.snapshot(),
        }
