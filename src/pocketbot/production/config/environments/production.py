from .base import EnvironmentConfig


production_environment = EnvironmentConfig(
    name="production",
    debug=False,
    testing=False,
)
