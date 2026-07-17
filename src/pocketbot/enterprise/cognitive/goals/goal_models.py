from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum


class GoalStatus(Enum):
    CREATED = "created"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class CognitiveGoal:
    name: str
    objective: str
    priority: int = 1

    status: GoalStatus = GoalStatus.CREATED

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    completed_at: datetime | None = None

    metadata: dict = field(default_factory=dict)

    def activate(self):
        self.status = GoalStatus.ACTIVE

    def complete(self):
        self.status = GoalStatus.COMPLETED
        self.completed_at = datetime.now(UTC)

    def fail(self):
        self.status = GoalStatus.FAILED
