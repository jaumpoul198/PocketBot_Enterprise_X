import time
from datetime import UTC, datetime

from ...intelligence.runtime import IntelligenceRuntime
from ..autonomy import CognitiveAutonomyOrchestrator
from ..core.cognitive_engine import CognitiveEngine
from ..decision.cognitive_decision import CognitiveDecision
from ..feedback.cognitive_feedback_loop import CognitiveFeedbackLoop
from ..evolution import CognitiveEvolution
from ..goals import CognitiveGoalManager
from ..goals.runtime import GoalRuntime
from ..learning.cognitive_learning import CognitiveLearning
from ..memory.cognitive_memory import CognitiveMemory
from ..planning import CognitivePlanning
from ..reflection.self_reflection import SelfReflection
from ..persistence import CognitiveStorage
from ..observability import CognitiveMonitor


class CognitiveRuntime:

    def __init__(
        self,
        observability: CognitiveMonitor | None = None,
    ):

        self.observability = observability or CognitiveMonitor()
        
        self.engine = CognitiveEngine()

        self.intelligence = IntelligenceRuntime()

        self.memory = CognitiveMemory()

        self.learning = CognitiveLearning()

        self.goals = CognitiveGoalManager()

        self.goal_runtime = GoalRuntime()

        self.planning = CognitivePlanning()

        self.decision = CognitiveDecision()

        self.feedback_loop = CognitiveFeedbackLoop()

        self.evolution = CognitiveEvolution()

        self.autonomy = CognitiveAutonomyOrchestrator()

        self.self_reflection = SelfReflection()

        self.storage = CognitiveStorage()

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
        self.last_evolution_metric = None

        # Runtime metrics
        self.cycles_executed = 0
        self.successful_cycles = 0
        self.failed_cycles = 0

        self.last_cycle_duration = None
        self.last_cycle_started = None
        self.last_cycle_finished = None

        self.total_cycle_duration = 0.0
        self.average_cycle_duration = 0.0

        self.last_error = None


    def execute(
        self,
        health_score: float = 1.0,
    ):

        self.last_cycle_started = datetime.now(UTC)

        start_time = time.perf_counter()

        trace = self.observability.start_trace(
            "cognitive_runtime.execute"
        )

        self.observability.emit_event(
            event_type="COGNITIVE_RUNTIME_STARTED",
            source="runtime",
        )

        try:

            result = self._execute_cycle(
                health_score
            )

            self.successful_cycles += 1
            self.cycles_executed += 1

            return result

        except Exception as error:

            self.failed_cycles += 1
            self.cycles_executed += 1

            self.last_error = repr(error)

            self.observability.emit_event(
                event_type="COGNITIVE_RUNTIME_ERROR",
                source="runtime",
                payload={
                   "error": repr(error),
                },
            )

            self.observability.traces.finish(trace)

            return None

        finally:

            duration = time.perf_counter() - start_time

            self.observability.record_metric(
                name="runtime_cycle_duration",
                value=duration,
                component="runtime",
            )

            self.last_cycle_duration = duration

            self.total_cycle_duration += duration

            if self.cycles_executed:
                self.average_cycle_duration = (
                    self.total_cycle_duration /
                    self.cycles_executed
                )

            self.last_cycle_finished = datetime.now(UTC)

    def _execute_cycle(
        self,
        health_score: float = 1.0,
    ):

        cognitive_decision = self.engine.process()

        self.storage.save_decision(
            cognitive_decision.action,
            cognitive_decision.confidence,
        )

        intelligence_decision = self.intelligence.evaluate(
            health_score
        )

        memory_entry = self.memory.remember(
            cycle=cognitive_decision.action,
            action=cognitive_decision.action,
            confidence=cognitive_decision.confidence,
        )

        self.storage.save_memory(
            memory_entry
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

        self.feedback_loop.evaluate(
            decision=str(final_decision),
            outcome=str(feedback),
            score=cognitive_decision.confidence,
        )

        self.last_reflection = reflection

        if hasattr(self.learning, "update"):
            self.learning.update(reflection)

        evolution_metric = self.evolution.evaluate(
            memory_count=self.memory.count(),
            learning_score=self.learning.score(),
        )

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

        self.last_evolution_metric = evolution_metric

        self.storage.save_metric(
            "evolution_score",
            self.learning.score(),
        )

        self.storage.save_metric(
            "confidence",
            cognitive_decision.confidence,
        )

        return cognitive_decision


    def health(self):

        total = self.cycles_executed

        success_rate = 0

        if total:
            success_rate = (
                self.successful_cycles /
                total
            )

        status = "healthy"

        if self.failed_cycles:
            status = "degraded"

        return {
            "status": status,
            "cycles": total,
            "successful_cycles": self.successful_cycles,
            "failed_cycles": self.failed_cycles,
            "success_rate": success_rate,
            "last_duration": self.last_cycle_duration,
            "average_duration": self.average_cycle_duration,
            "last_error": self.last_error,
        }


    def status(self):

        return {
            "health": self.health(),

            "storage": self.storage.health(),

            "started_at": self.started_at,

            "last_decision": self.last_decision,

            "last_intelligence_decision": self.last_intelligence_decision,

            "last_memory_entry": self.last_memory_entry,

            "memory": self.memory.all(),

            "last_learning_experience": self.last_learning_experience,

            "learning_score": self.learning.score(),

            "learning_status": {
                "experiences": len(
                    self.learning.history()
                ),
                "feedback_entries": len(
                    self.learning.feedback()
                ),
                "score": self.learning.score(),
            },

            "feedback_metrics": {
                "feedback_score": self.learning.feedback_score(),
                "feedback_history": self.learning.feedback(),
            },

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

            "feedback_loop": {
                "score": self.feedback_loop.score(),
                "history": self.feedback_loop.all(),
            },

            "evolution": {
                "latest": self.evolution.latest(),
                "last_metric": self.last_evolution_metric,
            },

            "last_reflection": self.last_reflection,

            "runtime_metrics": {
                "cycles_executed": self.cycles_executed,
                "successful_cycles": self.successful_cycles,
                "failed_cycles": self.failed_cycles,
                "last_cycle_duration": self.last_cycle_duration,
                "average_cycle_duration": self.average_cycle_duration,
                "last_cycle_started": self.last_cycle_started,
                "last_cycle_finished": self.last_cycle_finished,
                "last_error": self.last_error,
            },
        }
