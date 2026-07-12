from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProductionMetrics:
    counters: dict[str, int] = field(default_factory=dict)

    def increment(self, name: str) -> None:
        self.counters[name] = self.counters.get(name, 0) + 1

    def get(self, name: str) -> int:
        return self.counters.get(name, 0)
