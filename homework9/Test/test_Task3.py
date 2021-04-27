import os
from contextlib import ExitStack

import pytest
from Task3 import universal_file_counter


@pytest.fixture
def create_two_files():
    with ExitStack() as stack:
        file1 = stack.enter_context(open("file1.txt", "w"))
        file1.write("1\n3\n5 4\n")
        file2 = stack.enter_context(open("file2.txt", "w"))
        file2.write("2\n4\n65 5\n")
    yield
    os.remove("file1.txt")
    os.remove("file2.txt")


def test_without_tokenizer(create_two_files):
    assert universal_file_counter("./", "txt") == 6


def test_with_tokenizer(create_two_files):
    assert universal_file_counter("./", "txt", str.split) == 8
