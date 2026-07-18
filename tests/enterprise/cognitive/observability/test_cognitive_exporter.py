from pocketbot.enterprise.cognitive.observability.cognitive_monitor import (
    CognitiveMonitor,
)

from pocketbot.enterprise.cognitive.observability.cognitive_dashboard import (
    CognitiveDashboard,
)

from pocketbot.enterprise.cognitive.observability.cognitive_exporter import (
    CognitiveExporter,
)


def test_export_dict():
    monitor = CognitiveMonitor()

    dashboard = CognitiveDashboard(
        monitor,
    )

    exporter = CognitiveExporter(
        dashboard,
    )

    monitor.record_metric(
        name="confidence",
        value=0.95,
        component="decision",
    )

    data = exporter.export_dict()

    assert "summary" in data
    assert "metrics" in data
    assert len(data["metrics"]) == 1


def test_export_json():
    monitor = CognitiveMonitor()

    dashboard = CognitiveDashboard(
        monitor,
    )

    exporter = CognitiveExporter(
        dashboard,
    )

    result = exporter.export_json()

    assert isinstance(result, str)
    assert "summary" in result
