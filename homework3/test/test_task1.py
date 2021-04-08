from unittest.mock import Mock

from Task01 import cache


def test_cache_decorator_with_mock():
    func = Mock(return_value=1)
    cached = cache(1)(func)
    cached(1)
    cached(1)
    assert len(func.mock_calls) == 1
