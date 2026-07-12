from .base import EnvironmentConfig


development_environment = EnvironmentConfig(
    name="development",
    debug=True,
    testing=True,
)
