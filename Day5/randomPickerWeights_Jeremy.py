from random import randint
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        tot = 0
        for i, weight in enumerate(self.w):
            tot += weight
            self.w[i] = tot

    def pickIndex(self) -> int:
        '''
        Passed 99% of test
        Fails in stress test :(
        '''
        # w[0] = weight of index 0
        totalWeight = self.w[-1]
        r = randint(0, totalWeight)
        print(f'r: {r}')
        left, right = 0, len(self.w) - 1
        ans = -1
        if r == totalWeight:
            return len(self.w) - 1
        
        # binary search sol
        while(left <= right):
            mid = left + (right - left) // 2
            if r < self.w[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        
        # linear sol
        for i, weight in enumerate(self.w):
            # tot += weight
            if r <= weight:
                return i