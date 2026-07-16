from pocketbot.enterprise.intelligence.context.context_memory import (
    ContextMemory,
)


def test_context_memory_remember():

    memory = ContextMemory()

    context = memory.remember(
        decision_id="memory-001",
        score=0.91,
        input_context={
            "asset": "XAUUSD"
        },
        feedback={
            "success": True
        },
    )

    assert context.decision_id == "memory-001"
    assert memory.size() == 1


def test_context_memory_recall():

    memory = ContextMemory()

    memory.remember(
        decision_id="memory-002",
        score=0.75,
    )

    result = memory.recall(
        "memory-002"
    )

    assert len(result) == 1
    assert result[0].score == 0.75


def test_context_memory_clear():

    memory = ContextMemory()

    memory.remember(
        decision_id="memory-003",
        score=0.60,
    )

    memory.clear()

    assert memory.size() == 0
