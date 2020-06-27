from typing import List

def findDuplicate(nums: List[int]) -> int:
    '''
    Runtime: 64ms -> O(n)
    Memory: 16.4mb -> O(n)
    '''    
    d = {}
    
    for n in nums:
        # I use try/except instead of checkin with 'in' 
        # because I believe in iterates through all keys? 
        # but I saw a faster solution on leetcode using 'in' #bruh
        try:
            d[n]
            return n
        except:
            d[n] = 0
    return 0