import re
from platform import python_implementation

import pytest

from luatable import Table


@pytest.fixture
def array_table():
    return Table(1, 2, 3, 4, 5)


@pytest.fixture
def hash_table():
    return Table(foo="bar", bar="baz", baz=False, pi=3.14)


@pytest.fixture
def mix_table():
    return Table(1, 2, 3, 4, 5, 6, foo="bar", bar="baz", pi=3.14)


@pytest.fixture
def array_with_hole():
    t = Table(1, 2, 3)
    t[5] = 5
    return t


@pytest.mark.parametrize("index,expected", [
        (0, None), (1, 1), (7, None),
        ("foo", "bar"), ("pi", 3.14), ("baz", None),
])
def test_index_access(mix_table, index, expected):
    assert mix_table[index] == expected


def test_float_key_access(array_table):
    for i in range(len(array_table)):
        assert array_table[i] == array_table[float(i)]


def test_index_none(mix_table):
    with pytest.raises(ValueError, match="table index is nil"):
        mix_table[None] = 1


def test_table_as_index():
    t = Table()
    i = Table()
    t[i] = True
    assert t[i]


def test_table_equality():
    t1 = Table(1, foo="bar")
    t2 = Table(1, foo="bar")
    t3 = t1
    assert t1 == t3
    assert t1 != t2


def test_dot_access(hash_table):
    assert hash_table["foo"] == hash_table.foo
    assert hash_table["bar"] == hash_table.bar
    assert hash_table.pi == 3.14
    assert hash_table[hash_table.foo] == "baz"


def test_dot_assign(hash_table):
    hash_table.key = "value"
    assert hash_table["key"] == "value"


def test_del_attr(hash_table):
    assert hash_table.baz == False
    del hash_table.baz
    assert hash_table.baz is None


def test_del_item(mix_table):
    del mix_table[2]
    assert mix_table[2] is None

    del mix_table["bar"]
    assert mix_table["bar"] is None


def test_array_grow():
    t = Table()
    t[2] = 2
    assert len(t) == 0
    t[1] = 1
    assert len(t) == 2
    t[3] = 3
    assert len(t) == 3
    t[4] = 4
    assert len(t) == 4


def test_create_hole_in_array(array_table):
    assert len(array_table) == 5
    del array_table[4]
    assert len(array_table) == 3


def test_fill_hole_in_array(array_with_hole):
    assert len(array_with_hole) == 3
    assert array_with_hole[5] == 5
    assert array_with_hole[4] is None
    array_with_hole[4] = 4
    assert len(array_with_hole) == 5


def test_create_sparse_table():
    t = Table()
    t[2] = True
    t[5] = True
    t[10] = True
    t[100] = True
    assert len(t) == 0

@pytest.mark.skipif(python_implementation() != "CPython",
                    reason="Depend on CPython implementation details of `id()`")
def test_table_to_str():
    assert re.match(r"table: 0x[0-9a-f]{12}", str(Table()))
