from .context_bridge import ContextBridge


class ContextRuntime:

    def __init__(
        self,
        context_bridge=None,
        intelligence_runtime=None,
    ):

        self.context_bridge = context_bridge or ContextBridge()
        self.intelligence_runtime = intelligence_runtime


    def execute_decision(
        self,
        decision_id: str,
        score: float,
        input_context=None,
        feedback=None,
    ):

        context = self.context_bridge.process(
            decision_id=decision_id,
            score=score,
            input_context=input_context,
            feedback=feedback,
        )

        return {
            "decision_id": context.decision_id,
            "score": context.score,
            "context": context,
        }


    def get_context_history(self):

        return self.context_bridge.get_history()


    def get_context_count(self):

        return self.context_bridge.total_contexts()


    def recall_decision(
        self,
        decision_id: str,
    ):

        return self.context_bridge.recall(
            decision_id
        )
