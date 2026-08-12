"""The engine: enforcement of declarations it did not author.

Every function here decides using only the world's own declarations. Nothing in
this module names a fact type, and nothing in it would change if you deleted a
world and invented a completely different one.
"""

from __future__ import annotations

from reverie.declarations import NotActionable, UndeclaredFactType, World, Writer


def may_write(world: World, fact_type: str, writer: Writer) -> bool:
    """Whether `writer` may write a fact of `fact_type` in `world`.

    Args:
        world: The world whose declarations govern.
        fact_type: The type being written. Meaningful to the world, opaque here.
        writer: Who is attempting it.

    Returns:
        True if the write is permitted.

    Raises:
        UndeclaredFactType: If the world declared nothing about this type.
    """
    if writer is Writer.AUTHOR:
        return True
    declaration = world.declarations.get(fact_type)
    if declaration is None:
        raise UndeclaredFactType(
            f"fact type {fact_type!r} is undeclared in this world; "
            "the engine will not guess an owner"
        )
    return declaration.actionable


def write(world: World, fact_type: str, writer: Writer) -> None:
    """Perform a write, or refuse it.

    Args:
        world: The world whose declarations govern.
        fact_type: The type being written.
        writer: Who is attempting it.

    Raises:
        NotActionable: If the world reserved this type for its author.
        UndeclaredFactType: If the world declared nothing about this type.
    """
    if not may_write(world, fact_type, writer):
        raise NotActionable(
            f"{writer.value} may not write {fact_type!r}: this world declares it "
            "not actionable"
        )
