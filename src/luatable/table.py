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
        pass

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
        return len(self._array_part) + len(self._hash_part)

    def __iter__(self):
        pass


if __name__ == "__main__":
    t = Table(2, 3, 4, 5, func=lambda x: x * x)

    t["x"] = "string"
    t.y = 45
    t[200] = lambda s: "### " + s + " ###"

    assert t.x == "string"
    assert t["y"] == 45
    assert t[1] == 2
    assert t[2] == 3
    assert t[3] == 4
    assert t[4] == 5
    assert t.func(5) == 25
    assert t["non_existence"] is None
    assert t[200]("hello") == "### hello ###"

    del t[4]
    assert t[4] is None

    t[4] = 100
    assert t[4] == 100
