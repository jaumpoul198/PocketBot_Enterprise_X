# -*- coding: utf-8 -*-

from pathlib import Path

from pocketbot.config import ConfigLoader

loader = ConfigLoader(Path("config"))

config = loader.load("app.yaml")

print("=" * 60)
print("CONFIGURACAO OK")
print("=" * 60)
print(config)