from pocketbot.enterprise.intelligence.governance import (
    IntelligenceGovernance,
    IntelligenceGovernancePolicy,
)


def test_create_policy_returns_policy():
    governance = IntelligenceGovernance()

    policy = governance.create_policy(
        name="data_access_policy",
        level="enterprise",
        enabled=True,
        rules={
            "audit": True,
            "retention_days": 90,
        },
    )

    assert isinstance(policy, IntelligenceGovernancePolicy)
    assert policy.name == "data_access_policy"
    assert policy.level == "enterprise"
    assert policy.enabled is True
    assert policy.rules == {
        "audit": True,
        "retention_days": 90,
    }


def test_policy_to_dict():
    policy = IntelligenceGovernancePolicy(
        name="security_policy",
        level="high",
        enabled=True,
        rules={
            "encryption": True,
        },
    )

    assert policy.to_dict() == {
        "name": "security_policy",
        "level": "high",
        "enabled": True,
        "rules": {
            "encryption": True,
        },
    }


def test_from_mapping():
    governance = IntelligenceGovernance()

    policy = governance.from_mapping(
        {
            "name": "compliance_policy",
            "level": "enterprise",
            "enabled": True,
            "rules": {
                "approval_required": True,
            },
        }
    )

    assert policy.name == "compliance_policy"
    assert policy.level == "enterprise"
    assert policy.enabled is True
    assert policy.rules == {
        "approval_required": True,
    }


def test_from_mapping_defaults():
    governance = IntelligenceGovernance()

    policy = governance.from_mapping({})

    assert policy.name == ""
    assert policy.level == ""
    assert policy.enabled is False
    assert policy.rules == {}
