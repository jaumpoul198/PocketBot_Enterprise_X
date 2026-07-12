from __future__ import annotations

from pathlib import Path

from pocketbot.config.service import ConfigService


def test_config_cache_is_isolated_from_loader_result(
    tmp_path: Path,
) -> None:
    config_file = tmp_path / "app.yaml"

    config_file.write_text(
        """
database:
  host: localhost
""",
        encoding="utf-8",
    )

    service = ConfigService(tmp_path)

    first = service.load("app.yaml")

    first["database"]["host"] = "changed"

    second = service.load("app.yaml")

    assert second["database"]["host"] == "localhost"
