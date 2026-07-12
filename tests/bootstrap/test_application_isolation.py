from __future__ import annotations

from pocketbot.bootstrap.application import (
    build_application,
)
from pocketbot.infrastructure.audit import (
    AuditRegistry,
)
from pocketbot.infrastructure.metrics import (
    MetricsRegistry,
)


def test_application_bootstrap_creates_isolated_infrastructure_instances() -> None:
    first = build_application()
    second = build_application()

    assert first.get_service(
        MetricsRegistry,
    ) is not second.get_service(
        MetricsRegistry,
    )

    assert first.get_service(
        AuditRegistry,
    ) is not second.get_service(
        AuditRegistry,
    )
