from __future__ import annotations

import time


class RuntimeHistory:

    def __init__(self):
        self._history: list[dict] = []

    def add(
        self,
        state: str,
        metadata: dict | None = None,
    ) -> None:

        self._history.append(
            {
                "state": state,
                "timestamp": time.time(),
                "metadata": metadata,
            }
        )

    def latest(self) -> dict | None:
        if not self._history:
            return None

        return self._history[-1]

    def all(self) -> list[dict]:
        return list(self._history)
