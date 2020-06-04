from functools import reduce
from typing import List

class Pair:
    def __init__(self, p: List[int]):
        self.first = p[0]
        self.second = p[1]
    
    @property
    def diff(self):
        return abs(self.first - self.second)
    
    def __lt__(self, other): 
        return self.diff < other.diff
    
    def __str__(self):
        return f'<{self.first}, {self.second}>'
    
    def __repr__(self):
        return self.__str__()

def twoCitySchedCost(costs: List[List[int]]) -> int:
    '''
    Wrote all this crap and still ended up just having 
    three lines of code as a solution :') 
    '''
    # half = len(costs)//2

    # copy = []
    # for p in costs:
    #     copy.append(Pair(p))
    # copy.sort()
    # print(copy)
    # A, B = [], []
    # ans = 0

    # for i in range(half, len(costs)):
    #     if copy[i].first < copy[i].second:
    #         A.append([copy[i].first, i])
    #     else:
    #         B.append([copy[i].second, i])
    # A.sort(key = lambda p : p[0])
    # B.sort(key = lambda p : p[0])

    # for i in range(half):
    #     if copy[i].first < copy[i].second:
    #         if len(A) == half: # if full
    #             temp = A.pop()
    #             idx = temp[1]
    #             val = copy[idx].second
    #             A.append([copy[i].first, i])
    #             A.sort(key = lambda p : p[0])
    #             B.append([val, idx])
    #             B.sort(key = lambda p : p[0])
    #         else:
    #             A.append([copy[i].first, i])
    #             A.sort(key = lambda p : p[0])
    #     else:
    #         if len(B) == half: # if full
    #             temp = B.pop()
    #             idx = temp[1]
    #             val = copy[idx].first

    #             B.append([copy[i].second, i])
    #             B.sort(key = lambda p : p[0])

    #             A.append([val, idx])
    #             A.sort(key = lambda p : p[0])
    #         else:    
    #             B.append([copy[i].second, i])
    #             B.sort(key = lambda p : p[0])

    # print(A)
    # print(B)
    # for i in range(len(A)):
    #     ans += A[i][0] + B[i][0]
    # return ans

    diff = [j - i for i, j in costs]
    first = [i for i, _ in costs]
    return sum(first) + sum(sorted(diff)[:len(diff)//2])
        
            





if __name__ == "__main__":
    # costs = [[10,20],[30,200],[400,50],[30,20]]
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    # costs = [[518,518],[71,971],[121,862],[967,607],[138,754],[513,337],[499,873],[337,387],[647,917],[76,417]]
    print(f'ans : {twoCitySchedCost(costs)}')
       