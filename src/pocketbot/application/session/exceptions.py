"""
PocketBot Enterprise X

Trading session exceptions.
"""


class TradingSessionError(Exception):
    """
    Base trading session exception.
    """


class InvalidTradingSessionError(TradingSessionError):
    """
    Raised when a session operation is invalid.
    """
