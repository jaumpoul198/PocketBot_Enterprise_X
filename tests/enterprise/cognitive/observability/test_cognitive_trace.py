from pocketbot.enterprise.cognitive.observability.cognitive_trace import (
    CognitiveTraceManager,
)


def test_start_trace():
    manager = CognitiveTraceManager()

    trace = manager.start(
        operation="planning",
    )

    assert trace.operation == "planning"
    assert manager.count() == 1


def test_add_step_to_trace():
    manager = CognitiveTraceManager()

    trace = manager.start(
        operation="runtime",
    )

    manager.add_step(
        trace,
        "analyze_context",
    )

    manager.add_step(
        trace,
        "execute_plan",
    )

    assert trace.steps == [
        "analyze_context",
        "execute_plan",
    ]


def test_finish_trace():
    manager = CognitiveTraceManager()

    trace = manager.start(
        operation="decision",
    )

    result = manager.finish(trace)

    assert result.finished_at is not None


def test_latest_trace():
    manager = CognitiveTraceManager()

    manager.start(
        operation="memory",
    )

    manager.start(
        operation="planning",
    )

    latest = manager.latest()

    assert latest.operation == "planning"
