from pocketbot.enterprise.intelligence.recommendations import (
    IntelligenceRecommendation,
    IntelligenceRecommendations,
)


def test_build_recommendation_returns_recommendation():
    recommendations = IntelligenceRecommendations()

    recommendation = recommendations.build_recommendation(
        action="optimize_runtime",
        reason="High resource utilization detected",
        priority="high",
        confidence=0.92,
        metadata={
            "cpu": 85,
            "memory": 70,
        },
    )

    assert isinstance(recommendation, IntelligenceRecommendation)
    assert recommendation.action == "optimize_runtime"
    assert recommendation.reason == "High resource utilization detected"
    assert recommendation.priority == "high"
    assert recommendation.confidence == 0.92
    assert recommendation.metadata == {
        "cpu": 85,
        "memory": 70,
    }


def test_recommendation_to_dict():
    recommendation = IntelligenceRecommendation(
        action="review_policy",
        reason="Threshold exceeded",
        priority="medium",
        confidence=0.80,
        metadata={"source": "analytics"},
    )

    assert recommendation.to_dict() == {
        "action": "review_policy",
        "reason": "Threshold exceeded",
        "priority": "medium",
        "confidence": 0.80,
        "metadata": {"source": "analytics"},
    }


def test_from_mapping():
    recommendations = IntelligenceRecommendations()

    recommendation = recommendations.from_mapping(
        {
            "action": "scale_service",
            "reason": "Traffic increase",
            "priority": "high",
            "confidence": 0.95,
            "metadata": {
                "instances": 3,
            },
        }
    )

    assert recommendation.action == "scale_service"
    assert recommendation.reason == "Traffic increase"
    assert recommendation.priority == "high"
    assert recommendation.confidence == 0.95
    assert recommendation.metadata == {
        "instances": 3,
    }


def test_from_mapping_defaults():
    recommendations = IntelligenceRecommendations()

    recommendation = recommendations.from_mapping({})

    assert recommendation.action == ""
    assert recommendation.reason == ""
    assert recommendation.priority == ""
    assert recommendation.confidence == 0.0
    assert recommendation.metadata == {}
