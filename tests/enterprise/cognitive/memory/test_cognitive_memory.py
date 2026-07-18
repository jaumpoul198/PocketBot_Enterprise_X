from pocketbot.enterprise.cognitive.memory.cognitive_memory import (
    CognitiveMemory,
)


def test_cognitive_memory_store():

    memory = CognitiveMemory()

    entry = memory.remember(
        cycle="PERCEIVE",
        action="observe",
        confidence=1.0,
    )

    assert entry.cycle == "PERCEIVE"

    assert memory.latest() == entry

    assert len(memory.all()) == 1
