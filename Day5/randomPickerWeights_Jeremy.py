from random import randint
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        tot = 0
        for i, weight in enumerate(self.w):
            tot += weight
            self.w[i] = tot
        self.totalWeight = tot

    def pickIndex(self) -> int:
        '''
        Passed 99% of test
        Fails in stress test :(
        '''
        r = randint(0, self.totalWeight - 1)
        left, right = 0, len(self.w) - 1
        
        if r == self.totalWeight:
            return len(self.w) - 1
        if r == 0:
            return 0
        
        
        # binary search sol
        while(left < right):
            mid = left + (right - left) // 2
            if r < self.w[mid]:
                right = mid
            else:
                left = mid + 1
        return right
        
        # linear sol
#         for i, weight in enumerate(self.w):
#             # tot += weight
#             if r <= weight:
#                 return i