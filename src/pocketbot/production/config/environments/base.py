from dataclasses import dataclass


@dataclass(frozen=True)
class EnvironmentConfig:
    name: str
    debug: bool
    testing: bool
