from pocketbot.production.entrypoint.application import (
    create_production_runtime,
    run_production,
)


def test_create_production_runtime() -> None:
    runtime = create_production_runtime()

    assert runtime.settings.environment == "production"


def test_run_production() -> None:
    assert run_production() is True
