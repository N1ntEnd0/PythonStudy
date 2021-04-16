"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


@contextmanager
def supressor(exception):
    try:
        yield
    except exception:
        pass


class Supressor:
    def __init__(self, exception):
        self._exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self._exception:
            return True
        else:
            return False
