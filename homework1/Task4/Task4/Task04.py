"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List

# main idea of this method (a[i] + b[i]) == (-c[k] - d[l])


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    dic = {}
    res = 0
    for i in a:
        for j in b:
            if i + j in dic:
                dic[i + j] += 1
            else:
                dic[i + j] = 1
    for k in c:
        for l in d:
            if -k - l in dic:
                # dic[-k -l] += 1
                res += dic.get(-k - l)
    print(dic)
    return res
