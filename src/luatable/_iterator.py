from typing import Any, Iterator

from ._table import Table


def ipairs(t: Table) -> Iterator[tuple[int, Any]]:
    for i, v in enumerate(t._array_part[1:], start=1):
        if v is None:
            break

        yield i, v


def pairs(t: Table) -> Iterator[tuple[Any, Any]]:
    for i, v in enumerate(t._array_part[1:], start=1):
        if v is None:
            continue

        yield i, v

    if t._array_part[0] is not None:
        yield 0, t._array_part[0]

    for k, v in t._hash_part.items():
        yield k, v
