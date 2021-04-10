import os

import pytest

from Task1 import read_magic_number


@pytest.fixture(params=["2", "1.3"])
def work_with_file(request):
    with open("text.txt", "w") as f:
        f.write(request.param)
    yield
    os.remove("text.txt")


@pytest.fixture(params=["-2", "-1.3"])
def work_with_file_negative_value(request):
    with open("text.txt", "w") as f:
        f.write(request.param)
    yield
    os.remove("text.txt")


def test_func_returned_true(work_with_file):
    assert read_magic_number("text.txt")


def test_func_returned_false(work_with_file_negative_value):
    assert read_magic_number("text.txt") is False


def test_func_returned_exeption(work_with_file):
    with pytest.raises(ValueError):
        read_magic_number("")
