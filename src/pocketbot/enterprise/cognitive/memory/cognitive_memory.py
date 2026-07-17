from datetime import datetime, UTC

from .memory_models import CognitiveMemoryEntry


class CognitiveMemory:

    def __init__(self):
        self._memory = []

    def remember(
        self,
        cycle: str,
        action: str,
        confidence: float,
    ):

        entry = CognitiveMemoryEntry(
            cycle=cycle,
            action=action,
            confidence=confidence,
            timestamp=datetime.now(UTC),
        )

        self._memory.append(entry)

        return entry

    def latest(self):

        if not self._memory:
            return None

        return self._memory[-1]

    def all(self):

        return self._memory

    def history(self):

        return self._memory

    def count(self):

        return len(self._memory)

    def clear(self):

        self._memory.clear()
