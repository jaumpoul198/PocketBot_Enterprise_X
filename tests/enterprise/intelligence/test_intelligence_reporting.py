from pocketbot.enterprise.intelligence.reporting import (
    IntelligenceReport,
    IntelligenceReporting,
)


def test_build_report_returns_report():
    reporting = IntelligenceReporting()

    report = reporting.build_report(
        title="Enterprise Summary",
        generated_at="2026-07-17T10:00:00Z",
        metrics={
            "events": 120,
            "contexts": 35,
            "average_score": 0.94,
        },
    )

    assert isinstance(report, IntelligenceReport)
    assert report.title == "Enterprise Summary"
    assert report.generated_at == "2026-07-17T10:00:00Z"
    assert report.metrics == {
        "events": 120,
        "contexts": 35,
        "average_score": 0.94,
    }


def test_report_to_dict():
    report = IntelligenceReport(
        title="Daily",
        generated_at="2026-07-17",
        metrics={"events": 10},
    )

    assert report.to_dict() == {
        "title": "Daily",
        "generated_at": "2026-07-17",
        "metrics": {"events": 10},
    }


def test_from_mapping():
    reporting = IntelligenceReporting()

    report = reporting.from_mapping(
        {
            "title": "Weekly",
            "generated_at": "2026-07-17T12:00:00Z",
            "metrics": {
                "events": 250,
                "contexts": 70,
            },
        }
    )

    assert report.title == "Weekly"
    assert report.generated_at == "2026-07-17T12:00:00Z"
    assert report.metrics == {
        "events": 250,
        "contexts": 70,
    }


def test_from_mapping_defaults():
    reporting = IntelligenceReporting()

    report = reporting.from_mapping({})

    assert report.title == ""
    assert report.generated_at == ""
    assert report.metrics == {}
