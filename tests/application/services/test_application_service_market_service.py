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
from pocketbot.market.repositories.in_memory_market_repository import (
    InMemoryMarketRepository,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)


class MockMarketCollector(MarketCollector):
    def __init__(self) -> None:
        self.called = False
        self.asset = ""
        self.timeframe = 0
        self.count = 0

    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        self.called = True
        self.asset = asset
        self.timeframe = timeframe
        self.count = count

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


def test_market_service_refresh_market_delegates_to_collector() -> None:
    collector = MockMarketCollector()

    cache = InMemoryMarketCache()
    repository = InMemoryMarketRepository()
    validator = DefaultMarketValidator()

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

    assert collector.called is True
    assert collector.asset == "BTCUSDT"
    assert collector.timeframe == 60
    assert collector.count == 1
    assert len(result) == 1