from dataclasses import dataclass
from datetime import datetime


@dataclass
class LearningExperience:
    event: str
    outcome: str
    score: float
    timestamp: datetime
