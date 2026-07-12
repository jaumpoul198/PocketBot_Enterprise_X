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


def get_default_profile() -> dict[str, object]:
    """
    Return the default production configuration profile mapping.
    """

    return {
        "environment": "production",
        "debug": default_profile.debug,
        "service_name": default_profile.service_name,
    }
