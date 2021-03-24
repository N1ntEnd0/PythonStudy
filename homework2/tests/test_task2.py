import pytest

from Task02 import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([3, 2, 3], (3, 2)), ([2, 2, 1, 1, 1, 2, 2], (2, 1)), ([2, 2, 2], (2, 2))],
)
def test1(value, expected_result):
    assert major_and_minor_elem(value) == expected_result
