from pocketbot.enterprise.intelligence.analytics import (
    IntelligenceAnalytics,
    IntelligenceAnalyticsSnapshot,
)


def test_build_snapshot_returns_snapshot():
    analytics = IntelligenceAnalytics()

    snapshot = analytics.build_snapshot(
        total_events=12,
        total_contexts=5,
        total_memories=8,
        average_score=0.91,
    )

    assert isinstance(snapshot, IntelligenceAnalyticsSnapshot)
    assert snapshot.total_events == 12
    assert snapshot.total_contexts == 5
    assert snapshot.total_memories == 8
    assert snapshot.average_score == 0.91


def test_snapshot_to_dict():
    snapshot = IntelligenceAnalyticsSnapshot(
        total_events=1,
        total_contexts=2,
        total_memories=3,
        average_score=0.5,
    )

    assert snapshot.to_dict() == {
        "total_events": 1,
        "total_contexts": 2,
        "total_memories": 3,
        "average_score": 0.5,
    }


def test_from_mapping():
    analytics = IntelligenceAnalytics()

    snapshot = analytics.from_mapping(
        {
            "total_events": 20,
            "total_contexts": 10,
            "total_memories": 15,
            "average_score": 0.87,
        }
    )

    assert snapshot.total_events == 20
    assert snapshot.total_contexts == 10
    assert snapshot.total_memories == 15
    assert snapshot.average_score == 0.87


def test_from_mapping_defaults():
    analytics = IntelligenceAnalytics()

    snapshot = analytics.from_mapping({})

    assert snapshot.total_events == 0
    assert snapshot.total_contexts == 0
    assert snapshot.total_memories == 0
    assert snapshot.average_score == 0.0
