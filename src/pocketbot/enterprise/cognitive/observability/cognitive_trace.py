"""
PocketBot Enterprise X
Cognitive Trace Manager

Tracks execution flow through
cognitive processing stages.
"""

from typing import Any, Dict, List, Optional

from .observability_models import CognitiveTrace


class CognitiveTraceManager:
    """
    Manages cognitive execution traces.
    """

    def __init__(self):
        self._traces: List[CognitiveTrace] = []

    def start(
        self,
        operation: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> CognitiveTrace:
        """
        Start a new cognitive trace.
        """

        trace = CognitiveTrace(
            operation=operation,
            metadata=metadata or {},
        )

        self._traces.append(trace)

        return trace

    def add_step(
        self,
        trace: CognitiveTrace,
        step: str,
    ) -> CognitiveTrace:
        """
        Add execution step to trace.
        """

        trace.add_step(step)

        return trace

    def finish(
        self,
        trace: CognitiveTrace,
    ) -> CognitiveTrace:
        """
        Finish cognitive trace.
        """

        trace.finish()

        return trace

    def get_all(self) -> List[CognitiveTrace]:
        """
        Return all traces.
        """

        return list(self._traces)

    def latest(
        self,
        operation: Optional[str] = None,
    ) -> Optional[CognitiveTrace]:
        """
        Return latest trace.
        """

        for trace in reversed(self._traces):
            if operation is None or trace.operation == operation:
                return trace

        return None

    def count(self) -> int:
        """
        Return total traces stored.
        """

        return len(self._traces)
