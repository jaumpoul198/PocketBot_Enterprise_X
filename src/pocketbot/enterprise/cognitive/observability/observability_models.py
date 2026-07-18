"""
PocketBot Enterprise X
Cognitive Observability Models

Core data structures used by the
cognitive monitoring system.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from uuid import uuid4


def utc_now():
    return datetime.now(timezone.utc)


@dataclass
class CognitiveMetric:
    """
    Represents a measurable cognitive signal.
    """

    name: str
    value: float
    component: str

    timestamp: datetime = field(default_factory=utc_now)

    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CognitiveEvent:
    """
    Represents an event generated during
    cognitive processing.
    """

    event_type: str
    source: str

    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    timestamp: datetime = field(default_factory=utc_now)

    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CognitiveTrace:
    """
    Represents execution tracing
    through cognitive cycles.
    """

    operation: str

    trace_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    started_at: datetime = field(default_factory=utc_now)

    finished_at: Optional[datetime] = None

    steps: List[str] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)


    def add_step(self, step: str):
        self.steps.append(step)


    def finish(self):
        self.finished_at = utc_now()
