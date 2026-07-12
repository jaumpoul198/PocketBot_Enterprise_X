from pocketbot.production.bootstrap.runtime import ProductionRuntime
from pocketbot.production.config.settings import ProductionSettings


def test_production_runtime_lifecycle() -> None:
    settings = ProductionSettings()
    runtime = ProductionRuntime(settings)

    assert runtime.settings == settings
    assert runtime.start() is True
    assert runtime.shutdown() is True
