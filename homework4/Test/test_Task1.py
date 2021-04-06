import os

import pytest
from Task1 import read_magic_number


@pytest.fixture(params=["2", "1.3"])
def work_with_file(request):
    with open("text.txt", "w") as f:
        f.write(request.param)
    yield
    os.remove("text.txt")


def test_func(work_with_file):
    assert read_magic_number("text.txt")
