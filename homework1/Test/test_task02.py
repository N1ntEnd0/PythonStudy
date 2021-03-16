import pytest
from Task02 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([0, 1, 1], True),
        ([0, 1], True),
        ([1, 1], True),
        ([0, 1, 2], False),
        ([], True),
        ([0, 1, 1, 2, 3, 5, 8], True),
    ],
)
def test_function(value, expected_result):
    assert check_fibonacci(value) == expected_result
