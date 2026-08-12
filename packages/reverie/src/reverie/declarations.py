"""Declarations a world makes about its own fact types.

The engine enforces these. It does not author them, and it does not know what
any of them mean -- only whether a given write is permitted by the declaration
the world supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Writer(Enum):
    """Who is attempting a write.

    The distinction is the whole point of a declaration: the same write is
    permitted from one writer and refused from another.
    """

    AUTHOR = "author"
    SIMULATION = "simulation"


@dataclass(frozen=True)
class Declaration:
    """What a world says about one of its fact types.

    Attributes:
        actionable: Whether the simulation may write facts of this type. When
            false, only the author may -- the simulation can read it but has no
            path to change it.
    """

    actionable: bool


@dataclass(frozen=True)
class World:
    """A world's declarations, keyed by fact type.

    The engine never inspects the keys. They are the world's vocabulary, and a
    different world will use entirely different ones.
    """

    declarations: dict[str, Declaration]

    @classmethod
    def from_mapping(cls, raw: dict[str, dict[str, bool]]) -> World:
        """Build a world from plain data.

        Args:
            raw: Fact type name to its declared properties.

        Returns:
            The world.

        Raises:
            UndeclaredFactType: If any entry omits `actionable`. A fact type
                with no stated ownership is not a permissive default -- it is
                an authoring error, and it fails here rather than at write time.
        """
        declarations: dict[str, Declaration] = {}
        for fact_type, props in raw.items():
            if "actionable" not in props:
                raise UndeclaredFactType(
                    f"fact type {fact_type!r} does not declare `actionable`; "
                    "absence of a declaration is not permission"
                )
            declarations[fact_type] = Declaration(actionable=props["actionable"])
        return cls(declarations=declarations)


class UndeclaredFactType(Exception):
    """A fact type carries no declaration, so no write to it can be judged."""


class NotActionable(Exception):
    """The simulation attempted a write the world reserved for its author."""
