from .context_models import DecisionContext
from .context_store import ContextStore


class ContextEngine:

    def __init__(self):
        self.store = ContextStore()

    def register_decision(
        self,
        decision_id: str,
        score: float,
        input_context=None,
        feedback=None,
    ):

        context = DecisionContext(
            decision_id=decision_id,
            score=score,
            input_context=input_context or {},
            feedback=feedback or {},
        )

        self.store.save(context)

        return context


    def get_context_history(self):
        return self.store.get_all()


    def analyze_relationship(self, decision_id):

        history = self.store.find_by_decision(
            decision_id
        )

        return {
            "decision_id": decision_id,
            "related_decisions": len(history),
            "history": history,
        }
