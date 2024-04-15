"""
Implement lua stdlib functions from:
    https://www.lua.org/manual/5.4/manual.html#6.6
"""

import operator
from typing import Any, Callable, Optional, Tuple

from luatable import Table


def concat(list_: Table, sep: str = "", i: int = 1, j: Optional[int] = None) -> str:
    if not j:
        j = len(list_)

    if i > j:
        return ""

    return sep.join(list_[idx] for idx in range(i, j + 1))


def insert(list_: Table, value: Any, pos: Optional[int] = None):
    return NotImplemented


def move(a1: Table, from_: int, end: int, to: int, a2: Optional[Table] = None) -> Table:
    return NotImplemented


def pack(*args) -> Table:
    return NotImplemented


def remove(list_: Table, pos: Optional[int] = None) -> Table:
    return NotImplemented


def sort(list_: Table, comp: Callable[[Any, Any], bool] = operator.lt):
    return NotImplemented


def unpack(list_: Table, i: int = 1, j: Optional[int] = None) -> Tuple[Any]:
    return NotImplemented
