from pocketbot.production.api.intelligence_routes import (
    IntelligenceAPI,
)


def test_intelligence_autonomy():

    api = IntelligenceAPI()

    api.decision()

    result = api.autonomy()

    assert "autonomy_score" in result
    assert "decision_count" in result
    assert result["decision_count"] == 1
