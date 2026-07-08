"""
PocketBot Enterprise X

Application Service Bootstrap.
"""

from __future__ import annotations

from pocketbot.application.services.application_service import ApplicationService
from pocketbot.bootstrap.application import build_indicator_pipeline
from pocketbot.confluence.engine import ConfluenceEngine
from pocketbot.decision.engine import DecisionEngine
from pocketbot.execution.engine import ExecutionEngine
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.application.services.market_service import (
    MarketService,
)
from pocketbot.risk.engine import RiskEngine
from pocketbot.score.engine import ScoreEngine
from pocketbot.trading.engine import TradeEngine


def build_application_service(
    market: MarketService,
) -> ApplicationService:
    """
    Builds the complete application service.
    """

    pipeline: IndicatorPipeline = build_indicator_pipeline()

    decision_engine = DecisionEngine()

    risk_engine = RiskEngine()

    execution_engine = ExecutionEngine()

    trade_engine = TradeEngine(
        decision=decision_engine,
        risk=risk_engine,
        execution=execution_engine,
    )

    return ApplicationService(
        market=market,
        pipeline=pipeline,
        confluence=ConfluenceEngine(),
        score_engine=ScoreEngine(),
        trade_engine=trade_engine,
    )