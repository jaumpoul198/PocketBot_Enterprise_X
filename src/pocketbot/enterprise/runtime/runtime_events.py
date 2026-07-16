from __future__ import annotations

import time
from dataclasses import dataclass


@dataclass
class RuntimeEvent:
    name: str
    timestamp: float
    metadata: dict | None = None


class RuntimeEvents:

    def __init__(self):
        self._events: list[RuntimeEvent] = []

    def record(
        self,
        name: str,
        metadata: dict | None = None,
    ) -> None:

        self._events.append(
            RuntimeEvent(
                name=name,
                timestamp=time.time(),
                metadata=metadata,
            )
        )

    def all(self) -> list[RuntimeEvent]:
        return list(self._events)

    def count(self) -> int:
        return len(self._events)
