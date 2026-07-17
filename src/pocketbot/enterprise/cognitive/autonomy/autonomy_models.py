from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class AutonomyDecision:
    action: str
    allowed: bool
    risk: float
    confidence: float
    reasoning: str

    created_at: datetime = datetime.now(UTC)
