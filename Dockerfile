FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app/src

RUN useradd \
    --create-home \
    --shell /bin/bash \
    pocketbot

RUN mkdir -p \
    /app/config \
    /app/logs

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY config ./config

RUN chown -R pocketbot:pocketbot /app

USER pocketbot

EXPOSE 8000

HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=10s \
    --retries=3 \
    CMD python -c "import pocketbot" || exit 1

CMD [
    "python",
    "-m",
    "pocketbot.production.entrypoint.application"
]
