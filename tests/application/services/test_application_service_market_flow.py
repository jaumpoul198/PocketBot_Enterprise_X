from datetime import datetime

from pocketbot.application.services.application_service import (
    ApplicationService,
)
from pocketbot.bootstrap.indicator_loader import load_indicators
from pocketbot.confluence.engine import ConfluenceEngine
from pocketbot.decision.engine import DecisionEngine
from pocketbot.domain.candle import Candle
from pocketbot.domain.value_objects.price import Price
from pocketbot.execution.engine import ExecutionEngine
from pocketbot.indicators.engine import IndicatorEngine
from pocketbot.indicators.factory import IndicatorFactory
from pocketbot.indicators.manager import IndicatorManager
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.market.cache.in_memory_market_cache import (
    InMemoryMarketCache,
)
from pocketbot.market.collectors.default_market_collector import (
    DefaultMarketCollector,
)
from pocketbot.market.providers.default_provider import (
    DefaultMarketProvider,
)
from pocketbot.market.validators.default_market_validator import (
    DefaultMarketValidator,
)
from pocketbot.risk.engine import RiskEngine
from pocketbot.score.engine import ScoreEngine
from pocketbot.trading.engine import TradeEngine


class MockMarketProvider(DefaultMarketProvider):
    def get_candles(
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
            for _ in range(count)
        ]


def test_application_service_uses_market_collector() -> None:
    collector = DefaultMarketCollector(
        MockMarketProvider(),
        DefaultMarketValidator(),
        InMemoryMarketCache(),
    )

    registry = load_indicators()

    pipeline = IndicatorPipeline(
        IndicatorManager(
            IndicatorEngine(
                IndicatorFactory(
                    registry,
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
        collector,
        pipeline,
        ConfluenceEngine(),
        ScoreEngine(),
        trade_engine,
    )

    result = service.analyse(
        "BTCUSDT",
        60,
        100,
    )

    assert result is not None
