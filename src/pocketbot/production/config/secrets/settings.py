from dataclasses import dataclass


@dataclass(frozen=True)
class SecretSettings:
    """
    Configuration for enterprise secret resolution.
    """

    provider: str = "environment"
