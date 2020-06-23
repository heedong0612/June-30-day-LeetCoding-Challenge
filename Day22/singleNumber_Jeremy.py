from collections import defaultdict as dd
from typing import List

def singleNumber(nums: List[int]) -> int:
    d = dd(lambda : 3)
    for n in nums:
        d[n] -= 1
        if d[n] == 0:
            d.pop(n)
        
    print(d.keys())
    return d[list(d.keys())[0]]

if __name__ == "__main__":
    singleNumber([2, 2, 3, 2])