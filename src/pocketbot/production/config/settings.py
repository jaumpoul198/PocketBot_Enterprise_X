from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductionSettings:
    environment: str = "production"
    debug: bool = False
    service_name: str = "pocketbot"
