from datetime import datetime, UTC

from .consolidation import MemoryConsolidation

from .memory_models import (
    CognitiveKnowledge,
    CognitiveMemoryEntry,
)


class CognitiveMemory:

    def __init__(self):

        self._memory = []

        self._knowledge = []

        self.consolidator = MemoryConsolidation()

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

    def consolidate(
        self,
        source: str,
        pattern: str,
        score: float,
    ):

        knowledge = CognitiveKnowledge(
            source=source,
            pattern=pattern,
            score=score,
            created_at=datetime.now(UTC),
        )

        self._knowledge.append(
            knowledge
        )

        return knowledge

    def knowledge(self):

        return self._knowledge

    def knowledge_count(self):

        return len(
            self._knowledge
        )

    def consolidate_experiences(self):

        memories = self.consolidator.evaluate(
            self._memory
        )

        for memory in memories:

            self.consolidate(
                source="memory",
                pattern=memory.action,
                score=memory.confidence,
            )

        return memories
