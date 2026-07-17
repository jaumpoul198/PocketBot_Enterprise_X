from pocketbot.enterprise.intelligence.orchestration import (
    IntelligenceOrchestrator,
    IntelligenceOrchestrationResult,
)


def test_execute_returns_result():
    orchestrator = IntelligenceOrchestrator()

    result = orchestrator.execute(
        operation="refresh_intelligence_state",
        details={
            "source": "runtime",
        },
    )

    assert isinstance(result, IntelligenceOrchestrationResult)
    assert result.status == "completed"
    assert result.operation == "refresh_intelligence_state"
    assert result.executed is True
    assert result.details == {
        "source": "runtime",
    }


def test_result_to_dict():
    result = IntelligenceOrchestrationResult(
        status="completed",
        operation="sync_context",
        executed=True,
        details={
            "items": 10,
        },
    )

    assert result.to_dict() == {
        "status": "completed",
        "operation": "sync_context",
        "executed": True,
        "details": {
            "items": 10,
        },
    }


def test_from_mapping():
    orchestrator = IntelligenceOrchestrator()

    result = orchestrator.from_mapping(
        {
            "status": "completed",
            "operation": "analyze_events",
            "executed": True,
            "details": {
                "events": 100,
            },
        }
    )

    assert result.status == "completed"
    assert result.operation == "analyze_events"
    assert result.executed is True
    assert result.details == {
        "events": 100,
    }


def test_from_mapping_defaults():
    orchestrator = IntelligenceOrchestrator()

    result = orchestrator.from_mapping({})

    assert result.status == ""
    assert result.operation == ""
    assert result.executed is False
    assert result.details == {}
