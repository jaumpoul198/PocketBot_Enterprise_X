from dataclasses import dataclass
from datetime import datetime


@dataclass
class EvolutionMetric:

    score: float
    experiences: int
    maturity: str
    timestamp: datetime
