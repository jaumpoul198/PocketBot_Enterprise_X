from pocketbot.bootstrap.application import build_indicator_pipeline

print("===================================")
print(" PocketBot Enterprise X")
print(" Indicator Pipeline")
print("===================================")

pipeline = build_indicator_pipeline()

registry = pipeline._manager._engine._factory._registry

print()

print("Indicadores registrados:")

for indicator in registry.names():
    print(f" - {indicator}")

print()

print(f"Total: {len(registry)} indicadores.")