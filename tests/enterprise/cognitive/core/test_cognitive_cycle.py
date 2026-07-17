from pocketbot.enterprise.cognitive.core.cognitive_cycle import (
    CognitiveCycle,
)


def test_cycle_sequence():

    cycle = CognitiveCycle()

    assert cycle.next() == "PERCEIVE"
    assert cycle.next() == "PROCESS"
    assert cycle.next() == "DECIDE"
    assert cycle.next() == "LEARN"


def test_cycle_reset():

    cycle = CognitiveCycle()

    cycle.next()

    cycle.reset()

    assert cycle.next() == "PERCEIVE"
