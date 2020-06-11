from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    # linear solution
    # for i, n in enumerate(nums):
    #     if target <= n:
    #         return i
    # return len(nums)
    
    # binary search solution
    l, r = 0, len(nums) - 1
    
    while(l <= r):
        mid = l + (r - l)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return l