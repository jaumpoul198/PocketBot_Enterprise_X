from datetime import datetime, timezone


class ContextMetrics:
    def __init__(self):
        self.created_at = datetime.now(timezone.utc)

        self.total_decisions = 0
        self.successful_feedbacks = 0
        self.total_score = 0.0

        self.records = []

    def record(self, score, feedback=None):
        feedback = feedback or {}

        self.total_decisions += 1
        self.total_score += score

        if feedback.get("success"):
            self.successful_feedbacks += 1

        self.records.append(
            {
                "score": score,
                "feedback": feedback,
                "created_at": datetime.now(timezone.utc),
            }
        )

    def average_score(self):
        if self.total_decisions == 0:
            return 0.0

        return self.total_score / self.total_decisions

    def success_rate(self):
        if self.total_decisions == 0:
            return 0.0

        return self.successful_feedbacks / self.total_decisions

    def snapshot(self):
        return {
            "created_at": self.created_at,
            "total_decisions": self.total_decisions,
            "successful_feedbacks": self.successful_feedbacks,
            "average_score": self.average_score(),
            "success_rate": self.success_rate(),
            "records": self.records,
        }
