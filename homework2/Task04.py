"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    dic = {}

    def wrapper(*args, **kwargs):

        tuple_args = (*args, tuple(*kwargs.items()))
        if tuple_args in dic:
            return dic.get(tuple_args)
        res = func(*args, **kwargs)
        dic[tuple_args] = res
        return res

    return wrapper


def func(a, b=2):
    return (a ** b) ** 2
