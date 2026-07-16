from pocketbot.enterprise.api.intelligence.intelligence_routes import (
    intelligence_bp,
)

from flask import Flask


def create_app():

    app = Flask(__name__)

    app.register_blueprint(
        intelligence_bp
    )

    return app


def test_intelligence_status_api():

    app = create_app()

    client = app.test_client()

    response = client.get(
        "/intelligence/status"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "active"


def test_context_history_api():

    app = create_app()

    client = app.test_client()

    response = client.get(
        "/intelligence/context/history"
    )

    assert response.status_code == 200
