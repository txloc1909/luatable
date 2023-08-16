from collections.abc import MutableSequence, MutableMapping


class Table:
    __slots__ = ("_array_part", "_hash_part")

    def __init__(self):
        self._hash_part: Optional[dict] = None
        self._array_part: Optional[list] = None

    def __getattr__(self, name):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, item, value):
        pass

    def __delitem__(self, item):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass
