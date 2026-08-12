"""Reverie — a world that keeps living when you are not there.

The engine enforces declarations it did not author. It may know that a change is
reserved. It may not know what that change means.
"""

from reverie.declarations import (
    Declaration,
    NotActionable,
    UndeclaredFactType,
    World,
    Writer,
)
from reverie.engine import may_write, write

__all__ = [
    "Declaration",
    "NotActionable",
    "UndeclaredFactType",
    "World",
    "Writer",
    "may_write",
    "write",
]
