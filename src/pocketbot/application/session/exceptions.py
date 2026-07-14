"""
PocketBot Enterprise X

Trading session exceptions.
"""

from pocketbot.core.exceptions import (
    PocketBotError,
)


class TradingSessionError(PocketBotError):
    """
    Base trading session exception.
    """


class InvalidTradingSessionError(TradingSessionError):
    """
    Raised when a session operation is invalid.
    """


class TradingSessionExecutionError(TradingSessionError):
    """
    Raised when a trading session execution fails.
    """