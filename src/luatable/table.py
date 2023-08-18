from typing import Final, Any


class Table:
    __slots__ = ("_array_part", "_hash_part")

    def __init__(self, *args, **kwargs):
        self._array_part: Final[list] = [None, *args]
        self._hash_part: Final[dict] = kwargs

    def __hash__(self):
        return id(self)

    def __eq__(self, other: Any) -> bool:
        return self is other

    def __getattr__(self, name: str) -> Any:
        return self._hash_part.get(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self.__slots__:
            self._hash_part[name] = value
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        del self._hash_part[name]

    def __getitem__(self, item: Any) -> Any:
        if isinstance(item, int) and item < len(self._array_part):
            return self._array_part[item]

        return self._hash_part.get(item)

    def __setitem__(self, item, value):
        if isinstance(item, int):
            if item < len(self._array_part):
                self._array_part[item] = value
                return
            elif item == len(self._array_part):
                self._array_part.append(value)
                return

        self._hash_part[item] = value

    def __delitem__(self, item):
        self[item] = None

    def __len__(self) -> int:
        return len(self._array_part)

    def __repr__(self) -> str:
        return f"table: {hex(id(self))}"
