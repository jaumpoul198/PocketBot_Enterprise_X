from .context_models import DecisionContext
from .storage.context_repository import ContextRepository


class ContextMemory:

    def __init__(
        self,
        repository=None,
        learning_engine=None,
        adaptive_engine=None,
    ):
        self.repository = repository or ContextRepository()
        self.learning_engine = learning_engine
        self.adaptive_engine = adaptive_engine


    def remember(
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

        self.repository.save(context)

        if self.learning_engine:
            self.learning_engine.learn(
                context
            )

        if self.adaptive_engine:
            self.adaptive_engine.adapt(
                context
            )

        return context


    def recall(self, decision_id: str):

        return self.repository.find(
            decision_id
        )


    def history(self):

        return self.repository.get_all()


    def size(self):

        return self.repository.count()


    def clear(self):

        self.repository.clear()
