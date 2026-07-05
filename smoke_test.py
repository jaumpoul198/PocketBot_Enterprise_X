from pocketbot.bootstrap.application import build_indicator_pipeline

pipeline = build_indicator_pipeline()

print(type(pipeline).__name__)
print("OK")