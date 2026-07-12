from pocketbot.production.bootstrap.health import (
    ProductionHealth,
)


def test_production_health() -> None:
    health = ProductionHealth()

    status = health.check()

    assert status.healthy is True
    assert status.service == "pocketbot"
