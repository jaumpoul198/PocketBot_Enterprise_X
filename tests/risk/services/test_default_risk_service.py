"""
PocketBot Enterprise X

Tests for default risk service.
"""

from pocketbot.risk.interfaces.risk_service import (
    RiskService,
)
from pocketbot.risk.models.risk_assessment import (
    RiskStatus,
)
from pocketbot.risk.services.default_risk_service import (
    DefaultRiskService,
)


def test_default_risk_service_implements_contract() -> None:

    service = DefaultRiskService()

    assert isinstance(
        service,
        RiskService,
    )


def test_risk_service_approves_valid_operation() -> None:

    service = DefaultRiskService()

    result = service.evaluate(
        position_size=0.5,
        current_exposure=0.2,
    )

    assert result.status is RiskStatus.APPROVED
    assert result.approved is True


def test_risk_service_rejects_position_limit() -> None:

    service = DefaultRiskService()

    result = service.evaluate(
        position_size=2.0,
        current_exposure=0.2,
    )

    assert result.status is RiskStatus.REJECTED
    assert result.approved is False


def test_risk_service_rejects_exposure_limit() -> None:

    service = DefaultRiskService()

    result = service.evaluate(
        position_size=0.5,
        current_exposure=0.8,
    )

    assert result.status is RiskStatus.REJECTED
    assert result.approved is False
