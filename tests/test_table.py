import pytest

from luatable import Table


def test_table():
    t = Table(2, 3, 4, foo="bar", func=lambda x: x+x)

    t["x"] = "string"
    t.y = 45
    t[100] = lambda x, y: " ".join([x, y + "!"])

    assert t.x == "string"
    assert t["y"] == 45
    assert t[1] == 2
    assert t[2] == 3
    assert t[3] == 4
    assert t.foo == "bar"
    assert t.func(5) == 10
    assert t.func("a") == "aa"
    assert t["non_existence"] is None
    assert t[100]("hello", "world") == "hello world!"

    del t[2]
    assert t[2] is None

    t[4] = 100
    assert t[4] == 100

    del t.x
    assert t["x"] == None
