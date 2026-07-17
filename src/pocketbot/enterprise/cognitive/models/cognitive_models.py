from dataclasses import dataclass
from datetime import datetime


@dataclass
class CognitiveSignal:
    name: str
    value: float
    source: str
    timestamp: datetime


@dataclass
class CognitiveStateModel:
    state: str
    confidence: float
    timestamp: datetime


@dataclass
class CognitiveDecision:
    action: str
    confidence: float
    reasoning: str
    timestamp: datetime
