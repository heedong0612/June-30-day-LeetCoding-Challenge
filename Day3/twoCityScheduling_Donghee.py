class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [[0, 0] for x in range(len(costs))] # diff = A - B
        
        for i in range(len(costs)) :
            diff[i] = [costs[i][0] - costs[i][1], i]

        diff.sort(reverse = True) # big to small
        
        count = 0
        limit = len(costs) / 2
        res = 0
        
        while (count < limit) :
            # diff[count][1] is the personID of whom should go to city B
            res += costs[diff[count][1]][1]
            count += 1
            
        while (count < len(costs)) :
            res += costs[diff[count][1]][0]
            count += 1
        
        return res