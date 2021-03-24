import pytest

from Task04 import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"], [(10, False), (9, True), (153, True), (0, True)]
)
def test_number(value, expected_result):
    assert is_armstrong(value) == expected_result
