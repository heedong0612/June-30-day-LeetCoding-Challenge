from typing import List

def largestDivisibleSubset(nums: List[int]) -> List[int]:
        s = set()
        dp = [ [ None for _ in range(len(nums))] for _ in range(len(nums))]
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                dp[i][j] = nums[j] % nums[i] == 0
        
        for i in range(1,len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if dp[i][j]:


if __name__ == "__main__":
    test = [1,2,3]
    print(largestDivisibleSubset(test))