"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:
@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:
@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""


def cache(times=1):
    def decorator(func):
        dic = {}
        count = 0

        def wrapper(*args, **kwargs):
            tuple_args = frozenset((*args, *kwargs.items()))
            nonlocal count
            if tuple_args in dic:
                if count < times:
                    count += 1
                    return dic.get(tuple_args)
            res = func(*args, **kwargs)
            dic[tuple_args] = res
            count = 0
            return res

        return wrapper

    return decorator


@cache(1)
def f():
    return input("? ")
