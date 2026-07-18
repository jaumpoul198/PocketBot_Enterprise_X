from dataclasses import dataclass
from datetime import datetime


@dataclass
class CognitiveMemoryEntry:

    cycle: str

    action: str

    confidence: float

    timestamp: datetime


@dataclass
class CognitiveKnowledge:

    source: str

    pattern: str

    score: float

    created_at: datetime
