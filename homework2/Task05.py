"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(*args):
    length = len(args)
    value = list(args[0])
    start = 0
    step = 1
    if length == 2:
        end = value.index(args[1])
    else:
        end = len(value)
    if length == 3:
        start = value.index(args[1])
        end = value.index(args[2])
    if length == 4:
        start = value.index(args[1])
        end = value.index(args[2])
        step = args[3]

    return value[start:end:step]
