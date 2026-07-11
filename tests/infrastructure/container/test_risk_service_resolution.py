"""
PocketBot Enterprise X

Risk service container resolution test.
"""

from pocketbot.bootstrap.service_registration import (
    register_services,
)
from pocketbot.infrastructure.container.service_collection import (
    ServiceCollection,
)
from pocketbot.risk.interfaces.risk_service import (
    RiskService,
)
from pocketbot.risk.services.default_risk_service import (
    DefaultRiskService,
)


def test_risk_service_is_resolvable_from_container():

    services = ServiceCollection()

    register_services(services)

    provider = services.build_provider()

    risk_service = provider.get_service(
        RiskService,
    )

    assert isinstance(
        risk_service,
        DefaultRiskService,
    )
