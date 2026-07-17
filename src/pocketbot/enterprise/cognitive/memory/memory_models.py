from dataclasses import dataclass
from datetime import datetime


@dataclass
class CognitiveMemoryEntry:
    cycle: str
    action: str
    confidence: float
    timestamp: datetime
