from datetime import datetime


class ContextMetrics:

    def __init__(self):

        self.total_decisions = 0
        self.successful_feedbacks = 0
        self.failed_feedbacks = 0
        self.total_score = 0.0
        self.created_at = datetime.utcnow()


    def record(
        self,
        score: float,
        feedback=None,
    ):

        self.total_decisions += 1
        self.total_score += score

        if feedback:

            if feedback.get("success"):

                self.successful_feedbacks += 1

            else:

                self.failed_feedbacks += 1


    def average_score(self):

        if self.total_decisions == 0:
            return 0

        return (
            self.total_score /
            self.total_decisions
        )


    def success_rate(self):

        if self.total_decisions == 0:
            return 0

        return (
            self.successful_feedbacks /
            self.total_decisions
        )


    def snapshot(self):

        return {
            "total_decisions": self.total_decisions,
            "average_score": self.average_score(),
            "success_rate": self.success_rate(),
            "successful_feedbacks": self.successful_feedbacks,
            "failed_feedbacks": self.failed_feedbacks,
        }
