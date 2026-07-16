from .context_memory import ContextMemory


class ContextBridge:

    def __init__(
        self,
        context_memory=None,
        learning_engine=None,
        adaptive_engine=None,
        feedback_processor=None,
    ):

        self.context_memory = context_memory or ContextMemory()
        self.learning_engine = learning_engine
        self.adaptive_engine = adaptive_engine
        self.feedback_processor = feedback_processor


    def process(
        self,
        decision_id: str,
        score: float,
        input_context=None,
        feedback=None,
    ):

        context = self.context_memory.remember(
            decision_id=decision_id,
            score=score,
            input_context=input_context,
            feedback=feedback,
        )


        if self.feedback_processor:

            self.feedback_processor.process(
                feedback or {}
            )


        if self.learning_engine:

            self.learning_engine.learn(
                context
            )


        if self.adaptive_engine:

            self.adaptive_engine.adapt(
                context
            )


        return context


    def recall(
        self,
        decision_id: str,
    ):

        return self.context_memory.recall(
            decision_id
        )


    def get_history(self):

        return self.context_memory.history()


    def total_contexts(self):

        return self.context_memory.size()
