import pytest
from Task2 import TableData


@pytest.fixture
def presidents():
    with TableData(database_name="../example.sqlite", table_name="presidents") as td:
        yield td


def test_len(presidents):
    assert len(presidents) == 3


def test_get_attr(presidents):
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_check_include(presidents):
    assert "Yeltsin" in presidents


def test_iteration_capability(presidents):
    lst = ["Yeltsin", "Trump", "Big Man Tyrone"]
    for i in presidents:
        assert i["name"] in lst
