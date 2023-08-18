from typing import Iterator, Any

from luatable import Table


def ipairs(t: Table) -> Iterator[tuple[int, Any]]:
    for i, v in enumerate(t._array_part[1:], start=1):
        if not v:
            break

        yield i, v


def pairs(t: Table) -> Iterator[tuple[Any, Any]]:
    for i, v in enumerate(t._array_part[1:], start=1):
        if not v:
            continue

        yield i, v

    for k, v in t._hash_part.items():
        yield k, v
