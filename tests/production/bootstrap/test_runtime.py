from pocketbot.production.bootstrap.runtime import ProductionRuntime
from pocketbot.production.config.settings import ProductionSettings


def test_production_runtime_lifecycle() -> None:
    settings = ProductionSettings()
    runtime = ProductionRuntime(settings)

    assert runtime.settings == settings
    assert runtime.started is False

    assert runtime.start() is True
    assert runtime.started is True

    assert runtime.shutdown() is True
    assert runtime.started is False
