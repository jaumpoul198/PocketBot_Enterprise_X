from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class DecisionContext:
    decision_id: str
    score: float
    input_context: Dict[str, Any] = field(default_factory=dict)
    feedback: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ContextSnapshot:
    decision_id: str
    history: list[DecisionContext] = field(default_factory=list)
