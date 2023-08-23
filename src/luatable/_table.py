from typing import Final, Any
from math import log2, ceil


def _can_be_int(x: int | float) -> bool:
    return isinstance(x, int) or (isinstance(x, float) and x.is_integer())


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
        if _can_be_int(item) and 0 <= item < len(self._array_part):
            return self._array_part[int(item)]

        return self._hash_part.get(item)

    def __setitem__(self, index: Any, value: Any) -> None:
        if index is None:
            raise ValueError("table index is nil")

        if _can_be_int(index):
            self._set_int_key(index, value)
            return

        self._hash_part[index] = value

    def __delitem__(self, item):
        self[item] = None

    def __len__(self) -> int:
        for i, v in enumerate(l[1:], start=1):
            if v is None:
                return i - 1

        return len(self._array_part) - 1

    def __repr__(self) -> str:
        return f"table: {hex(id(self))}"

    def _count_positive_int_key(self) -> tuple[list[int], list[int]]:
        # buckets[i]: number of int key k where: 2**(i-1) < k <= 2**i
        buckets: list[int] = [0, ]

        # first, count in array part
        for i, v in enumerate(self._array_part[1:], start=1):
            if i > 2**(len(buckets) - 1):
                buckets.append(0)

            if v is not None:
                buckets[-1] += 1

        # then, count in hash part
        int_keys_in_hash_part: list[int] = []
        positive_int_key = lambda key: _can_be_int(key) and key > 0
        for k in filter(positive_int_key, self._hash_part.keys()):
            i = ceil(log2(k))                   # bucket that `k` belongs to
            if i >= len(buckets):
                num_new_buckets = i - len(buckets) + 1
                buckets.extend([0] * num_new_buckets)

            buckets[-1] += 1
            int_keys_in_hash_part.append(k)

        return buckets, int_keys_in_hash_part

    @staticmethod
    def _optimal_array_size(buckets: list[int]) -> int:
        optimal: int = 0
        cum_sum: int = 0
        for i, count in enumerate(buckets, start=1):
            cum_sum += count
            if cum_sum >= 2**(i-1):
                optimal = 2**i
        return optimal

    def _set_int_key(self, index: int, value: Any) -> None:
        if index < 0:               # Negative key always goes into hash part
            self._hash_part[index] = value
            return
        elif 0 <= index < len(self._array_part): # Trivial case for array part
            self._array_part[index] = value
            return

        # Grow the array part
        ## First, counting positive integer keys in table
        buckets, int_keys_in_hash_part = self._count_positive_int_key()

        ## Calculate optimal size for array part
        optimal = self._optimal_array_size(buckets)

        ## Extend array part and move keys from hash part
        extra_size = optimal - len(self._array_part) + 1
        self._array_part.extend([None] * extra_size)

        moving_keys = filter(lambda key: key <= optimal, int_keys_in_hash_part)
        for k in moving_keys:
            self._array_part[k] = self._hash_part[k]
            del self._hash_part[k]

        # Finally, assign the index
        if index < len(self._array_part):
            self._array_part[index] = value
        else:
            self._hash_part[index] = value
