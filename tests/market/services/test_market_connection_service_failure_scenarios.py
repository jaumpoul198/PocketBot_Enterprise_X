from unittest.mock import Mock

import pytest

from pocketbot.market.services.market_connection_service import (
    MarketConnectionService,
)


def test_start_propagates_connection_state_check_failure() -> None:
    provider = Mock()

    provider.is_connected.side_effect = RuntimeError(
        "connection state unavailable",
    )

    service = MarketConnectionService(
        provider,
    )

    with pytest.raises(
        RuntimeError,
        match="connection state unavailable",
    ):
        service.start()


def test_stop_propagates_connection_state_check_failure() -> None:
    provider = Mock()

    provider.is_connected.side_effect = RuntimeError(
        "connection state unavailable",
    )

    service = MarketConnectionService(
        provider,
    )

    with pytest.raises(
        RuntimeError,
        match="connection state unavailable",
    ):
        service.stop()


def test_start_does_not_call_connect_when_provider_state_check_fails() -> None:
    provider = Mock()

    provider.is_connected.side_effect = RuntimeError(
        "state failure",
    )

    service = MarketConnectionService(
        provider,
    )

    with pytest.raises(RuntimeError):
        service.start()

    provider.connect.assert_not_called()


def test_stop_does_not_call_disconnect_when_provider_state_check_fails() -> None:
    provider = Mock()

    provider.is_connected.side_effect = RuntimeError(
        "state failure",
    )

    service = MarketConnectionService(
        provider,
    )

    with pytest.raises(RuntimeError):
        service.stop()

    provider.disconnect.assert_not_called()

def test_constructor_rejects_none_provider() -> None:
    with pytest.raises(
        ValueError,
        match="market_provider cannot be None",
    ):
        MarketConnectionService(
            None,
        )


def test_constructor_rejects_invalid_provider() -> None:
    with pytest.raises(
        TypeError,
        match="invalid market provider",
    ):
        MarketConnectionService(
            object(),
        )


def test_constructor_rejects_provider_without_required_methods() -> None:
    provider = object()

    with pytest.raises(
        TypeError,
        match="invalid market provider",
    ):
        MarketConnectionService(
            provider,
        )
