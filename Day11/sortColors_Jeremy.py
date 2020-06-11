from typing import List
from collections import Counter

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # construct Counter dict
    c = Counter(nums)

    i = 0
    # sorted(c) returns a dictionary sorted by its keys
    for k in sorted(c):
        for _ in range(c[k]):
            nums[i] = k
            i += 1