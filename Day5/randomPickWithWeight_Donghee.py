class Solution:

    def __init__(self, w: List[int]):
        global wSum
        wSum = 0
        global ran
        ran = []
        
        for x in w :
            wSum += x
            ran.append(wSum)

    def pickIndex(self) -> int:
        randIndex = randint(0, wSum - 1)
        
        start = 0
        end = len(ran)
        
        while (start < end) :
            mid = start + (end - start) // 2
            
            if (randIndex >= ran[mid]) :
                start = mid + 1
            else :
                end = mid
            
        return end
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()