"""
PocketBot Enterprise X
Cognitive Monitor

Central coordinator for cognitive
system observability.
"""

from typing import Any, Dict, Optional

from .cognitive_metrics import CognitiveMetrics
from .cognitive_events import CognitiveEvents
from .cognitive_trace import CognitiveTraceManager


class CognitiveMonitor:
    """
    Provides unified access to cognitive
    observability capabilities.
    """

    def __init__(self):
        self.metrics = CognitiveMetrics()
        self.events = CognitiveEvents()
        self.traces = CognitiveTraceManager()

    def record_metric(
        self,
        name: str,
        value: float,
        component: str,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        """
        Record cognitive metric.
        """

        return self.metrics.record(
            name=name,
            value=value,
            component=component,
            metadata=metadata,
        )

    def emit_event(
        self,
        event_type: str,
        source: str,
        payload: Optional[Dict[str, Any]] = None,
    ):
        """
        Emit cognitive event.
        """

        return self.events.emit(
            event_type=event_type,
            source=source,
            payload=payload,
        )

    def start_trace(
        self,
        operation: str,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        """
        Start cognitive trace.
        """

        return self.traces.start(
            operation=operation,
            metadata=metadata,
        )

    def add_trace_step(
        self,
        trace,
        step: str,
    ):
        """
        Add step to trace.
        """

        return self.traces.add_step(
            trace=trace,
            step=step,
        )

    def finish_trace(
        self,
        trace,
    ):
        """
        Finish trace.
        """

        return self.traces.finish(trace)

    def snapshot(self) -> Dict[str, int]:
        """
        Return current observability snapshot.
        """

        return {
            "metrics": self.metrics.count(),
            "events": self.events.count(),
            "traces": self.traces.count(),
        }
