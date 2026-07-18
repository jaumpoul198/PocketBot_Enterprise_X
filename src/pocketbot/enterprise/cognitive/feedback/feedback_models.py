from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass
class CognitiveFeedback:

    decision: str

    outcome: str

    score: float

    timestamp: datetime = None

    def __post_init__(self):

        if self.timestamp is None:
            self.timestamp = datetime.now(UTC)
