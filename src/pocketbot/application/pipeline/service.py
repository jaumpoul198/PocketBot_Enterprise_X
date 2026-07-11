"""
PocketBot Enterprise X

Trading Pipeline Service.
"""

from __future__ import annotations

from pocketbot.application.pipeline.exceptions import (
    TradingPipelineError,
)
from pocketbot.application.pipeline.models import (
    TradingRequest,
    TradingResult,
)
from pocketbot.application.pipeline.protocols import (
    TradingPipelineProtocol,
)
from pocketbot.application.services.market_query_service import (
    MarketQueryService,
)
from pocketbot.decision.engine import DecisionEngine
from pocketbot.indicators.pipeline import IndicatorPipeline
from pocketbot.market.strategy.service import StrategyService
from pocketbot.risk.interfaces.risk_service import (
    RiskService,
)
from pocketbot.risk.models.risk_assessment import (
    RiskStatus,
)
from pocketbot.score.engine import ScoreEngine


class TradingPipelineService(
    TradingPipelineProtocol,
):
    """
    Orchestrates complete trading analysis flow.
    """

    def __init__(
        self,
        market_query_service: MarketQueryService,
        indicator_pipeline: IndicatorPipeline,
        score_engine: ScoreEngine,
        strategy_service: StrategyService,
        decision_engine: DecisionEngine,
        risk_service: RiskService,
    ) -> None:

        self._market_query_service = (
            market_query_service
        )

        self._indicator_pipeline = (
            indicator_pipeline
        )

        self._score_engine = score_engine

        self._strategy_service = (
            strategy_service
        )

        self._decision_engine = (
            decision_engine
        )

        self._risk_service = risk_service

    def execute(
        self,
        request: TradingRequest,
    ) -> TradingResult:

        snapshot = (
            self._market_query_service.get_latest_market(
                request.asset,
                request.timeframe,
            )
        )

        if snapshot is None:
            raise TradingPipelineError(
                "Market snapshot not found."
            )

        indicators = (
            self._indicator_pipeline.execute(
                request.indicators,
                snapshot.candles,
            )
        )

        score = (
            self._score_engine.calculate(
                indicators,
            )
        )

        strategies = (
            self._strategy_service.analyze(
                snapshot,
            )
        )

        strategy = (
            strategies[0]
            if strategies
            else None
        )

        decision = (
            self._decision_engine.decide(
                score,
                strategy,
            )
        )

        risk = self._risk_service.evaluate(
            position_size=1.0,
            current_exposure=0.0,
        )

        metadata = {}

        if risk.status is RiskStatus.REJECTED:
            metadata["blocked_by_risk"] = True

        return TradingResult(
            market=snapshot,
            indicators=indicators,
            score=score,
            strategy=strategy,
            decision=decision,
            risk=risk,
            metadata=metadata,
        )
