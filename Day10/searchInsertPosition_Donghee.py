### Linear search ###

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)


### binary search ###

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
        
#         i = 0
#         j = len(nums)
        
#         while i < j:
#             mid = i + (j - i) // 2
            
#             if target == nums[mid]:
#                 return mid
            
#             if target < nums[mid]:
#                 j = mid
#             else :
#                 i = mid + 1
            
#         return i
    
