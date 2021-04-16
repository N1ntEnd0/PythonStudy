import os
from contextlib import ExitStack

import pytest
from Task1 import merge_sorted_files


@pytest.fixture
def create_two_files():
    with ExitStack() as stack:
        file1 = stack.enter_context(open("file1.txt", "w"))
        file1.write("1\n3\n5\n")
        file2 = stack.enter_context(open("file2.txt", "w"))
        file2.write("2\n4\n6\n")
    yield
    os.remove("file1.txt")
    os.remove("file2.txt")


@pytest.fixture
def create_three_files():
    with ExitStack() as stack:
        file1 = stack.enter_context(open("file1.txt", "w"))
        file1.write("1\n4\n")
        file2 = stack.enter_context(open("file2.txt", "w"))
        file2.write("2\n5\n")
        file3 = stack.enter_context(open("file3.txt", "w"))
        file3.write("3\n6\n")
    yield
    os.remove("file1.txt")
    os.remove("file2.txt")
    os.remove("file3.txt")


def test_with_two_files(create_two_files):
    assert list(merge_sorted_files(["file1.txt", "file2.txt"])) == [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    ]


def test_with_three_files(create_three_files):
    assert list(merge_sorted_files(["file1.txt", "file2.txt", "file3.txt"])) == [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
    ]
