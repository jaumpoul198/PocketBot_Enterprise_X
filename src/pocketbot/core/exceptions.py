"""
PocketBot Enterprise X
Core - Exceptions

Exceções centralizadas do sistema.
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
    Erro de configuração.
    """

    default_message = "Erro na configuração do sistema."


class DatabaseError(PocketBotError):
    """
    Erro relacionado ao banco de dados.
    """

    default_message = "Erro ao acessar o banco de dados."


class MarketError(PocketBotError):
    """
    Erro relacionado ao mercado.
    """

    default_message = "Erro ao obter dados do mercado."


class StrategyError(PocketBotError):
    """
    Erro relacionado às estratégias.
    """

    default_message = "Erro na execução da estratégia."


class AIEngineError(PocketBotError):
    """
    Erro relacionado ao motor de IA.
    """

    default_message = "Erro no mecanismo de Inteligência Artificial."


class ValidationError(PocketBotError):
    """
    Erro de validação.
    """

    default_message = "Falha na validação dos dados."