from pocketbot.enterprise.intelligence.compliance import (
    IntelligenceCompliance,
    IntelligenceComplianceCheck,
)


def test_check_returns_compliance_check():
    compliance = IntelligenceCompliance()

    result = compliance.check(
        name="data_protection",
        compliant=True,
        severity="low",
        details={
            "audit": True,
        },
    )

    assert isinstance(result, IntelligenceComplianceCheck)
    assert result.name == "data_protection"
    assert result.compliant is True
    assert result.severity == "low"
    assert result.details == {
        "audit": True,
    }


def test_check_to_dict():
    result = IntelligenceComplianceCheck(
        name="security_review",
        compliant=False,
        severity="high",
        details={
            "issue": "missing_policy",
        },
    )

    assert result.to_dict() == {
        "name": "security_review",
        "compliant": False,
        "severity": "high",
        "details": {
            "issue": "missing_policy",
        },
    }


def test_from_mapping():
    compliance = IntelligenceCompliance()

    result = compliance.from_mapping(
        {
            "name": "governance_check",
            "compliant": True,
            "severity": "medium",
            "details": {
                "approved": True,
            },
        }
    )

    assert result.name == "governance_check"
    assert result.compliant is True
    assert result.severity == "medium"
    assert result.details == {
        "approved": True,
    }


def test_from_mapping_defaults():
    compliance = IntelligenceCompliance()

    result = compliance.from_mapping({})

    assert result.name == ""
    assert result.compliant is False
    assert result.severity == ""
    assert result.details == {}
