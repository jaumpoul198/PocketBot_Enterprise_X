"""
PocketBot Enterprise X
Core - Enums
"""

from enum import Enum


class SignalDirection(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    WAIT = "WAIT"


class ConfidenceLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Environment(str, Enum):
    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"