from pocketbot.enterprise.intelligence.scoring import (
    IntelligenceScore,
    IntelligenceScoring,
)


def test_calculate_returns_score():
    scoring = IntelligenceScoring()

    score = scoring.calculate(
        name="runtime_health",
        value=0.95,
        threshold=0.90,
        metadata={
            "source": "production",
        },
    )

    assert isinstance(score, IntelligenceScore)
    assert score.name == "runtime_health"
    assert score.value == 0.95
    assert score.threshold == 0.90
    assert score.passed is True
    assert score.metadata == {
        "source": "production",
    }


def test_calculate_failed_score():
    scoring = IntelligenceScoring()

    score = scoring.calculate(
        name="performance",
        value=0.60,
        threshold=0.80,
    )

    assert score.passed is False


def test_score_to_dict():
    score = IntelligenceScore(
        name="security",
        value=1.0,
        threshold=0.95,
        passed=True,
        metadata={"alerts": 0},
    )

    assert score.to_dict() == {
        "name": "security",
        "value": 1.0,
        "threshold": 0.95,
        "passed": True,
        "metadata": {"alerts": 0},
    }


def test_from_mapping():
    scoring = IntelligenceScoring()

    score = scoring.from_mapping(
        {
            "name": "availability",
            "value": 0.99,
            "threshold": 0.95,
            "metadata": {
                "uptime": "99.9%",
            },
        }
    )

    assert score.name == "availability"
    assert score.value == 0.99
    assert score.threshold == 0.95
    assert score.passed is True
    assert score.metadata == {
        "uptime": "99.9%",
    }
