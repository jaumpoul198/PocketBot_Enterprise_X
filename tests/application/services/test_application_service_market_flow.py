from datetime import datetime

from pocketbot.application.services.application_service import (
    ApplicationService,
)
from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.bootstrap.indicator_loader import (
    load_indicators,
)
from pocketbot.confluence.engine import (
    ConfluenceEngine,
)
from pocketbot.decision.engine import (
    DecisionEngine,
)
from pocketbot.domain.candle import (
    Candle,
)
from pocketbot.domain.value_objects.price import (
    Price,
)
from pocketbot.execution.engine import (
    ExecutionEngine,
)
from pocketbot.indicators.engine import (
    IndicatorEngine,
)
from pocketbot.indicators.factory import (
    IndicatorFactory,
)
from pocketbot.indicators.manager import (
    IndicatorManager,
)
from pocketbot.indicators.pipeline import (
    IndicatorPipeline,
)
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
from pocketbot.risk.engine import (
    RiskEngine,
)
from pocketbot.score.engine import (
    ScoreEngine,
)
from pocketbot.trading.engine import (
    TradeEngine,
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
                open=Price(100.0 + i),
                high=Price(105.0 + i),
                low=Price(95.0 + i),
                close=Price(102.0 + i),
                volume=1000.0,
                timestamp=datetime.now(),
            )
            for i in range(100)
        ]

def test_application_service_uses_market_service() -> None:

    collector = MockMarketCollector()

    market_service = MarketService(
        collector,
        InMemoryMarketCache(),
        InMemoryMarketRepository(),
        DefaultMarketValidator(),
    )

    pipeline = IndicatorPipeline(
        IndicatorManager(
            IndicatorEngine(
                IndicatorFactory(
                    load_indicators(),
                ),
            ),
        ),
    )

    trade_engine = TradeEngine(
        DecisionEngine(),
        RiskEngine(),
        ExecutionEngine(),
    )

    service = ApplicationService(
        market_service,
        pipeline,
        ConfluenceEngine(),
        ScoreEngine(),
        trade_engine,
    )

    result = service.analyse(
        asset="BTCUSDT",
        timeframe=60,
        candles=100,
    )

    assert collector.called is True
    assert collector.asset == "BTCUSDT"
    assert collector.timeframe == 60
