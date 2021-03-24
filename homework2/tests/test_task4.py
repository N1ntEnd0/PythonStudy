import pytest
from Task04 import cache, func


@pytest.mark.parametrize(["value1", "value2"], [(1, 2), (100, 200), (0, 0)])
def test_cache_func(value1, value2):
    cache_func = cache(func)
    some = value1, value2
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
