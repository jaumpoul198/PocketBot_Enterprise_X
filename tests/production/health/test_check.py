

def test_health_check_returns_frozen_status() -> None:
    status = check_health()

    assert status.healthy
