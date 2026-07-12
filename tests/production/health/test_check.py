from pocketbot.production.health.check import check_health


def test_health_check_default() -> None:
    status = check_health()

    assert status.healthy is True
    assert status.service == "pocketbot"


def test_health_check_custom_service() -> None:
    status = check_health("enterprise")

    assert status.healthy is True
    assert status.service == "enterprise"


def test_health_check_returns_frozen_status() -> None:
    status = check_health()

    assert status.healthy is True
