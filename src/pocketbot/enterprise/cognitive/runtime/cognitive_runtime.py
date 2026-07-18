from datetime import UTC, datetime

from ...intelligence.runtime import IntelligenceRuntime
from ..autonomy import CognitiveAutonomyOrchestrator
from ..core.cognitive_engine import CognitiveEngine
from ..decision.cognitive_decision import CognitiveDecision
from ..goals import CognitiveGoalManager
from ..goals.runtime import GoalRuntime
from ..learning.cognitive_learning import CognitiveLearning
from ..memory.cognitive_memory import CognitiveMemory
from ..planning import CognitivePlanning
from ..reflection.self_reflection import SelfReflection


class CognitiveRuntime:

    def __init__(self):

        self.engine = CognitiveEngine()

        self.intelligence = IntelligenceRuntime()

        self.memory = CognitiveMemory()

        self.learning = CognitiveLearning()

        self.goals = CognitiveGoalManager()

        self.goal_runtime = GoalRuntime()

        self.planning = CognitivePlanning()

        self.decision = CognitiveDecision()

        self.autonomy = CognitiveAutonomyOrchestrator()

        self.self_reflection = SelfReflection()

        self.started_at = datetime.now(UTC)

        self.last_decision = None

        self.last_intelligence_decision = None

        self.last_memory_entry = None

        self.last_learning_experience = None

        self.last_goal = None

        self.last_plan = None

        self.last_final_decision = None

        self.last_autonomy_result = None

        self.last_feedback = None

        self.last_reflection = None

    def execute(
        self,
        health_score: float = 1.0,
    ):

        cognitive_decision = self.engine.process()

        intelligence_decision = self.intelligence.evaluate(
            health_score
        )

        memory_entry = self.memory.remember(
            cycle=cognitive_decision.action,
            action=cognitive_decision.action,
            confidence=cognitive_decision.confidence,
        )

        learning_experience = self.learning.learn(
            memory_entry,
            cognitive_decision.action,
            cognitive_decision.confidence,
        )

        plan = self.planning.plan(
            learning_score=self.learning.score(),
            evolution_score=self.learning.score(),
        )

        goal = self.goals.create_goal(
            name="autonomous_cycle",
            objective=plan.strategy,
            priority=1,
        )

        self.goals.engine.activate(goal)

        self.goal_runtime.register(goal)

        self.goal_runtime.prepare(goal)

        self.goal_runtime.execute(goal)

        final_decision = self.decision.decide(
            cognitive_state=cognitive_decision.action,
            memory_score=cognitive_decision.confidence,
            learning_score=self.learning.score(),
        )

        autonomy_result = self.autonomy.execute(
            action={
                "decision": final_decision,
                "plan": plan.strategy,
                "goal": goal.name,
            },
            confidence=cognitive_decision.confidence,
        )

        feedback = autonomy_result["feedback"]

        reflection = self.self_reflection.reflect(
            decision_confidence=cognitive_decision.confidence,
            feedback=feedback,
        )

        self.last_reflection = reflection

        if hasattr(self.learning, "update"):
            self.learning.update(reflection)

        self.goal_runtime.complete(
            goal,
            score=cognitive_decision.confidence,
        )

        self.last_decision = cognitive_decision

        self.last_intelligence_decision = intelligence_decision

        self.last_memory_entry = memory_entry

        self.last_learning_experience = learning_experience

        self.last_goal = goal

        self.last_plan = plan

        self.last_final_decision = final_decision

        self.last_autonomy_result = autonomy_result

        self.last_feedback = feedback

        return cognitive_decision

    def status(self):

        return {
            "started_at": self.started_at,
            "last_decision": self.last_decision,
            "last_intelligence_decision": self.last_intelligence_decision,
            "last_memory_entry": self.last_memory_entry,
            "memory": self.memory.all(),
            "last_learning_experience": self.last_learning_experience,
            "learning_score": self.learning.score(),
            "last_goal": self.last_goal,
            "goals": self.goals.get_active_goals(),
            "goal_runtime": self.goal_runtime.status(),
            "last_plan": self.last_plan,
            "planning": self.planning.status(),
            "engine": self.engine.status(),
            "intelligence": self.intelligence.status(),
            "last_final_decision": self.last_final_decision,
            "decision": self.decision.status(),
            "last_autonomy_result": self.last_autonomy_result,
            "last_feedback": self.last_feedback,
            "last_reflection": self.last_reflection,
        }
