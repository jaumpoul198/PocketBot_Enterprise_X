import sqlite3
from datetime import UTC, datetime
from pathlib import Path


class CognitiveStorage:

    def __init__(
        self,
        database_path="cognitive_memory.db",
    ):

        self.database_path = Path(
            database_path
        )

        self._initialize()


    def _connect(self):

        return sqlite3.connect(
            self.database_path
        )


    def _initialize(self):

        with self._connect() as connection:

            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS cognitive_decisions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    decision TEXT,
                    confidence REAL,
                    created_at TEXT
                )
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS cognitive_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT,
                    created_at TEXT
                )
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS cognitive_metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric TEXT,
                    value TEXT,
                    created_at TEXT
                )
                """
            )

            connection.commit()


    def save_decision(
        self,
        decision,
        confidence,
    ):

        with self._connect() as connection:

            connection.execute(
                """
                INSERT INTO cognitive_decisions
                (
                    decision,
                    confidence,
                    created_at
                )
                VALUES (?, ?, ?)
                """,
                (
                    str(decision),
                    confidence,
                    datetime.now(UTC).isoformat(),
                ),
            )


    def save_memory(
        self,
        content,
    ):

        with self._connect() as connection:

            connection.execute(
                """
                INSERT INTO cognitive_memory
                (
                    content,
                    created_at
                )
                VALUES (?, ?)
                """,
                (
                    str(content),
                    datetime.now(UTC).isoformat(),
                ),
            )


    def save_metric(
        self,
        metric,
        value,
    ):

        with self._connect() as connection:

            connection.execute(
                """
                INSERT INTO cognitive_metrics
                (
                    metric,
                    value,
                    created_at
                )
                VALUES (?, ?, ?)
                """,
                (
                    metric,
                    str(value),
                    datetime.now(UTC).isoformat(),
                ),
            )


    def health(self):

        return {
            "storage": "available",
            "database": str(
                self.database_path
            ),
        }
