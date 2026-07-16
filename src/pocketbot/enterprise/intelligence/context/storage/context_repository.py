from typing import List

from ..context_models import DecisionContext


class ContextRepository:

    def __init__(self):
        self._storage: List[DecisionContext] = []


    def save(self, context: DecisionContext):
        self._storage.append(context)
        return context


    def get_all(self):
        return self._storage


    def find(self, decision_id: str):

        return [
            context
            for context in self._storage
            if context.decision_id == decision_id
        ]


    def count(self):

        return len(self._storage)


    def clear(self):

        self._storage.clear()
