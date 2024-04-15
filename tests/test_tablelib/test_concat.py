import pytest

from luatable import Table
from luatable.table import concat


def test_concat_strings():
    assert concat(Table("hello", " ", "world")) == "hello world"


def test_concat_strings_and_numbers():
    assert concat(Table("hello", "world", 3.14)) == "helloworld3.14"


def test_concat_strings_with_sep():
    assert concat(Table("hello", "world", "hi", "mom"), sep=" ") == "hello world hi mom"


def test_concat_valid_range():
    assert concat(Table(1, 2, 3, 4, 5), i=2, j=4) == "234"


def test_concat_invalid_range():
    assert concat(Table(1, 2, 3), i=3, j=1) == ""


def test_concat_nil():
    assert concat(Table(None)) == ""


@pytest.mark.parametrize("value", [None, True, False, Table()])
def test_invalid_values(value):
    with pytest.raises(ValueError):
        _ = concat(Table("hello", value))
