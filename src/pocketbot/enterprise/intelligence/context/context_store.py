from .context_models import DecisionContext


class ContextStore:

    def __init__(self):
        self._contexts = []

    def save(self, context: DecisionContext):
        self._contexts.append(context)

    def get_all(self):
        return self._contexts

    def find_by_decision(self, decision_id: str):
        return [
            ctx for ctx in self._contexts
            if ctx.decision_id == decision_id
        ]
