"""
PocketBot Enterprise X
Core - Exceptions
"""

from __future__ import annotations


class PocketBotError(Exception):
    """
    Exceção base do PocketBot.
    """

    default_message = "Ocorreu um erro interno no PocketBot."

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.default_message
        super().__init__(self.message)


class ConfigurationError(PocketBotError):
    """
    Erro relacionado às configurações do sistema.
    """

    default_message = "Erro na configuração do sistema."


class DatabaseError(PocketBotError):
    """
    Erro relacionado ao banco de dados.
    """

    default_message = "Erro de banco de dados."


class ValidationError(PocketBotError):
    """
    Erro de validação.
    """

    default_message = "Erro de validação."


class MarketError(PocketBotError):
    """
    Erro relacionado ao mercado.
    """

    default_message = "Erro de mercado."


class StrategyError(PocketBotError):
    """
    Erro relacionado às estratégias.
    """

    default_message = "Erro de estratégia."


class ExecutionError(PocketBotError):
    """
    Erro relacionado à execução de operações.
    """

    default_message = "Erro de execução."


class AIError(PocketBotError):
    """
    Erro relacionado aos módulos de IA.
    """

    default_message = "Erro no módulo de inteligência artificial."
