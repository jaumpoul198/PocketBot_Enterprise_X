from pocketbot.production.startup.validator import validate_startup


def test_startup_validation() -> None:
    result = validate_startup()

    assert result.valid is True
    assert "configuration" in result.checks
    assert "dependencies" in result.checks


def test_startup_checks_count() -> None:
    result = validate_startup()

    assert len(result.checks) == 3
