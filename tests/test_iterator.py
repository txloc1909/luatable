import pytest

from luatable import Table, pairs, ipairs


@pytest.fixture
def test_table():
    t = Table()
    t[-1] = "y"
    t[0] = "z"
    t[1] = "a"
    t[3] = "b"
    t[2] = "c"
    t[4] = "d"
    t[6] = "e"
    t["hello"] = "world"
    return t


def test_pairs(test_table):
    output = tuple(pairs(test_table))

    # `pairs` guarantee no order, so just check if output exists
    assert (1, "a") in output
    assert (2, "c") in output
    assert (3, "b") in output
    assert (4, "d") in output
    assert (0, "z") in output
    assert (6, "e") in output
    assert ("hello", "world") in output
    assert (-1, "y") in output


def test_ipairs(test_table):
    output = tuple(ipairs(test_table))

    # numeric order of keys is guaranteed in `ipairs`
    expected = ((1, "a"), (2, "c"), (3, "b"), (4, "d"))

    assert output == expected
