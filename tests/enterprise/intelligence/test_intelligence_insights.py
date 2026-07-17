from pocketbot.enterprise.intelligence.insights import (
    IntelligenceInsight,
    IntelligenceInsights,
)


def test_build_insight_returns_insight():
    insights = IntelligenceInsights()

    insight = insights.build_insight(
        category="performance",
        summary="Runtime operating normally",
        confidence=0.95,
        metadata={
            "events": 120,
            "health": "healthy",
        },
    )

    assert isinstance(insight, IntelligenceInsight)
    assert insight.category == "performance"
    assert insight.summary == "Runtime operating normally"
    assert insight.confidence == 0.95
    assert insight.metadata == {
        "events": 120,
        "health": "healthy",
    }


def test_insight_to_dict():
    insight = IntelligenceInsight(
        category="security",
        summary="No anomalies detected",
        confidence=0.98,
        metadata={"alerts": 0},
    )

    assert insight.to_dict() == {
        "category": "security",
        "summary": "No anomalies detected",
        "confidence": 0.98,
        "metadata": {"alerts": 0},
    }


def test_from_mapping():
    insights = IntelligenceInsights()

    insight = insights.from_mapping(
        {
            "category": "operations",
            "summary": "System stable",
            "confidence": 0.91,
            "metadata": {
                "uptime": "99.9%",
            },
        }
    )

    assert insight.category == "operations"
    assert insight.summary == "System stable"
    assert insight.confidence == 0.91
    assert insight.metadata == {
        "uptime": "99.9%",
    }


def test_from_mapping_defaults():
    insights = IntelligenceInsights()

    insight = insights.from_mapping({})

    assert insight.category == ""
    assert insight.summary == ""
    assert insight.confidence == 0.0
    assert insight.metadata == {}
