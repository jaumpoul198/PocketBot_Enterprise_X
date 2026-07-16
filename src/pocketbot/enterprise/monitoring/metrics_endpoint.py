from __future__ import annotations


class MetricsEndpoint:

    def __init__(self, runtime_metrics=None):
        self.runtime_metrics = runtime_metrics

    def metrics(self) -> dict:
        if self.runtime_metrics:
            return self.runtime_metrics.snapshot()

        return {}
