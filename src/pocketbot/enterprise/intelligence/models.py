from dataclasses import dataclass
from datetime import datetime


@dataclass
class IntelligenceSignal:
    name: str
    value: float
    severity: str
    timestamp: datetime


@dataclass
class IntelligenceDecision:
    action: str
    confidence: float
    reason: str
    timestamp: datetime
