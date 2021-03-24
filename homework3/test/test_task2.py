from timeit import default_timer as timer

from Task02 import calc_total_sum


def test_func_time():
    start = timer()
    calc_total_sum()
    end = timer()
    assert end - start < 60
