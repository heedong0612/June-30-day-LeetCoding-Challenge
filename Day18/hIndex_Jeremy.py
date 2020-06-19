from typing import List

def hIndex(citations: List[int]) -> int:
    '''
    Got it from 
    https://www.youtube.com/watch?v=CjKJDloMnwE
    '''
    size = len(citations)
    l, r = 0, size - 1
    
    while l <= r:
        mid = l + (r - l) // 2
        if citations[mid] == size - mid:
            return citations[mid]
        elif citations[mid] > size - mid:
            r = mid - 1
        else:
            l = mid + 1
        
    return n - l