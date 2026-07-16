from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeHealth:
    """
    Enterprise runtime health state.
    """

    healthy: bool
    runtime_running: bool
    autonomy_running: bool


class RuntimeHealthSupervisor:
    """
    Evaluates enterprise runtime health.
    """

    def evaluate(
        self,
        runtime_running: bool,
        autonomy_running: bool,
    ) -> RuntimeHealth:
        return RuntimeHealth(
            healthy=runtime_running and autonomy_running,
            runtime_running=runtime_running,
            autonomy_running=autonomy_running,
        )
