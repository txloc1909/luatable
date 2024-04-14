"""
Implement lua stdlib functions from:
    https://www.lua.org/manual/5.4/manual.html#6.6
"""

import operator
from typing import Any, Callable, Optional, Tuple

from luatable import Table


def concat(list_: Table, sep: str = "", i: int = 1, j: Optional[int] = None) -> str:
    return NotImplemented


def insert(list_: Table, value: Any, pos: Optional[int] = None) -> None:
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
