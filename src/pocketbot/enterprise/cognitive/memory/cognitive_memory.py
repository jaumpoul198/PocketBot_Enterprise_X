from datetime import datetime, UTC

from .memory_models import CognitiveMemoryEntry


class CognitiveMemory:

    def __init__(self):
        self.entries = []

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

        self.entries.append(entry)

        return entry

    def latest(self):

        return self.entries[-1] if self.entries else None

    def all(self):

        return list(self.entries)
