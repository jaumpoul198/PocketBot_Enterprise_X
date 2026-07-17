from pocketbot.enterprise.intelligence.audit import (
    IntelligenceAudit,
    IntelligenceAuditRecord,
)


def test_record_returns_audit_record():
    audit = IntelligenceAudit()

    record = audit.record(
        event="intelligence_execution",
        actor="runtime",
        success=True,
        metadata={
            "module": "context",
        },
    )

    assert isinstance(record, IntelligenceAuditRecord)
    assert record.event == "intelligence_execution"
    assert record.actor == "runtime"
    assert record.success is True
    assert record.metadata == {
        "module": "context",
    }


def test_record_to_dict():
    record = IntelligenceAuditRecord(
        event="policy_validation",
        actor="governance",
        success=False,
        metadata={
            "reason": "missing_rule",
        },
    )

    assert record.to_dict() == {
        "event": "policy_validation",
        "actor": "governance",
        "success": False,
        "metadata": {
            "reason": "missing_rule",
        },
    }


def test_from_mapping():
    audit = IntelligenceAudit()

    record = audit.from_mapping(
        {
            "event": "compliance_check",
            "actor": "system",
            "success": True,
            "metadata": {
                "approved": True,
            },
        }
    )

    assert record.event == "compliance_check"
    assert record.actor == "system"
    assert record.success is True
    assert record.metadata == {
        "approved": True,
    }


def test_from_mapping_defaults():
    audit = IntelligenceAudit()

    record = audit.from_mapping({})

    assert record.event == ""
    assert record.actor == ""
    assert record.success is False
    assert record.metadata == {}
