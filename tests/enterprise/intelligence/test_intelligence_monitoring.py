from pocketbot.enterprise.intelligence.monitoring.intelligence_monitoring import (
    IntelligenceMonitoring,
)


def test_monitoring_default_creation():
    monitor = IntelligenceMonitoring()

    assert monitor.component == "enterprise_intelligence"
    assert monitor.status == "healthy"


def test_monitoring_run_check():
    monitor = IntelligenceMonitoring()

    result = monitor.run_check()

    assert isinstance(result, dict)
    assert result["status"] == "healthy"


def test_monitoring_to_dict():
    monitor = IntelligenceMonitoring(
        component="ai_engine",
        status="warning",
        events_checked=10,
        alerts=2,
    )

    data = monitor.to_dict()

    assert data["component"] == "ai_engine"
    assert data["alerts"] == 2


def test_monitoring_from_mapping():
    data = {
        "component": "scanner",
        "status": "active",
        "events_checked": 25,
    }

    monitor = IntelligenceMonitoring.from_mapping(data)

    assert monitor.component == "scanner"
    assert monitor.events_checked == 25
