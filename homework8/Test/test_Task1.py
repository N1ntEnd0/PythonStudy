import pytest
from Task1 import KeyValueStorage


@pytest.fixture
def storage():
    return KeyValueStorage("../task1.txt")


def test_access_with_attributes(storage):
    assert storage.name == "kek"
    assert storage.song == "shadilay"


def test_accessible_as_collection(storage):
    assert storage["name"] == "kek"
    assert storage["power"] == "9001"


def test_len(storage):
    assert len(storage) == 4


def test_contains(storage):
    assert "name" in storage
