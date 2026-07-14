from unittest.mock import Mock

import pytest

from pocketbot.market.services.market_connection_service import (
    MarketConnectionService,
)


def test_market_connection_start_connects_provider() -> None:
    provider = Mock()

    provider.is_connected.return_value = False

    service = MarketConnectionService(
        provider,
    )

    service.start()

    provider.connect.assert_called_once()


def test_market_connection_start_does_not_reconnect_existing_provider() -> None:
    provider = Mock()

    provider.is_connected.return_value = True

    service = MarketConnectionService(
        provider,
    )

    service.start()

    provider.connect.assert_not_called()


def test_market_connection_stop_disconnects_provider() -> None:
    provider = Mock()

    provider.is_connected.return_value = True

    service = MarketConnectionService(
        provider,
    )

    service.stop()

    provider.disconnect.assert_called_once()


def test_market_connection_stop_does_not_disconnect_inactive_provider() -> None:
    provider = Mock()

    provider.is_connected.return_value = False

    service = MarketConnectionService(
        provider,
    )

    service.stop()

    provider.disconnect.assert_not_called()


def test_market_connection_propagates_connect_failure() -> None:
    provider = Mock()

    provider.is_connected.return_value = False

    provider.connect.side_effect = RuntimeError(
        "connection failed",
    )

    service = MarketConnectionService(
        provider,
    )

    with pytest.raises(
        RuntimeError,
        match="connection failed",
    ):
        service.start()


def test_market_connection_propagates_disconnect_failure() -> None:
    provider = Mock()

    provider.is_connected.return_value = True

    provider.disconnect.side_effect = RuntimeError(
        "disconnect failed",
    )

    service = MarketConnectionService(
        provider,
    )

    with pytest.raises(
        RuntimeError,
        match="disconnect failed",
    ):
        service.stop()
