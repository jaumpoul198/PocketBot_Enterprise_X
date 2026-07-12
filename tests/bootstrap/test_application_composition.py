from __future__ import annotations

from pocketbot.application.pipeline.service import (
    TradingPipelineService,
)
from pocketbot.application.runtime.application_runtime import (
    ApplicationRuntime,
)
from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.bootstrap.application import (
    build_application,
)
from pocketbot.infrastructure.audit import (
    AuditRegistry,
)
from pocketbot.infrastructure.health import (
    HealthRegistry,
)
from pocketbot.infrastructure.metrics import (
    MetricsRegistry,
)
from pocketbot.infrastructure.observability import (
    RuntimeObservabilityHandler,
)


def test_application_bootstrap_resolves_enterprise_components() -> None:
    provider = build_application()

    assert isinstance(
        provider.get_service(HealthRegistry),
        HealthRegistry,
    )

    assert isinstance(
        provider.get_service(MetricsRegistry),
        MetricsRegistry,
    )

    assert isinstance(
        provider.get_service(AuditRegistry),
        AuditRegistry,
    )

    assert isinstance(
        provider.get_service(RuntimeObservabilityHandler),
        RuntimeObservabilityHandler,
    )

    assert isinstance(
        provider.get_service(ApplicationRuntime),
        ApplicationRuntime,
    )

    assert isinstance(
        provider.get_service(TradingPipelineService),
        TradingPipelineService,
    )

    assert isinstance(
        provider.get_service(MarketService),
        MarketService,
    )
