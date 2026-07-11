from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .event import Event


@dataclass(slots=True)
class ApplicationStarted(Event):
    """
    Evento emitido quando o runtime da aplicação inicia.
    """

    name: str = field(
        default="application.started",
        init=False,
    )

    payload: dict[str, Any] = field(
        default_factory=dict,
        init=False,
    )


@dataclass(slots=True)
class ApplicationStopped(Event):
    """
    Evento emitido quando o runtime da aplicação encerra.
    """

    name: str = field(
        default="application.stopped",
        init=False,
    )

    payload: dict[str, Any] = field(
        default_factory=dict,
        init=False,
    )


@dataclass(slots=True)
class ApplicationStartupFailed(Event):
    """
    Evento emitido quando a inicialização da aplicação falha.
    """

    name: str = field(
        default="application.startup.failed",
        init=False,
    )

    payload: dict[str, Any] = field(
        default_factory=dict,
        init=False,
    )


@dataclass(slots=True)
class ApplicationShutdownRequested(Event):
    """
    Evento emitido quando o encerramento da aplicação é solicitado.
    """

    name: str = field(
        default="application.shutdown.requested",
        init=False,
    )

    payload: dict[str, Any] = field(
        default_factory=dict,
        init=False,
    )


@dataclass(slots=True)
class ApplicationShutdownCompleted(Event):
    """
    Evento emitido quando o encerramento da aplicação termina.
    """

    name: str = field(
        default="application.shutdown.completed",
        init=False,
    )

    payload: dict[str, Any] = field(
        default_factory=dict,
        init=False,
    )
