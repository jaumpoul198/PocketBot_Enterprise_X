from pocketbot.enterprise.intelligence.dashboard import (
    IntelligenceDashboard,
    IntelligenceDashboardSnapshot,
)


def test_build_snapshot_returns_snapshot():
    dashboard = IntelligenceDashboard()

    snapshot = dashboard.build_snapshot(
        title="Enterprise Dashboard",
        generated_at="2026-07-17T10:00:00Z",
        widgets={
            "events": 120,
            "contexts": 35,
            "health": "healthy",
        },
    )

    assert isinstance(snapshot, IntelligenceDashboardSnapshot)
    assert snapshot.title == "Enterprise Dashboard"
    assert snapshot.generated_at == "2026-07-17T10:00:00Z"
    assert snapshot.widgets == {
        "events": 120,
        "contexts": 35,
        "health": "healthy",
    }


def test_snapshot_to_dict():
    snapshot = IntelligenceDashboardSnapshot(
        title="Daily Dashboard",
        generated_at="2026-07-17",
        widgets={"events": 10},
    )

    assert snapshot.to_dict() == {
        "title": "Daily Dashboard",
        "generated_at": "2026-07-17",
        "widgets": {"events": 10},
    }


def test_from_mapping():
    dashboard = IntelligenceDashboard()

    snapshot = dashboard.from_mapping(
        {
            "title": "Weekly Dashboard",
            "generated_at": "2026-07-17T12:00:00Z",
            "widgets": {
                "events": 250,
                "contexts": 70,
            },
        }
    )

    assert snapshot.title == "Weekly Dashboard"
    assert snapshot.generated_at == "2026-07-17T12:00:00Z"
    assert snapshot.widgets == {
        "events": 250,
        "contexts": 70,
    }


def test_from_mapping_defaults():
    dashboard = IntelligenceDashboard()

    snapshot = dashboard.from_mapping({})

    assert snapshot.title == ""
    assert snapshot.generated_at == ""
    assert snapshot.widgets == {}
