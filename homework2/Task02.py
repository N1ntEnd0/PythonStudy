"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    const = len(inp) // 2
    d = {}
    for i in inp:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    max_key = inp[0]
    min_key = inp[0]
    max_frequency = d.get(max_key)
    min_frequency = d.get(min_key)
    for key, frequency in d.items():
        if frequency > max_frequency and frequency > const:
            max_frequency = frequency
            max_key = key
        if frequency < min_frequency:
            min_frequency = frequency
            min_key = key

    return max_key, min_key


# done
