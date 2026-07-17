from dataclasses import dataclass
from datetime import datetime


@dataclass
class PlanningResult:

    objective: str

    priority: float

    strategy: str

    timestamp: datetime
