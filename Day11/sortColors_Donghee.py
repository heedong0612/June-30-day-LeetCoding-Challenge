class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        ptr = len(nums) - 1
        ptr2 = ptr
        
        while curr <= ptr :
            if nums[ptr] == 2:
                nums[ptr] = nums[ptr2]
                nums[ptr2] = 2
                
                ptr2 -= 1
                ptr -= 1
                
            elif nums[ptr] == 0:
                nums[ptr] = nums[curr]
                nums[curr] = 0
                curr += 1
                
            else :
                ptr -= 1
        