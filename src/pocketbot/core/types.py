"""
PocketBot Enterprise X
Core - Types

Tipos compartilhados por todo o sistema.
"""

from __future__ import annotations

from typing import Any, TypeAlias

JSON: TypeAlias = dict[str, Any]

Number: TypeAlias = int | float

Candle: TypeAlias = dict[str, Any]

Signal: TypeAlias = dict[str, Any]

StrategyResult: TypeAlias = dict[str, Any]

IndicatorResult: TypeAlias = dict[str, Any]

Metadata: TypeAlias = dict[str, Any]
