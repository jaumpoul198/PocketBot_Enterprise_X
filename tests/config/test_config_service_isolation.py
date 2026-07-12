from __future__ import annotations

from pathlib import Path

from pocketbot.config.service import ConfigService


def test_loaded_configuration_is_isolated_from_external_mutation(
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

    config = service.load("app.yaml")

    config["database"]["host"] = "changed"

    stored = service.load("app.yaml")

    assert stored["database"]["host"] == "localhost"


def test_multiple_loads_return_isolated_configuration_instances(
    tmp_path: Path,
) -> None:
    config_file = tmp_path / "app.yaml"

    config_file.write_text(
        """
runtime:
  mode: production
""",
        encoding="utf-8",
    )

    service = ConfigService(tmp_path)

    first = service.load("app.yaml")
    second = service.load("app.yaml")

    assert first is not second

    first["runtime"]["mode"] = "development"

    assert second["runtime"]["mode"] == "production"
