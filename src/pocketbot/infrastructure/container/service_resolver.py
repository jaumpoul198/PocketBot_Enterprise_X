"""
PocketBot Enterprise X
Infrastructure Container

Service resolver responsible for constructor injection.
"""

from __future__ import annotations

import inspect
import types
from typing import Any, Union, get_args, get_origin

from pocketbot.infrastructure.container.exceptions import (
    CircularDependencyError,
    ServiceResolutionError,
)


class ServiceResolver:
    """
    Creates service instances using constructor injection.
    """

    def __init__(self) -> None:
        self._resolution_stack: list[type[Any]] = []

    @staticmethod
    def _unwrap_optional(
        annotation: Any,
    ) -> tuple[Any, bool]:
        """
        Extracts the real type from Optional[T] / T | None.
        """

        origin = get_origin(annotation)

        if origin is Union or isinstance(
            annotation,
            types.UnionType,
        ):
            args = get_args(annotation)

            non_none_types = [
                arg
                for arg in args
                if arg is not type(None)
            ]

            if len(non_none_types) == 1:
                return non_none_types[0], True

        return annotation, False

    def create_instance(
        self,
        implementation_type: type[Any],
        provider: Any,
    ) -> Any:
        """
        Creates an instance resolving constructor dependencies.
        """

        if implementation_type in self._resolution_stack:
            chain = " -> ".join(
                cls.__name__
                for cls in (
                    *self._resolution_stack,
                    implementation_type,
                )
            )

            raise CircularDependencyError(
                f"Circular dependency detected: {chain}"
            )

        self._resolution_stack.append(implementation_type)

        try:
            constructor = implementation_type.__init__
            signature = inspect.signature(constructor)

            type_hints = inspect.get_annotations(
                constructor,
                eval_str=True,
            )

            kwargs: dict[str, Any] = {}

            for name, parameter in signature.parameters.items():

                if name == "self":
                    continue

                if parameter.kind in (
                    inspect.Parameter.VAR_POSITIONAL,
                    inspect.Parameter.VAR_KEYWORD,
                ):
                    continue

                annotation = type_hints.get(
                    name,
                    parameter.annotation,
                )

                if annotation is inspect.Parameter.empty:
                    raise ServiceResolutionError(
                        f"Constructor parameter '{name}' "
                        f"of '{implementation_type.__name__}' "
                        "must have a type annotation."
                    )

                dependency_type, optional = self._unwrap_optional(
                    annotation
                )

                try:
                    dependency = provider.get_service(
                        dependency_type
                    )
                except ServiceResolutionError:
                    if optional:
                        dependency = None
                    else:
                        raise

                kwargs[name] = dependency

            return implementation_type(**kwargs)

        finally:
            self._resolution_stack.pop()
