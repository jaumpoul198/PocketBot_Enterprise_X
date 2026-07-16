from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from pocketbot.production.api.health_models import (
    HealthResponse,
)
from pocketbot.production.health.service import (
    ProductionHealthService,
)
from pocketbot.production.api.intelligence_routes import (
    IntelligenceAPI,
)

class HealthRequestHandler(BaseHTTPRequestHandler):
    """
    HTTP handler for production health endpoints.
    """

    health_service: ProductionHealthService | None = None

    intelligence_api: IntelligenceAPI | None = None

    def do_GET(self) -> None:
        if self.health_service is None:
            self._send_response(
                503,
                {
                    "status": "unavailable",
                },
            )
            return

        if self.path == "/health":
            result = self.health_service.health()

        elif self.path == "/readiness":
            result = self.health_service.readiness()

        elif self.path == "/liveness":
            result = self.health_service.liveness()

        elif self.path == "/api/intelligence/status":
            result = self.intelligence_api.status()

        elif self.path == "/api/intelligence/decision":
            result = self.intelligence_api.decision()

        elif self.path == "/api/intelligence/signals":
            result = self.intelligence_api.signals()

        elif self.path == "/api/intelligence/autonomy":
            result = self.intelligence_api.autonomy()

        else:
            self._send_response(
                404,
                {
                    "status": "not_found",
                },
            )
            return

        response = HealthResponse(
            status="ok" if result.healthy else "unhealthy",
            service=result.service,
            healthy=result.healthy,
            ready=result.ready,
            alive=result.alive,
            uptime_seconds=result.uptime_seconds,
        )

        self._send_response(
            200 if result.healthy else 503,
            response.to_dict(),
        )

    def _send_response(
        self,
        status_code: int,
        payload: dict[str, object],
    ) -> None:
        body = json.dumps(payload).encode()

        self.send_response(status_code)
        self.send_header(
            "Content-Type",
            "application/json",
        )
        self.send_header(
            "Content-Length",
            str(len(body)),
        )
        self.end_headers()

        self.wfile.write(body)

    def log_message(
        self,
        format: str,
        *args: object,
    ) -> None:
        return


class HealthServer:
    """
    Minimal production health HTTP server.
    """

    def __init__(
        self,
        port: int,
        health_service: ProductionHealthService,
    ) -> None:
        self._port = port
        self._started = False

        HealthRequestHandler.health_service = (
            health_service
        )

        HealthRequestHandler.intelligence_api = (
            IntelligenceAPI()
        )

        self._server = HTTPServer(
            (
                "0.0.0.0",
                port,
            ),
            HealthRequestHandler,
        )

    def start(self) -> None:
        if self._started:
            return

        self._started = True

        self._server.serve_forever()

    def stop(self) -> None:
        if not self._started:
            return

        self._server.shutdown()
        self._server.server_close()

        self._started = False
