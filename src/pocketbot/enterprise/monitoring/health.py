from __future__ import annotations


class HealthStatus:

    def __init__(self, runtime_metrics=None):
        self.runtime_metrics = runtime_metrics

    def health(self) -> dict:
        return {
            "status": "ok",
            "runtime": self.runtime_metrics.snapshot()
            if self.runtime_metrics
            else {},
        }

    def liveness(self) -> dict:
        return {
            "alive": True
        }

    def readiness(self) -> dict:
        return {
            "ready": True
        }
