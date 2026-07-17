from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class CognitiveDecisionResult:
    action: str
    confidence: float
    reasoning: str
    source: str = "cognitive_decision"

    created_at: datetime = datetime.now(UTC)
