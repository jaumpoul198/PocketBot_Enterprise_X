from flask import Blueprint, jsonify

from pocketbot.enterprise.intelligence.context.context_runtime import (
    ContextRuntime,
)

from pocketbot.enterprise.intelligence.context.context_metrics import (
    ContextMetrics,
)


intelligence_bp = Blueprint(
    "intelligence",
    __name__,
    url_prefix="/intelligence",
)


context_runtime = ContextRuntime()
context_metrics = ContextMetrics()


@intelligence_bp.route("/status", methods=["GET"])
def intelligence_status():

    return jsonify(
        {
            "module": "enterprise_intelligence",
            "status": "active",
            "contexts": context_runtime.get_context_count(),
        }
    )


@intelligence_bp.route("/context/history", methods=["GET"])
def context_history():

    history = context_runtime.get_context_history()

    return jsonify(
        {
            "count": len(history),
            "history": [
                {
                    "decision_id": item.decision_id,
                    "score": item.score,
                }
                for item in history
            ],
        }
    )


@intelligence_bp.route("/context/metrics", methods=["GET"])
def context_metrics_status():

    return jsonify(
        context_metrics.snapshot()
    )
