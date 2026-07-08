from datetime import datetime

from pocketbot.application.services.application_service import (
    ApplicationService,
)
from pocketbot.application.services.market_service import (
    MarketService,
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
from pocketbot.market.interfaces.market_collector import (
    MarketCollector,
)
from pocketbot.risk.engine import RiskEngine
from pocketbot.score.engine import ScoreEngine
from pocketbot.trading.engine import TradeEngine


class MockMarketCollector(MarketCollector):
    def __init__(self) -> None:
        self.called = False

    def collect(
        self,
        asset: str,
        timeframe: int,
        count: int,
    ) -> list[Candle]:
        self.called = True

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


def test_application_service_uses_market_service() -> None:
    collector = MockMarketCollector()

    market_service = MarketService(
        collector,
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
        market_service,
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

    assert collector.called is True
    assert result is not None