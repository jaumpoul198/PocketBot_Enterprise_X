from datetime import datetime

from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)
from pocketbot.market.interfaces.market_collector import (
    MarketCollector,
)
from pocketbot.market.interfaces.market_validator import (
    MarketValidator,
)
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)


class MockInvalidMarketCollector(MarketCollector):
    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        return [
            Candle(
                symbol=asset,
                timeframe=str(timeframe),
                open=Price(100.0),
                high=Price(105.0),
                low=Price(95.0),
                close=Price(102.0),
                volume=1000.0,
                timestamp=datetime.now(),
            )
        ]


class RejectingMarketValidator(MarketValidator):
    def validate(
        self,
        candles: list[Candle],
    ) -> bool:
        return False


def test_market_service_returns_empty_when_validation_fails() -> None:
    collector = MockInvalidMarketCollector()

    cache = InMemoryMarketCache()
    repository = InMemoryMarketRepository()
    validator = RejectingMarketValidator()

    service = MarketService(
        collector,
        cache,
        repository,
        validator,
    )

    result = service.refresh_market(
        "BTCUSDT",
        60,
        1,
    )

    assert result == []

    cached = cache.load(
        "BTCUSDT",
        60,
    )

    assert cached == []
