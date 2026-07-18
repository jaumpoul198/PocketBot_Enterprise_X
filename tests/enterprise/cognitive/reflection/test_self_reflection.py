import pytest

from pocketbot.enterprise.cognitive.reflection import (
    SelfReflection,
)


def test_self_reflection_cycle():

    reflection = SelfReflection()

    result = reflection.reflect(
        decision_confidence=0.8,
        feedback={
            "success": True,
            "score": 0.9,
        },
    )

    assert result["analysis"]["success"] is True

    assert result["score"]["reflection_score"] == pytest.approx(
    0.85,
    rel=1e-9,
    )

def test_reflection_memory():

    reflection = SelfReflection()

    reflection.reflect(
        0.5,
        {
            "success": False,
            "score": 0.2,
        },
    )

    assert len(
        reflection.memory.all()
    ) == 1
