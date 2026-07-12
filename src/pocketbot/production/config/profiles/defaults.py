from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConfigurationProfile:
    service_name: str
    debug: bool


default_profile = ConfigurationProfile(
    service_name="pocketbot",
    debug=False,
)


def get_default_profile() -> ConfigurationProfile:
    """
    Return the default production configuration profile.
    """

    return default_profile
