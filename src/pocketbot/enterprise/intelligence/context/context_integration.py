from .context_engine import ContextEngine


class ContextIntegration:

    def __init__(
        self,
        context_engine=None,
        adaptive_engine=None,
        learning_engine=None,
        feedback_processor=None,
    ):
        self.context_engine = context_engine or ContextEngine()
        self.adaptive_engine = adaptive_engine
        self.learning_engine = learning_engine
        self.feedback_processor = feedback_processor


    def process_decision(
        self,
        decision_id: str,
        score: float,
        input_context=None,
        feedback=None,
    ):

        context = self.context_engine.register_decision(
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


    def get_context(self):

        return self.context_engine.get_context_history()
